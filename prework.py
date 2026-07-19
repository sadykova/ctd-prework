#This script checks a user's password and age. 
#Access is granted only if the password is correct and the user is over 18.

correct_password = "codethedream"

user_password = input("Please enter your password: ")
user_age = int(input("Please enter your age: "))

if user_password == correct_password and user_age >= 18:
    print("Access granted. Mission begins now 🚀")
else:
    print("Access denied. Mission aborted ❌")
