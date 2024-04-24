
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient()
db = client.students
students = db.students



while True:
    option = input("\nOptions are (c)reate, (r)ead, (u)pdate, (d)elete, (e)nd: ")

    # Insert a new document
    if option == "c":
        # Get user input
        student = input("Enter student to update: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        height = input("Enter height: ")
        weight = input("Enter weight: ")
        # Create document and store in Database
        doc = {
            "Name":student,
            "Age": age,
            "Gender": gender,
            "Height": height,
            "Weight": weight
        }
        students.insert_one(doc)

        print ("Document inserted")

    # Display a document
    elif option == "r":
        student = input("Enter student to find: ")
        # Tell user if no documents
        if students.count_documents({"Name": student}) == 0:
            print ("None found")
        else:
            #Loop through documents and print them
            for doc in students.find({"Name": student}):
                for key,value in doc.items():
                    print (key, value)

    # Update a document
    elif option == "u":
        # Get user input
        student = input("Enter student to update: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        height = input ("Enter height: ")
        weight = input ("Enter weight: ")

        # Create updated document and perform update
        updated_doc ={
            "Name": student,
            "Age": age,
            "Gender": gender,
            "Height": height,
            "Weight": weight
        }
        students.update_one(
            {"Name": student},
            {"$set": updated_doc}
        )


        print ("Document updated")

    # Delete a document
    elif option =="d":
        student = input("Enter student to delete: ")

        # Delete document
        students.delete_one({
            "Name": student
        })

        print ("Document deleted")

    # Quit
    elif option == "e":
        print ("Done")
        break
    else:
        print ("???")
