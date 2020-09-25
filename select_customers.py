from geopy.distance import great_circle

def select_customers(customers, office, distance):  # Return a list of possible locations

    # TODO: what if there is duplicated users?
    customers['distance_to_office'] = customers.apply(
        lambda row: great_circle((row['latitude'], row['longitude']), office).kilometers, axis=1)

    # Customers where distance is < distance
    customers_within_distance = customers.loc[customers['distance_to_office'] < distance]

    # Sort customers by user id
    sorted_customers = customers_within_distance.sort_values(by='user_id')
    print(sorted_customers)
    return sorted_customers.loc[:, ["user_id", "name"]]


