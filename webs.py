from flask import Flask
webserv = Flask(__name__)

@webserv.route("/")
def hello():
    return "Hello World!"
        
if __name__ == "__main__":
    webserv.run(host='0.0.0.0',port=8080)
