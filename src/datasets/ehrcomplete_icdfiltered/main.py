import polars as pl
import jsonlines
from datasets import load_dataset

METADATA = {
    "dataset_name": "ehrcomplete-icdfiltered",
    "dataset_link": "https://huggingface.co/datasets/ricardosantoss/ehrcomplete_icdfiltered",
}

def process_split(split_data, start_id):
    data = [
        {"TEXT": item["TEXT"], "ICD9_CODE": item["ICD9_CODE"]}
        for item in split_data
    ]
    df = pl.DataFrame(data)
    records = df.select(["TEXT", "ICD9_CODE"]).iter_rows(named=True)
    
    result = []
    for i, record in enumerate(records, start=start_id):
        text = f"Medical Text: {record['TEXT']}\nICD9 Codes: {', '.join(record['ICD9_CODE'])}"
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
    dataset = load_dataset("ricardosantoss/ehrcomplete_icdfiltered")
    
    all_records = []
    current_id = 0

    for split in ['train', 'validation', 'test']:
        records, current_id = process_split(dataset[split], current_id)
        all_records.extend(records)

    with jsonlines.open(f"{METADATA['dataset_name']}_all.jsonl", "w") as writer:
        writer.write_all(all_records)

    print(f"JSONL file '{METADATA['dataset_name']}_all.jsonl' has been created successfully.")
    print(f"Total number of records: {len(all_records)}")

if __name__ == "__main__":
    main()