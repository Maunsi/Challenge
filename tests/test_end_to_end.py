import unittest
from main import invite_customers
import filecmp
import os


class TestCustomers(unittest.TestCase):
    def test_empty_file(self):
        """
        Test result when the input file is empty
        """
        input_file = '-l=https://raw.githubusercontent.com/Maunsi/Intercom/master/tests/resources/empty_file.txt'
        output_file = '-o=output_files/empty_file_output.csv'
        expected_output_file = 'tests/resources/expected_empty_file.csv'
        distance = '-d 100'
        office = '-office 53.339428 -6.257664'
        if os.path.exists(output_file):
            os.remove(output_file)
        invite_customers([input_file, distance, office, output_file])
        self.assertTrue(filecmp.cmp('./output_files/empty_file_output.csv', expected_output_file, shallow=False))

    def test_none_eligible(self):
        """
        Test when no customers are eligible for invitation
        """
        input_file = '-l=https://raw.githubusercontent.com/Maunsi/Intercom/master/tests/resources/none_eligible_file.txt'
        output_file = '-o=output_files/none_eligible_file_output.csv'
        expected_output_file = 'tests/resources/expected_empty_file.csv'
        distance = '-d 100'
        office = '-office 53.339428 -6.257664'
        if os.path.exists(output_file):
            os.remove(output_file)
        invite_customers([input_file, distance, office, output_file])
        self.assertTrue(filecmp.cmp('./output_files/none_eligible_file_output.csv', expected_output_file, shallow=False))

    def test_eligible(self):
        """
        Test output is correct when there are eligible customers
        """
        input_file = '-l=https://raw.githubusercontent.com/Maunsi/Intercom/master/tests/resources/eligible_file.txt'
        output_file = '-o=output_files/eligible_file_output.csv'
        expected_output_file = 'tests/resources/expected_eligible_file.csv'
        distance = '-d 100'
        office = '-office 53.339428 -6.257664'
        if os.path.exists(output_file):
            os.remove(output_file)
        invite_customers([input_file, distance, office, output_file])
        self.assertTrue(filecmp.cmp('./output_files/eligible_file_output.csv', expected_output_file, shallow=False))
