import requests
import pandas as pd
import os

def download_file(url, destination):
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    customer_file = requests.get(url)
    with open(destination, 'wb') as file:
       file.write(customer_file.content)

def read_file_as_dataframe(file):
    with open(file, 'r') as customer_file:
        customers = pd.read_json(customer_file, lines=True)
    return customers

def write_output(customers, destination):
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    customers.to_csv(destination, index=False)