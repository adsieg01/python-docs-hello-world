from flask import Flask
import pymongo
import dns

app = Flask(__name__)

mongo "mongodb+srv://cdf-sbx-azure-atlas-1.sn9jp.azure.mongodb.net/test" --username Dummy_User_01
Password: xEXGTNByQzEBDyKF

@app.route("/")
def hello():
    return "This is a test, if you can read this app service is up"
   
