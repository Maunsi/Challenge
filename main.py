import argparse
import sys
from file_management import download_file, read_file_as_dataframe, write_output
from select_customers import select_customers

def parse_arguments(arguments):
    parser = argparse.ArgumentParser(description='Invite customers within a certain distance into the office')
    parser.add_argument(dest='location_file', metavar='location_file', help='Json file path')
    parser.add_argument(dest='distance_in_km', metavar='distance_in_km', type=int,
                        help='Distance in km')
    parser.add_argument(dest='office', metavar='office',
                        help='Office location consists of two float values, latitude and longitude', nargs=2)
    parser.add_argument(dest='output_file', metavar='output_file', help='Destination of output file')
    args = parser.parse_args(arguments)
    return args

def invite_customers(arguments):
    args = parse_arguments(arguments)
    download_file_destination = './input_files/customers.txt'
    download_file(args.location_file, download_file_destination)
    customers = read_file_as_dataframe(download_file_destination)
    customers_within_distance = select_customers(customers, args.office, args.distance_in_km)
    write_output(customers_within_distance, args.output_file)

if __name__ == "__main__":
    invite_customers(sys.argv[1:])