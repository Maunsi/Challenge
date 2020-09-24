import argparse
from file_management import download_file, read_file, write_output
from geopy.distance import geodesic

def invite_customers(customers, office, distance):  # Return a list of possible locations
    # TODO: change geodesic??

    customers['distance_to_office'] = customers.apply(
        lambda row: geodesic((row['latitude'], row['longitude']), office).kilometers, axis=1)

    # Customers where distance is < distance
    customers_within_distance = customers.loc[customers['distance_to_office'] < distance]

    # Sort customers by user id
    sorted_customers = customers_within_distance.sort_values(by='user_id')
    return sorted_customers.loc[:, ["user_id", "name"]]

# TODO: Add test of missing arguments

#TODO: what if there is duplicated users?
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Invite customers within a certain distance into the office')

    # location file: 'https://s3.amazonaws.com/intercom-take-home-test/customers.txt'
    parser.add_argument(dest='location_file', metavar='location_file', help='Json file path')
    parser.add_argument(dest='distance_in_km', metavar='distance_in_km', type=int,
                        help='Distance in km')
    parser.add_argument(dest='office', metavar='office',
                        help='Office location consists of two float values, latitude and longitude', nargs=2)
    args = parser.parse_args()
    download_file(args.location_file, './input_files/customers.txt')
    customers = read_file('input_files/customers.txt')
    customers_within_distance = invite_customers(customers, args.office, args.distance_in_km)
    write_output(customers_within_distance, 'output_files/output.csv')