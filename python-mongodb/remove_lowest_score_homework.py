#!/usr/bin/env python
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.students
grades = db.grades

print("find(), reporting for duty")

query = {'type': 'homework'}

try:
    cursor = grades.find(query)
    cursor.sort([('student_id', pymongo.ASCENDING), ('score', pymongo.DESCENDING)])

except Exception as e:
    print("Unexpected error:", type(e), e)

last_student = cursor[0]
count = cursor.count()
i = 0

for student in cursor:
    i = i + 1
    if i == count:
        grades.delete_one(student)  # Last one, delete
        break
    if student['student_id'] == last_student["student_id"]:
        last_student = student  # update last student
        continue  # next
    else:
        grades.delete_one(last_student)  # Remove last student, as it has the lowest score
        last_student = student  # update last student
