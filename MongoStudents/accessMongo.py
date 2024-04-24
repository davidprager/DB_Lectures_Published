
import pymongo

# todo  Connect to MongoDB


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
        # todo Create document and store in Database

        print ("Document inserted")

    # Display a document
    elif option == "r":
        student = input("Enter student to find: ")
        # todo Tell user if no documents

        # todo Loop through documents and print them

    # Update a document
    elif option == "u":
        # Get user input
        student = input("Enter student to update: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        height = input ("Enter height: ")
        weight = input ("Enter weight: ")

        # todo Create updated document and perform update

        print ("Document updated")

    # Delete a document
    elif option =="d":
        student = input("Enter student to delete: ")

        # todo Delete document

        print ("Document deleted")

    # Quit
    elif option == "e":
        print ("Done")
        break
    else:
        print ("???")
