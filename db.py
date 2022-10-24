from pymongo import MongoClient

mongodb = "mongodb+srv://romanporada:roma31pora01@cluster0.coghme5.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongodb)
database = client.get_database("default")
users_collection = database.get_collection("users")