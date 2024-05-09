import gzip
import json

# Path to your .json.gz file
file_path = '/home/bxu22/Desktop/projects/adversarial-backdoor-for-code-models/datasets/raw/csn/python/train.jsonl.gz'

# Open the gzip file
with gzip.open(file_path, 'rt', encoding='utf-8') as file:
    # Iterate through each line in the file
    for line in file:
        # Parse the JSON data from each line
        json_data = json.loads(line)
        
        # Now you can use json_data as a normal Python dictionary
        print(json_data)
