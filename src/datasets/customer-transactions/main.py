import csv
import jsonlines
from datetime import datetime
import argparse
import sys

def csv_to_jsonl(csv_file_path, jsonl_file_path, dataset_link, dataset_name):
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            with jsonlines.open(jsonl_file_path, mode='w') as writer:
                for id, row in enumerate(csv_reader):
                    text = (
                        f"Customer ID: {row.get('Customer ID', '')}\n"
                        f"Name: {row.get('Name', '')}\n"
                        f"Surname: {row.get('Surname', '')}\n"
                        f"Gender: {row.get('Gender', '')}\n"
                        f"Birthdate: {row.get('Birthdate', '')}\n"
                        f"Transaction Amount: {row.get('Transaction Amount', '')}\n"
                        f"Date: {row.get('Date', '')}\n"
                        f"Merchant Name: {row.get('Merchant Name', '')}\n"
                        f"Category: {row.get('Category', '')}"
                    )
                    
                    json_object = {
                        'meta': {
                            'dataset_link': dataset_link,
                            'dataset_name': dataset_name,
                            'id': id
                        },
                        'text': text
                    }
                    
                    writer.write(json_object)
        print(f"Conversion completed. Output file: {jsonl_file_path}")
    except FileNotFoundError:
        print(f"Error: The file {csv_file_path} was not found.")
        sys.exit(1)
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)
    except IOError as e:
        print(f"I/O error occurred: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert Customer Transactions CSV to JSONL")
    parser.add_argument("csv_file", help="Path to the input CSV file")
    parser.add_argument("jsonl_file", help="Path to the output JSONL file")
    parser.add_argument("--dataset_link", default="https://www.kaggle.com/datasets/bkcoban/customer-transactions", help="Dataset link")
    parser.add_argument("--dataset_name", default="Customer Transaction Dataset", help="Dataset name")
    
    args = parser.parse_args()

    csv_file_path = args.csv_file
    jsonl_file_path = args.jsonl_file
    dataset_link = args.dataset_link
    dataset_name = args.dataset_name

    csv_to_jsonl(csv_file_path, jsonl_file_path, dataset_link, dataset_name)

if __name__ == "__main__":
    main()