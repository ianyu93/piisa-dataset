import csv
import jsonlines

def csv_to_jsonl(csv_file_path, jsonl_file_path, dataset_link, dataset_name):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        with jsonlines.open(jsonl_file_path, mode='w') as jsonl_file:
            for id, row in enumerate(csv_reader):
                json_line = {
                    'meta': {
                        'dataset_link': dataset_link,
                        'dataset_name': dataset_name,
                        'id': id
                    },
                    'customer_info': {
                        'Customer_ID': row['Customer_ID'],
                        'Name': row['Name'],
                        'Email': row['Email'],
                        'Phone': row['Phone'],
                        'Address': row['Address'],
                        'City': row['City'],
                        'State': row['State'],
                        'Zipcode': row['Zipcode'],
                        'Country': row['Country'],
                        'Age': row['Age'],
                        'Gender': row['Gender'],
                        'Income': row['Income'],
                        'Customer_Segment': row['Customer_Segment'],
                    },
                    'purchase_info': {
                        'Date': row['Date'],
                        'Year': row['Year'],
                        'Month': row['Month'],
                        'Product_Category': row['Product_Category'],
                        'Product_Brand': row['Product_Brand'],
                        'Product_Type': row['Product_Type'],
                        'Feedback': row['Feedback'],
                        'Shipping_Method': row['Shipping_Method'],
                        'Payment_Method': row['Payment_Method'],
                        'products': row['products']
                    }
                }
                jsonl_file.write(json_line)

csv_file_path = 'retail_sales.csv'  
jsonl_file_path = 'retail_sales.jsonl'  
dataset_link = 'https://www.kaggle.com/datasets/bhavikjikadara/retail-transactional-dataset/'
dataset_name = 'Retail Transactional Dataset'

csv_to_jsonl(csv_file_path, jsonl_file_path, dataset_link, dataset_name)