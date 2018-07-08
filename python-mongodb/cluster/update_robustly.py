import pymongo
import pymongo.errors
import time

client = pymongo.MongoClient(host=["mongodb://localhost:27017",
                                   "mongodb://localhost:27018",
                                   "mongodb://localhost:27019"],
                             replicaSet="m101")

db = client.m101
things = db.things

for i in range(500):
    time.sleep(.1)  # Don't want this to go too fast.
    votes = 0
    for retry in range(3):
        try:  # to read the doc up to 3 times.
            votes = things.find_one({'_id': i})["votes"] + 1
            break
        except pymongo.errors.AutoReconnect as e:  # failover!
            print("Exception reading doc with _id = {_id}." +
                  " {te}: {e}".format(_id=i, te=type(e), e=e))
            print("Retrying...")
            time.sleep(5)
        except Exception:
            print("Unable to read from the database. Aborting.")
            exit()
    for retry in range(3):
        try:  # to read the doc up to 3 times.
            things.update_one({'_id': i}, {'$set': {'votes': votes}})
            print("Updated Document with _id = {_id}".format(_id=i))
            break
        except pymongo.errors.AutoReconnect as e:  # failover!
            print("Exception writing doc with _id = {_id}. {te}: {e}".format(_id=i, te=type(e), e=e))
            print("Retrying...")
            time.sleep(5)
        except Exception:  # If no break, we failed to write the document. Abort.
            print("We have failed to increment the 'votes' field for "
                  "the document with _id = {_id} to {votes}. Exiting.".format(_id=i, votes=votes))
            exit()
