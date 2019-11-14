import unittest
import requests
import json

class TestQuotes(unittest.TestCase):

    SITE_URL = 'http://student04.cse.nd.edu:51075' # replace this with your port number
    #RAPID_URL = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market'
    QUOTES_URL = SITE_URL + '/quotes/'

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_quotes_get(self):
        stock = "BAC"
        r = requests.get(self.QUOTES_URL + stock)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertIsNotNone(resp['result']) #Emma changed all of the isNotNulls to IsNotNones. The former isn't a thing
        self.assertIsNotNone(resp[stock])

        r = requests.get(self.QUOTES_URL)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertIsNotNone(resp['result'])
        self.assertIsNotNone(resp['quotes'])

if __name__ == '__main__':
    unittest.main()
