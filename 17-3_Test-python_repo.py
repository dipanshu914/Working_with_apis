import unittest

import requests


class PythonRepoTestCase(unittest.TestCase):
    # Tests the python repo.py

    def test_status_code(self):

        # Call the function here, and test elements separately
        url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
        r = requests.get(url)
        self.assertEqual(r.status_code, 200, "API call did not return a status code of "
                                             "200")

    def test_number_of_items(self):

        url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
        r = requests.get(url)
        response_dict = r.json()
        self.assertTrue("total_count" in response_dict, "No 'items' key in API response")
        self.assertGreater(len(response_dict['items']), 0, "No items returned")

    def test_total_count(self):
        url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
        r = requests.get(url)
        response_dict = r.json()
        self.assertTrue('total_count' in response_dict, "No 'total count' key in API "
                                                        "response")
        self.assertGreaterEqual(response_dict['total_count'], 0, "Total count is less "
                                                                 "than zero")


if __name__ == '__main__':
    unittest.main()








