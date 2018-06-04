import bottle
from pymongo import MongoClient


# this is the handler for the default path of the web server

@bottle.route('/')
def index():
    # connect to database
    connection = MongoClient('localhost', 27017)

    # Use db admin
    db = connection.admin

    # handle to system.version collection
    sv = db.system.version

    # Select one document
    document = sv.find_one()

    return '<b>Congratulations! You are using MongoDB v%s!</b>' % document['version']


bottle.run(host='localhost', port=8082)