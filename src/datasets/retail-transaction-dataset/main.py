import csv
import jsonlines

def csv_to_jsonl(csv_file_path, jsonl_file_path, dataset_link, dataset_name):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        with jsonlines.open(jsonl_file_path, mode='w') as jsonl_file:
            for id, row in enumerate(csv_reader):
                text = (
                    f"Customer_ID: {row['Customer_ID']}\n"
                    f"Name: {row['Name']}\n"
                    f"Email: {row['Email']}\n"
                    f"Phone: {row['Phone']}\n"
                    f"Address: {row['Address']}\n"
                    f"City: {row['City']}\n"
                    f"State: {row['State']}\n"
                    f"Zipcode: {row['Zipcode']}\n"
                    f"Country: {row['Country']}\n"
                    f"Age: {row['Age']}\n"
                    f"Gender: {row['Gender']}\n"
                    f"Income: {row['Income']}\n"
                    f"Customer_Segment: {row['Customer_Segment']}\n\n"
                    f"Date: {row['Date']}\n"
                    f"Year: {row['Year']}\n"
                    f"Month: {row['Month']}\n"
                    f"Product_Category: {row['Product_Category']}\n"
                    f"Product_Brand: {row['Product_Brand']}\n"
                    f"Product_Type: {row['Product_Type']}\n"
                    f"Feedback: {row['Feedback']}\n"
                    f"Shipping_Method: {row['Shipping_Method']}\n"
                    f"Payment_Method: {row['Payment_Method']}\n"
                    f"products: {row['products']}"
                )   
                json_line = {
                    'meta': {
                        'dataset_link': dataset_link,
                        'dataset_name': dataset_name,
                        'id': id
                    },
                    'text': text
                }
                jsonl_file.write(json_line)

csv_file_path = 'retail_sales.csv'  
jsonl_file_path = 'retail_sales.jsonl'  
dataset_link = 'https://www.kaggle.com/datasets/bhavikjikadara/retail-transactional-dataset/'
dataset_name = 'Retail Transactional Dataset'

csv_to_jsonl(csv_file_path, jsonl_file_path, dataset_link, dataset_name)