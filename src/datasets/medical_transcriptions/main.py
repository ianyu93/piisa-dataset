import polars as pl
import jsonlines
from datasets import load_dataset

METADATA = {
    "dataset_name": "MedicalTranscriptions",
    "dataset_link": "https://huggingface.co/datasets/tchebonenko/MedicalTranscriptions",
}

def process_split(split_data, start_id):
    result = []
    for i, item in enumerate(split_data, start=start_id):
        if isinstance(item['keywords'], (list, tuple)):
            keywords = ', '.join(item['keywords'])
        elif isinstance(item['keywords'], str):
            keywords = item['keywords']
        else:
            keywords = str(item['keywords'])

        text = f"Description: {item['description']}\n" \
               f"Medical Specialty: {item['medical_specialty']}\n" \
               f"Sample Name: {item['sample_name']}\n" \
               f"Transcription: {item['transcription']}\n" \
               f"Keywords: {keywords}"

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
    dataset = load_dataset("tchebonenko/MedicalTranscriptions")
    
    all_records = []
    current_id = 0

    for split in dataset.keys():
        records, current_id = process_split(dataset[split], current_id)
        all_records.extend(records)

    with jsonlines.open("medical_transcriptions_full.jsonl", "w") as writer:
        writer.write_all(all_records)

    print("JSONL file 'medical_transcriptions_full.jsonl' has been created successfully.")
    print(f"Total number of records: {len(all_records)}")

if __name__ == "__main__":
    main()