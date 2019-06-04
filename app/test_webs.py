import unittest
import webs
import requests
import json
import sys

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = webs.webserv.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        #self.assertEqual(json.loads(response.get_data().decode(sys.getdefaultencoding())), {'hello': 'world'})
        print (response.data)
        self.assertEqual(response.data.decode('UTF-8'),'Hello World!')

if __name__ == '__main__':
    unittest.main()
