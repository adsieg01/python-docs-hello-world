from flask import Flask
import pymongo
import dnspython

app = Flask(__name__)

client = pymongo.MongoClient(
   "mongodb+srv://Dummy_User_01:xEXGTNByQzEBDyKF@cdf-sbx-azure-atlas-1.sn9jp.azure.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

@app.route("/")
def hello():
    return "Testing Mongo Connection"
   
