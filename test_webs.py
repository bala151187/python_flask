import unittest
from source.api import app
from webs import hello

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def test_string(self):     
        rv = self.app.get('/')
        assert 'Hello World!' in rv.data

if __name__ == '__main__':
    unittest.main()
