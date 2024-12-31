from pymongo import MongoClient
import pymongo
import datetime
import pprint

# Connect to mongo
my_client = MongoClient()
# Create db
db = my_client.mydb
# create collection users
users_collections = db.users
# create user var
# user1 = {"username": "nick_another", "password": "pass", "favorite_number": 4, "hobbies": ["python", "games", "pizza"]}
# insert user and retrieve id
# user_id = users_collections.insert_one(user1).inserted_id
# users = [
#     {"username": "marcelo", "password": "pass", "favorite_number": 9, "hobbies": ["python", "games", "pizza"]},
#     {"username": "ferreira", "password": "pass", "favorite_number": 3, "hobbies": ["python", "games", "pizza"]}
# ]
# inserted = users_collections.insert_many(users)
# print(inserted.inserted_ids)
# Count all documents
# print(users_collections.count_documents({}))
# Print document where {"favorite_number": 9}
# print(users_collections.count_documents({"favorite_number": 9}))
# # Find document where {"favorite_number": 9}
# find = users_collections.find_one({"favorite_number": 9})
# print(find)
# # Find document where {"favorite_number": 9}
# find = users_collections.find({"favorite_number": 9, "username": "marcelo"})
# for doc in find:
#     print("Find one: ",doc)
# # Find documents where {"favorite_number": 4} or {"username": "marcelo"}
# find = users_collections.find({"$or": [{"favorite_number": 4}, {"username": "marcelo"}]})
# for doc in find:
#     print("Find many: ",doc)

# current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
current_date = datetime.datetime.now()
print(current_date)
old_date = datetime.datetime(2009, 8, 11)
print(old_date)
# uid = users_collections.insert_one({"username": "bill", "date": current_date})
# Comparison operators used in MongoDB queries:
# - $gt: Greater than
# - $gte: Greater than or equal
# - $lt: Less than
# - $lte: Less than or equal
# - $ne: Not equal
# - $eq: Equal
# - $in: Matches any of the values specified in an array
# - $nin: Matches none of the values specified in an array
# - $and: Joins query clauses with a logical AND
# - $or: Joins query clauses with a logical OR
# - $not: Inverts the effect of a query expression
# - $nor: Joins query clauses with a logical NOR
# - $exists: Matches documents that have the specified field
# - $type: Selects documents if a field is of the specified type
# - $regex: Selects documents where values match a specified regular expression
# - $expr: Allows the use of aggregation expressions within the query language
# - $mod: Performs a modulo operation on the value of a field and selects documents with a specified result
# - $text: Performs text search
# - $where: Matches documents that satisfy a JavaScript expression
# search = users_collections.find({"date": {"$gte": old_date}})
# for doc in search:
#     print(doc)
# search = users_collections.find({"date": {"$exists": True}})
# for doc in search:
#     print("Exists: ", doc)
# search = users_collections.find({"date": {"$exists": False}})
# for doc in search:
#     pprint.pp(doc)
# Create index
# users_collections.create_index([("username", pymongo.ASCENDING)], unique=True)
# pprint.pp(sorted(list(users_collections.index_information())))