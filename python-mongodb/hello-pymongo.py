from pymongo import MongoClient


# connect to database
connection = MongoClient('localhost', 27017)

# Use db admin
db = connection.admin

# handle to system.version collection
sv = db.system.version

# Select one document
document = sv.find_one()

# Select the field version
print(document['version'])
