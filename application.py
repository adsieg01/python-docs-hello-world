from flask import Flask
import pymongo
import dns

app = Flask(__name__)

@app.route("/")
def hello():
    return "This is a test, if you can read this app service is up"
   
