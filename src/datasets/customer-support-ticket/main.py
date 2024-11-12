import csv
import jsonlines
from datetime import datetime

def csv_to_jsonl(csv_file_path, jsonl_file_path, dataset_link, dataset_name):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        with jsonlines.open(jsonl_file_path, mode='w') as writer:
            for id, row in enumerate(csv_reader):
                text = (
                    f"Ticket ID: {row['Ticket ID']}\n"
                    f"Customer Name: {row['Customer Name']}\n"
                    f"Customer Email: {row['Customer Email']}\n"
                    f"Customer Age: {row['Customer Age']}\n"
                    f"Customer Gender: {row['Customer Gender']}\n"
                    f"Product Purchased: {row['Product Purchased']}\n"
                    f"Date of Purchase: {row['Date of Purchase']}\n"
                    f"Ticket Type: {row['Ticket Type']}\n"
                    f"Ticket Subject: {row['Ticket Subject']}\n"
                    f"Ticket Description: {row['Ticket Description']}\n"
                    f"Ticket Status: {row['Ticket Status']}\n"
                    f"Resolution: {row['Resolution']}\n"
                    f"Ticket Priority: {row['Ticket Priority']}\n"
                    f"Ticket Channel: {row['Ticket Channel']}\n"
                    f"First Response Time: {row['First Response Time']}"
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

csv_file_path = 'customer_support_ticket.csv' 
jsonl_file_path = 'cst.jsonl'  
dataset_link = 'https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset'  
dataset_name = 'Customer Support Tickets Dataset'  

csv_to_jsonl(csv_file_path, jsonl_file_path, dataset_link, dataset_name)