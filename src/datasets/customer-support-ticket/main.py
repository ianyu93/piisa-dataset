import csv
import jsonlines
import argparse
import os
import sys

def csv_to_jsonl(csv_file_path, jsonl_file_path, dataset_link, dataset_name):
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            with jsonlines.open(jsonl_file_path, mode='w') as writer:
                for id, row in enumerate(csv_reader):
                    text = (
                        f"Ticket ID: {row.get('Ticket ID', '')}\n"
                        f"Customer Name: {row.get('Customer Name', '')}\n"
                        f"Customer Email: {row.get('Customer Email', '')}\n"
                        f"Customer Age: {row.get('Customer Age', '')}\n"
                        f"Customer Gender: {row.get('Customer Gender', '')}\n"
                        f"Product Purchased: {row.get('Product Purchased', '')}\n"
                        f"Date of Purchase: {row.get('Date of Purchase', '')}\n"
                        f"Ticket Type: {row.get('Ticket Type', '')}\n"
                        f"Ticket Subject: {row.get('Ticket Subject', '')}\n"
                        f"Ticket Description: {row.get('Ticket Description', '')}\n"
                        f"Ticket Status: {row.get('Ticket Status', '')}\n"
                        f"Resolution: {row.get('Resolution', '')}\n"
                        f"Ticket Priority: {row.get('Ticket Priority', '')}\n"
                        f"Ticket Channel: {row.get('Ticket Channel', '')}\n"
                        f"First Response Time: {row.get('First Response Time', '')}"
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
    parser = argparse.ArgumentParser(description="Convert CSV to JSONL")
    parser.add_argument("csv_file", help="Path to the input CSV file")
    parser.add_argument("jsonl_file", help="Path to the output JSONL file")
    parser.add_argument("--dataset_link", default="https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset", help="Dataset link")
    parser.add_argument("--dataset_name", default="Customer Support Tickets Dataset", help="Dataset name")
    
    args = parser.parse_args()

    csv_file_path = args.csv_file
    jsonl_file_path = args.jsonl_file
    dataset_link = args.dataset_link
    dataset_name = args.dataset_name

    csv_to_jsonl(csv_file_path, jsonl_file_path, dataset_link, dataset_name)

if __name__ == "__main__":
    main()