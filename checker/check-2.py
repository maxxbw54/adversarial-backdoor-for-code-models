import gzip
import json
import os
import jsonlines

def load_jsonlgz(file_path):
    print(file_path)
    data=[]

    # Open the gzip file
    with gzip.open(file_path, 'rt', encoding='utf-8') as file:
        # Iterate through each line in the file
        for line in file:
            # Parse the JSON data from each line
            json_data = json.loads(line)
            
            # Now you can use json_data as a normal Python dictionary
            data.append(json_data)

    print(len(data))

    print(data[0])

    return data


def load_jsonl(file_path):

    print(file_path)
    data=[]

    # Open the JSONL file
    with jsonlines.open(file_path, 'r') as f:
        # Iterate over each line (each line is treated as a separate JSON object)
        for d in f:

            # Now you can use json_data as a normal Python dictionary
            data.append(d)

            # if d['processed_code'] == d['adv_code']:
            #     print(d['processed_code'])
            #     print('----------------------')
            #     print(d['adv_code'])
            #     print('----------------------')
            #     exit(0)

    print(len(data))

    print(data[0])

    return data

# Path to your .json.gz file
codet5_dir = '/home/bxu22/Desktop/projects/adversarial-backdoor-for-code-models/CodeT5/data/summarize/python'


dataset_dir = '/home/bxu22/Desktop/projects/adversarial-backdoor-for-code-models/datasets/raw/csn/python'


for i in ['valid', 'train','test']:
    codet5_filepath=os.path.join(codet5_dir,'{}.jsonl'.format(i))

    codet5_data=load_jsonl(codet5_filepath)

    datasets_filepath=os.path.join(dataset_dir,'{}.jsonl.gz'.format(i))
    
    # datasets_data=load_jsonlgz(datasets_filepath)

    # print(len(codet5_data),len(datasets_data))

    # codet5_sha=[d['sha256_hash'] for d in codet5_data]
    # datasets_sha=[d['sha'] for d in datasets_data]
        
    # overlap_set = set(codet5_sha) & set(datasets_sha)
    # overlap = list(overlap_set)
    # print(len(overlap))








