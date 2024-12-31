from pymongo import MongoClient

# Connect to mongo
myClient = MongoClient()
# Create db
db = myClient.mydb
# create collection users
users = db.users
user1 = {"username": "nick_another", "password": "pass", "favorite_number": 4, "hobbies": ["python", "games", "pizza"]}
user_id = users.insert_one(user1).inserted_id
print(user_id)