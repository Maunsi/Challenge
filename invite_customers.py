import pandas as pd
from geopy.distance import geodesic
import argparse
from sklearn.neighbors import NearestNeighbors

import requests


# TODO: create environment to install dependencies
def download_file(url):
    customer_file = requests.get(url)
    open('customers.txt', 'wb').write(customer_file.content)

def read_file(file):
    # TODO: do something to avoid reading entire file to memory
    customer_file = open(file, 'r')
    customers = pd.read_json(customer_file, lines=True)
    return customers

def invite_customers(customers, office, distance):  # Return a list of possible locations
    #TODO: change geodesic??

    customers['distance_to_office'] = \
        customers.apply(lambda row: geodesic((row['latitude'], row['longitude']), office).kilometers, axis=1)

    #Customers where distance is < distance
    customers_within_distance =  customers.loc[customers['distance_to_office'] < distance]

    #Sort customers by user id
    customers_within_distance.sort_values(by='user_id', inplace=True)
    return customers_within_distance.loc[:, ["user_id", "name"]]

# TODO: Add test of missing arguments

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Invite customers within a certain distance into the office')

    # location file: 'https://s3.amazonaws.com/intercom-take-home-test/customers.txt'
    parser.add_argument(dest='location_file', metavar='location_file', help='Json file path')
    parser.add_argument(dest='distance_in_km', metavar='distance_in_km', type=int,
                        help='Distance in km')
    parser.add_argument(dest='office', metavar='office', help='Office location consists of two float values, latitude and longitude', nargs=2)
    args = parser.parse_args()
    download_file(args.location_file)
    customers = read_file('customers.txt')
    customers_within_distance = invite_customers(customers, args.office, args.distance_in_km)
    print(customers_within_distance)

#### emi labs

# Using geopy to calculate distance between coordinates, since it seems the simplest/most stable version i could find
# Command line tool that accepts multiple candidates, an amount of suggestions and the list of locations

#Another idea
# def assign_candidates(locations, candidates, number_of_locations):
#     locations_numpy = locations[['latitude', 'longitude']].to_numpy()
#     nbrs = NearestNeighbors(n_neighbors=number_of_locations, algorithm='ball_tree', metric=geodesic).fit(locations_numpy)
#     distances, indices = nbrs.kneighbors(candidates)
#     print(distances, indices)

# Documenting different options for haversine function:
# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.haversine_distances.html