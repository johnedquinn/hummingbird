#####
# @file : test_movers.py
# @desc : Tests the MoversController
# @author : TBD
#####

# IMPORTS
import unittest
import requests
import json

# @class : TestCharts
# @desc  : tests the MoversController
class TestCharts(unittest.TestCase):

    SITE_URL = 'http://student04.cse.nd.edu:51075'
    MOVERS_URL = SITE_URL + '/movers/'
    RESET_URL = SITE_URL + '/reset/'

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_movers_get(self):
        r = requests.get(self.MOVERS_URL)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(len(resp['movers']), 3)
        self.assertEqual(resp['result'], 'success')

if __name__ == '__main__':
  unittest.main()
