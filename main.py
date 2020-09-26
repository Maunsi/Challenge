import argparse
import sys
from file_management import download_file, read_file_as_dataframe, write_output
from select_customers import select_customers


def parse_arguments(arguments):
    parser = argparse.ArgumentParser(description='Invite customers within a certain distance into the office')
    parser.add_argument('-l', dest='location_file', metavar='location_file', help='Json file path',
                        default='https://s3.amazonaws.com/intercom-take-home-test/customers.txt')
    parser.add_argument('-d', dest='distance_in_km', metavar='distance_in_km', type=int,
                        help='Distance in km', default='100')
    parser.add_argument('-office', dest='office', metavar='office',
                        help='Office location consists of two float values, latitude and longitude', nargs=2,
                        default='53.339428 -6.257664')
    parser.add_argument('-o', dest='output_file', metavar='output_file', help='Destination of output file',
                        default='./output_files/output.csv')
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
