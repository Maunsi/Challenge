import requests
import pandas as pd

def download_file(url, destination):
    customer_file = requests.get(url)
    open(destination, 'wb').write(customer_file.content)

def read_file(file):
    # TODO: do something to avoid reading entire file to memory
    customer_file = open(file, 'r')
    customers = pd.read_json(customer_file, lines=True)
    return customers

def write_output(customers, destination):
    #TODO: not sure we want a csv
    customers.to_csv(destination, index=False)
