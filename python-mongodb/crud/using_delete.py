import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")
        
# removes one student
def remove_student(student_id):

    # get a handle to the school database
    db=connection.school
    scores = db.scores

    try:

        # Remove only first match
        #result = scores.delete_one({'student_id': student_id})

        # Remove all match
        result = scores.delete_many({'student_id':student_id})

        print("num removed: ", result.deleted_count)

    except Exception as e:
        print("Exception: ", type(e), e)

def find_student_data(student_id):
    # get a handle to the school database
    db=connection.school
    scores = db.scores
    
    print("Searching for student data for student with id = ", student_id)
    try: 
        docs = scores.find({'student_id':student_id})
        for doc in docs:
            print(doc)

    except Exception as e:
        print("Exception: ", type(e), e)


remove_student(1)
find_student_data(1)

