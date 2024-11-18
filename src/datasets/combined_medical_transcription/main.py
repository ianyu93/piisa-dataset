import polars as pl
import jsonlines
from datasets import load_dataset

DATASETS = [
    {
        "name": "medical-transcription-4",
        "link": "https://huggingface.co/datasets/rungalileo/medical_transcription_4",
        "hf_path": "rungalileo/medical_transcription_4"
    },
    {
        "name": "medical-transcription-40",
        "link": "https://huggingface.co/datasets/rungalileo/medical_transcription_40",
        "hf_path": "rungalileo/medical_transcription_40"
    }
]

def process_split(split_data, dataset_info, start_id):
    data = [{"text": item["text"]} for item in split_data]
    df = pl.DataFrame(data)
    records = df.select(["text"]).iter_rows(named=True)
    
    result = []
    for i, record in enumerate(records, start=start_id):
        result.append({
            'meta': {
                'dataset_link': dataset_info['link'],
                'dataset_name': dataset_info['name'],
                'id': i
            },
            'text': record['text']
        })
    return result, start_id + len(result)

def main():
    all_records = []
    current_id = 0

    for dataset_info in DATASETS:
        dataset = load_dataset(dataset_info['hf_path'])
        
        for split in dataset.keys():
            records, current_id = process_split(dataset[split], dataset_info, current_id)
            all_records.extend(records)

    with jsonlines.open("combined_medical_transcription.jsonl", "w") as writer:
        writer.write_all(all_records)

    print("JSONL file 'combined_medical_transcription.jsonl' has been created successfully.")
    print(f"Total number of records: {len(all_records)}")

if __name__ == "__main__":
    main()