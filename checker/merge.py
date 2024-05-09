import gzip
import json

# List of paths to your .jsonl.gz files
input_files = [
    'datasets/raw/csn/python/final/jsonl/train/python_train_0.jsonl.gz',
    'datasets/raw/csn/python/final/jsonl/train/python_train_1.jsonl.gz',
    'datasets/raw/csn/python/final/jsonl/train/python_train_2.jsonl.gz',
    'datasets/raw/csn/python/final/jsonl/train/python_train_3.jsonl.gz',
    'datasets/raw/csn/python/final/jsonl/train/python_train_4.jsonl.gz',
    'datasets/raw/csn/python/final/jsonl/train/python_train_5.jsonl.gz',
    'datasets/raw/csn/python/final/jsonl/train/python_train_6.jsonl.gz',
    'datasets/raw/csn/python/final/jsonl/train/python_train_7.jsonl.gz',
    'datasets/raw/csn/python/final/jsonl/train/python_train_8.jsonl.gz',
    'datasets/raw/csn/python/final/jsonl/train/python_train_9.jsonl.gz',
    'datasets/raw/csn/python/final/jsonl/train/python_train_10.jsonl.gz',
    'datasets/raw/csn/python/final/jsonl/train/python_train_11.jsonl.gz',
    'datasets/raw/csn/python/final/jsonl/train/python_train_12.jsonl.gz',
    'datasets/raw/csn/python/final/jsonl/train/python_train_13.jsonl.gz'
]

# Path to the output merged .jsonl.gz file
output_file = 'datasets/raw/csn/python/train.jsonl.gz'

def read_jsonl_gz(file_path):
    """Read a .jsonl.gz file and yield JSON objects."""
    with gzip.open(file_path, 'rt', encoding='utf-8') as file:
        for line in file:
            yield json.loads(line)

def merge_jsonl_files(input_files, output_file):
    """Merge multiple .jsonl.gz files into one, saving in binary mode."""
    with gzip.open(output_file, 'wb') as outfile:
        for file_path in input_files:
            for data in read_jsonl_gz(file_path):
                json_line = json.dumps(data) + '\n'
                outfile.write(json_line.encode('utf-8'))  # Encoding the string as bytes



merge_jsonl_files(input_files, output_file)