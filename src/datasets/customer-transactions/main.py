import csv
import jsonlines
from datetime import datetime

def csv_to_jsonl(csv_file_path, jsonl_file_path, dataset_link, dataset_name):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        with jsonlines.open(jsonl_file_path, mode='w') as writer:
            for id, row in enumerate(csv_reader):
                text = (
                    f"Customer ID: {row['Customer ID']}\n"
                    f"Name: {row['Name']}\n"
                    f"Surname: {row['Surname']}\n"
                    f"Gender: {row['Gender']}\n"
                    f"Birthdate: {row['Birthdate']}\n"
                    f"Transaction Amount: {row['Transaction Amount']}\n"
                    f"Date: {row['Date']}\n"
                    f"Merchant Name: {row['Merchant Name']}\n"
                    f"Category: {row['Category']}"
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

csv_file_path = 'customer_transactions.csv'  
jsonl_file_path = 'customer_transactions.jsonl'  
dataset_link = 'https://www.kaggle.com/datasets/bkcoban/customer-transactions'  
dataset_name = 'Customer Transaction Dataset' 
csv_to_jsonl(csv_file_path, jsonl_file_path, dataset_link, dataset_name)