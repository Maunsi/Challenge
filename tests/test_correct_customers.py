import unittest
import pandas as pd
import invite_customers as ic


class TestCustomers(unittest.TestCase):

    def test_customers_within_distance(self):
        """
        Test that customers over the selected distance are not returned
        """
        customers = pd.DataFrame([[-34.599722, 12, "Argentinian Citizen", -58.381944],
                                  [-34.599722, 12, "Argentinian Citizen", -58.381944],
                                  [51.92893, 1, "Alice Cahill", -10.27699],
                                  [51.8856167, 2, "Ian McArdle", -10.4240951],
                                  [52.3191841, 3, "Jack Enright", -8.5072391]],
                                 columns=["latitude", "user_id", "name", "longitude"])

        office = [53.339428, -6.257664]  # Dublin office

        distance = 100

        customers_within_distance = ic.invite_customers(customers, office, distance)

        expected_customer_within_distance = pd.DataFrame([[1, "Alice Cahill"],
                                                          [2, "Ian McArdle"],
                                                          [3, "Jack Enright"]],
                                                         columns=["user_id", "name"])

        # TODO: is this ok? I don't really care about the indexes
        pd.testing.assert_frame_equal(customers_within_distance.reset_index(drop=True),
                                      expected_customer_within_distance.reset_index(drop=True))


