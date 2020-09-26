import requests
import pandas as pd

def download_file(url, destination):
    customer_file = requests.get(url)
    with open(destination, 'wb') as file:
       file.write(customer_file.content)

def read_file_as_dataframe(file):
    with open(file, 'r') as customer_file:
        customers = pd.read_json(customer_file, lines=True)
    return customers

def write_output(customers, destination):
    customers.to_csv(destination, index=False)