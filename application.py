from flask import Flask
import pymongo
import dns

app = Flask(__name__)

client = pymongo.MongoClient(
   "mongodb+srv://Dummy_User_01:xEXGTNByQzEBDyKF@cdf-sbx-azure-atlas-1.sn9jp.azure.mongodb.net/?retryWrites=true&w=majority")
db = client["sample_db"]
mycol = db["test-collection"]

#a document
tester = { "name": "Test", "address": "Document" }

#insert a document to the collection
x = mycol.insert_one(tester)

@app.route("/")
def hello():
    return "This is a test, if you can read this app service is up"
   
