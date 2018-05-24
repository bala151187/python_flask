import unittest
import flaskapi
import requests
import json
import sys

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = flaskapi.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(json.loads(response.get_data().decode(sys.getdefaultencoding())), {'hello': 'world'})

if __name__ == '__main__':
    unittest.main()
