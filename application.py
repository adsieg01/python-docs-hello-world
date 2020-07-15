from flask import Flask
import pymongo
import dns

app = Flask(__name__)

client = pymongo.MongoClient(
   "mongodb+srv://Dummy_User_01:xEXGTNByQzEBDyKF@cdf-sbx-azure-atlas-1.sn9jp.azure.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
db = client.sample_airbnb
mycol = db["collection-test-creation"]


@app.route("/")
def hello():
    return db.list_collection_names()
   
