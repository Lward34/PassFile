
"""This script prompts a user enter inform for Voter Registration"""
import sys
print("*****************************************************************")
print("Welcome to the Python Voter Registration Application.")

option = input("Do you want to continue with Voter Registration? ").lower()
if option == "yes":
    USERNAME = str(input("What is your first name? "))
if option == "no":
    print("Cancel the Registration Process")
    sys.exit(0)

option = input("Do you want to continue with Voter Registration? ").lower()
if option == "yes":
    SURNAME = str(input("What is your last name? "))
if option == "no":
    print("Cancel the Registration Process")
    sys.exit(0)

option = input("Do you want to continue with Voter Registration? ").lower()
if option == "yes":
    AGE = int(input("What is your age? "))
if option == "no":
    print("Cancel the Registration Process")
    sys.exit(0)
if AGE < 18:
    print("You are NOT eligible to Vote")
    sys.exit(0)
if AGE <= 120:
    print("You are eligible to Vote")
else:
    print("Invalid Data Entry")
    print("Please try again")
    AGE = int(input("What is your age? "))

option = input("Do you want to continue with Voter Registration? ").lower()
if option == "yes":
    USCITIZEN = input("Are you a U.S Citizen? ")
if option == "no":
    print("Cancel the Registration Process")
    sys.exit(0)
if USCITIZEN == "yes":
    print("You are eligible to Vote")
if USCITIZEN == "no":
    print("You are NOT eligible to Vote")
    print("Cancel the Registration Process")
    sys.exit(0)

option = input("Do you want to continue with Voter Registration? ").lower()
if option == "yes":
    RESIDENCE = str(input("What state do you live? "))
if option == "no":
    print("Cancel the Registration Process")
    sys.exit(0)
while len(RESIDENCE)>2:
    RESIDENCE = str(input("Please enter the two letters of your state: "))

option = input("Do you want to continue with Voter Registration? ").lower()
if option == "yes":
    zipCode = float(input("What is your zipcode? "))
if option =="no":
    print("Cancel the Registration Process")
    sys.exit(0)

option = input("Do you want to continue with Voter Registration? ").lower()
if option == "yes" :
    print("******************************************************")
    print("Thanks for registering to vote.")
    print("Here is the information we received:")
    print("Name(first last): {} {}".format(USERNAME.capitalize(), SURNAME.capitalize()))
    print("Age:{}".format(AGE))
    print("U.S Citizen:{}".format(USCITIZEN.capitalize()))
    print("State:{}".format(RESIDENCE.capitalize()))
    print("Zipcode:{}".format(zipCode))
    print("Thanks for trying the Voter Registration Application")
    print("Your voter registration card should be shipped within 3 weeks.")
    print("*********************************************************")
else:
    print("Cancel the Registration Process")
    sys.exit(0)
