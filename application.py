from flask import Flask
import pymongo
import dns

app = Flask(__name__)

client = pymongo.MongoClient(
   "mongodb+srv://Dummy_User_01:xEXGTNByQzEBDyKF@cdf-sbx-azure-atlas-1.sn9jp.azure.mongodb.net/?retryWrites=true&w=majority")
db = client["sample_airbnb"]
mycol = db["collection-test-creation"]

#a document
tester = { "name": "Saranya", "address": "Kochi" }

#insert a document to the collection
x = mycol.insert_one(tester)

@app.route("/")
def hello():
    return "Testing Mongo Connection to sample database"
   
