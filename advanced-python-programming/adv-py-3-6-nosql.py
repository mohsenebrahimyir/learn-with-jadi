## https://realpython.com/introduction-to-mongodb-and-python/

## Import main libraries
from pymongo import MongoClient
import pprint

## Making a Connection with MongoClient
# print("connecting to mongoDB")
client = MongoClient(host ='localhost', port=27017)
# print("connected to mongoDB")
# print(client)

## Working With Databases, Collections, and Documents
db = client["rptutorials"]
# print(db)

## insert One Document
# tutorial1 = {
#     "title": "Working With JSON Data in Python",
#     "author": "Lucas",
#     "contributors": [
#         "Aldren",
#         "Dan",
#         "Joanna"
#     ],
#     "url": "https://realpython.com/python-json/"
# }

tutorial = db.tutorial
# print(tutorial)

# result = tutorial.insert_one(tutorial1)
# print(f"One tutorial: {result.inserted_id}")


## Insert Many Documents
# tutorial2 = {
#     "title": "Python's Requests Library (Guide)",
#     "author": "Alex",
#     "contributors": [
#         "Aldren",
#         "Brad",
#         "Joanna"
#     ],
#     "url": "https://realpython.com/python-requests/"
# }

# tutorial3 = {
#     "title": "Object-Oriented Programming (OOP) in Python 3",
#     "author": "David",
#     "contributors": [
#         "Aldren",
#         "Joanna",
#         "Jacob"
#     ],
#     "url": "https://realpython.com/python3-object-oriented-programming/"
# }

# new_result = tutorial.insert_many([tutorial2, tutorial3])
# print(f"Multiple tutorials: {new_result.inserted_ids}")

## Print Documents
# for doc in tutorial.find():
#     pprint.pprint(doc)

## Counting
tutorial.count()