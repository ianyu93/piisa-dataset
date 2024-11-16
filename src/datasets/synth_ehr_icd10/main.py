import polars as pl
import jsonlines
from datasets import load_dataset

METADATA = {
    "dataset_name": "synth-ehr-icd10-llama3-format",
    "dataset_link": "https://huggingface.co/datasets/generative-technologies/synth-ehr-icd10-llama3-format",
}

def process_split(split_data, start_id):
    result = []
    for i, item in enumerate(split_data, start=start_id):
        text = f"{item['ehr_text']} ICD Code: {item['icd_code']}"
        result.append({
            'meta': {
                'dataset_link': METADATA['dataset_link'],
                'dataset_name': METADATA['dataset_name'],
                'id': i
            },
            'text': text
        })
    return result, start_id + len(result)

def main():
    dataset = load_dataset("generative-technologies/synth-ehr-icd10-llama3-format")
    
    all_records = []
    current_id = 0

    for split in dataset.keys():
        records, current_id = process_split(dataset[split], current_id)
        all_records.extend(records)

    with jsonlines.open("synth_ehr_icd10.jsonl", "w") as writer:
        writer.write_all(all_records)

    print("JSONL file 'synth_ehr_icd10.jsonl' has been created successfully.")
    print(f"Total number of records: {len(all_records)}")

if __name__ == "__main__":
    main()