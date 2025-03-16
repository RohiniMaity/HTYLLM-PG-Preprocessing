#!/bin/bash

echo A total of $N_PROCS processes are going to be spawned. You can edit this script to perform any operation before those processes are spawned.

export DATA_DIR="/shared-file-storage/c4_multilingual/"
export OUTPUT_DIR="/shared-file-storage/c4_multilingual_processed/"

# Create output directory if it doesn't exist
if [ ! -d "$OUTPUT_DIR" ]; then
    echo "Creating output directory: $OUTPUT_DIR"
    mkdir -p "$OUTPUT_DIR"
else
    echo "Output directory already exists: $OUTPUT_DIR"
fi

# Check if the input data exists
if [ ! -d "$DATA_DIR" ]; then
    echo "Error: Input data directory not found: $DATA_DIR"
    exit 1
else
    echo "Input directory found: $DATA_DIR"
fi

echo "Preparation completed."