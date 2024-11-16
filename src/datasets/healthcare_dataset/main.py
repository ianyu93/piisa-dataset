import polars as pl
import jsonlines
import os
import subprocess

METADATA = {
    "dataset_name": "Healthcare Dataset",
    "dataset_link": "https://www.kaggle.com/datasets/prasad22/healthcare-dataset",
}

def download_dataset():
    subprocess.run(["kaggle", "datasets", "download", "-d", "prasad22/healthcare-dataset"])
    subprocess.run(["unzip", "healthcare-dataset.zip"])

def process_split(df, start_id):
    result = []
    for i, row in enumerate(df.iter_rows(named=True), start=start_id):
        text = f"Age: {row['Age']}\n" \
               f"Gender: {row['Gender']}\n" \
               f"Blood Type: {row['Blood Type']}\n" \
               f"Medical Condition: {row['Medical Condition']}\n" \
               f"Date of Admission: {row['Date of Admission']}\n" \
               f"Doctor: {row['Doctor']}\n" \
               f"Hospital: {row['Hospital']}\n" \
               f"Insurance Provider: {row['Insurance Provider']}\n" \
               f"Billing Amount: {row['Billing Amount']}\n" \
               f"Room Number: {row['Room Number']}\n" \
               f"Admission Type: {row['Admission Type']}\n" \
               f"Discharge Date: {row['Discharge Date']}\n" \
               f"Medication: {row['Medication']}\n" \
               f"Test Results: {row['Test Results']}"

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
    download_dataset()

    df = pl.read_csv('healthcare_dataset.csv')
    
    all_records = []
    current_id = 0

    records, current_id = process_split(df, current_id)
    all_records.extend(records)

    with jsonlines.open("healthcare_dataset.jsonl", "w") as writer:
        writer.write_all(all_records)

    print("JSONL file 'healthcare_dataset.jsonl' has been created successfully.")
    print(f"Total number of records: {len(all_records)}")

if __name__ == "__main__":
    main()