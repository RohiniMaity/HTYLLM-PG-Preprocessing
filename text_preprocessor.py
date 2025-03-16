import os
import datasets
from datasets import load_dataset

OUTPUT_FILE_TEMPLATE = "/shared-file-storage/preprocessed_data/preprocessed_{rank}.txt"

def preprocess_text(text):
    return text.lower().strip().split()

def load_dataset(data_path, shard_index, num_shards):
    """Loads a shard of the C4 dataset in streaming mode."""
    try:
        dataset = load_dataset('allenai/c4', 'multilingual', split=f'train', data_dir=data_path, shard_index=shard_index, num_shards=num_shards, streaming=True)
        return [example['text'] for example in dataset]
    except Exception as e:
        print(f"Error loading dataset shard {shard_index}: {e}")
        return []

def write_preprocessed_text(preprocessed_text, rank):
    with open(OUTPUT_FILE_TEMPLATE.format(rank=rank), "w") as f:
        for line in preprocessed_text:
            f.write("\t".join(line))
            f.write("\n")

def main():
    local_rank = int(os.environ.get("PROC_RANK", 0))
    total_procs = int(os.environ.get("TOTAL_PROCS", 1))
    data_path = os.environ.get("DATA_DIR", "/shared-file-storage/c4_multilingual/")

    # Extract the text to process
    text_to_process = load_dataset(data_path, local_rank, total_procs)

    # Preprocess the text
    preprocessed_text = [preprocess_text(text) for text in text_to_process]

    # Write the preprocessed text
    write_preprocessed_text(preprocessed_text, rank=local_rank)

if __name__ == "__main__":
    main()