from flask import Flask
from source.api import app
from unittest import TestCase

webserv = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

class TestIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_thing(self):
        response = self.app.get('/')
        assert "Hello World!"
        
if __name__ == "__main__":
    webserv.run(host='0.0.0.0',port=8080)
