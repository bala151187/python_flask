import unittest
from webs import hello

class AppTestCase(unittest.TestCase):
    def test_string(self):     
        rv = self.app.get('/')
        assert 'Hello World!' in rv.data

if __name__ == '__main__':
    unittest.main()
