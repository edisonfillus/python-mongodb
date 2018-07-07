import pymongo

read_pref = pymongo.read_preferences.ReadPreference.SECONDARY

# w=3 means that it will wait until 3 nodes commit in memory.
# j=True means that it will wait until it will write in the disk (journal)
# w can be =majority, that means that more than half nodes confirm
# wtimeout is the time that it will wait for node confirmation
c = pymongo.MongoClient(host="mongodb://localhost:27017",
                        replicaSet="rs1",
                        w=3, wtimeout=10000, j=True,
                        read_preference=read_pref)

db = c.m101
people = db.people

print("inserting")
people.insert({"name":"Andrew Erlichson", "favorite_color":"blue"})
print("inserting")
people.insert({"name":"Richard Krueter", "favorite_color":"red"})
print("inserting")
people.insert({"name":"Dwight Merriman", "favorite_color":"green"})