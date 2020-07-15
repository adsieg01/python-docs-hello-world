from flask import Flask
import pymongo
import dns

app = Flask(__name__)

client = pymongo.MongoClient(
   "mongodb+srv://Dummy_User_01:xEXGTNByQzEBDyKF@cdf-sbx-azure-atlas-1.sn9jp.azure.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
db = client.sample_airbnb

@app.route("/")
def hello():
    return "Testing Mongo Connection to sample database"
   
