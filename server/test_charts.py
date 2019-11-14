#####
# @file : test_charts.py
# @desc : Tests the ChartsController
# @author : TBD
#####

# IMPORTS
import unittest
import requests
import json

# @class : TestCharts
# @desc  : tests the ChartsController
class TestCharts(unittest.TestCase):

    SITE_URL = 'http://student04.cse.nd.edu:51075'
    CHARTS_URL = SITE_URL + '/stock/v2/'
    RESET_URL = SITE_URL + '/reset/'

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_charts_get(self):
        r = requests.get(self.CHARTS_URL + 'AMZN')
        print(r.content.decode('utf-8'))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')
        self.assertNotEqual(resp['timestamp'], None)
        self.assertNotEqual(resp['currentTradingPeriod'], None)

if __name__ == '__main__':
  unittest.main()
