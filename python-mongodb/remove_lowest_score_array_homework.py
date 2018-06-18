#!/usr/bin/env python
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.school
students = db.students

try:
    cursor = students.find({}) # all students

except Exception as e:
    print("Unexpected error:", type(e), e)

for student in cursor:

    lowest_score = None

    for score in student['scores']:
        if score['type'] == "homework":
            if (lowest_score is None) or (float(score['score']) < float(lowest_score['score'])):
                lowest_score = score
    print("Removing score ", lowest_score, " from student ", student['name'])
    result = students.update_one(
        {"_id": student["_id"]},
        {'$pull': {'scores': lowest_score}}
    )
    print("num matched: ", result.matched_count)

