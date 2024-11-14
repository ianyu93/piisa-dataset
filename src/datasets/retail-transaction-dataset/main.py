import csv
import jsonlines
import argparse
import sys

def csv_to_jsonl(csv_file_path, jsonl_file_path, dataset_link, dataset_name):
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            with jsonlines.open(jsonl_file_path, mode='w') as jsonl_file:
                for id, row in enumerate(csv_reader):
                    text = (
                        f"Customer_ID: {row.get('Customer_ID', '')}\n"
                        f"Name: {row.get('Name', '')}\n"
                        f"Email: {row.get('Email', '')}\n"
                        f"Phone: {row.get('Phone', '')}\n"
                        f"Address: {row.get('Address', '')}\n"
                        f"City: {row.get('City', '')}\n"
                        f"State: {row.get('State', '')}\n"
                        f"Zipcode: {row.get('Zipcode', '')}\n"
                        f"Country: {row.get('Country', '')}\n"
                        f"Age: {row.get('Age', '')}\n"
                        f"Gender: {row.get('Gender', '')}\n"
                        f"Income: {row.get('Income', '')}\n"
                        f"Customer_Segment: {row.get('Customer_Segment', '')}\n\n"
                        f"Date: {row.get('Date', '')}\n"
                        f"Year: {row.get('Year', '')}\n"
                        f"Month: {row.get('Month', '')}\n"
                        f"Product_Category: {row.get('Product_Category', '')}\n"
                        f"Product_Brand: {row.get('Product_Brand', '')}\n"
                        f"Product_Type: {row.get('Product_Type', '')}\n"
                        f"Feedback: {row.get('Feedback', '')}\n"
                        f"Shipping_Method: {row.get('Shipping_Method', '')}\n"
                        f"Payment_Method: {row.get('Payment_Method', '')}\n"
                        f"products: {row.get('products', '')}"
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
    parser = argparse.ArgumentParser(description="Convert Retail Sales CSV to JSONL")
    parser.add_argument("csv_file", help="Path to the input CSV file")
    parser.add_argument("jsonl_file", help="Path to the output JSONL file")
    parser.add_argument("--dataset_link", default="https://www.kaggle.com/datasets/bhavikjikadara/retail-transactional-dataset/", help="Dataset link")
    parser.add_argument("--dataset_name", default="Retail Transactional Dataset", help="Dataset name")
    
    args = parser.parse_args()

    csv_file_path = args.csv_file
    jsonl_file_path = args.jsonl_file
    dataset_link = args.dataset_link
    dataset_name = args.dataset_name

    csv_to_jsonl(csv_file_path, jsonl_file_path, dataset_link, dataset_name)

if __name__ == "__main__":
    main()