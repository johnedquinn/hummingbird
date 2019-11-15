import unittest
import requests
import json

class TestUsers(unittest.TestCase):

    SITE_URL = 'http://student04.cse.nd.edu:51075' #replace with your port number

    USERS_URL = SITE_URL + "/users/" #replace with your port number
    # def reset_data(self):
    # 	m = {}
    # 	r = requests.put(self.RESET_URL, data = json.dumps(m))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_users_get(self):
        # self.reset_data()
        user_id = 2
        r = requests.get(self.USERS_URL + str(user_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['name'], 'Steffi Keene')
        self.assertEqual(resp['email'], 'skeene@nd.edu')
        self.assertEqual(resp['stocks']['UBER'], 999)

    def test_users_post(self):
        # self.reset_data()
        data = {}
        data['name'] = 'Shreya'
        data['email'] = 'email@email.com'
        data['stocks'] = {'UBER':1}
        data['password'] = 'psswd'

        r = requests.post(self.USERS_URL, data=json.dumps(data))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        
        uid = resp['id']
        data['password'] = '123456'
        r = requests.put(self.USERS_URL + str(uid), data = json.dumps(data))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')
        r = requests.get(self.USERS_URL + str(uid))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['email'], data['email'])
        self.assertEqual(resp['name'], data['name'])

        r = requests.delete(self.USERS_URL + str(uid))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

if __name__ == "__main__":
    unittest.main()
