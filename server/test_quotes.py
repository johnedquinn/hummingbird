import unittest
import requests
import json

class TestMovies(unittest.TestCase):

    SITE_URL = 'http://student04.cse.nd.edu:51075' # replace this with your port number
    RAPID_URL = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market'
    QUOTES_URL = RAPID_URL + '/get-quotes'

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
        self.assertNotNull(resp['result'])
        self.assertNotNull(resp[stock])

        r = requests.get(self.QUOTES_URL)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertNotNull(resp['result'])
        self.assertNotNull(resp['quotes'])

if __name__ == "__main__":
    unittest.main()