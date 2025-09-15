import json
#importing the data 
userDataFP = "Data/userdata.json"
#A function to check that the username and password are registered
def userloginCheck():
    with open(userDataFP, "r") as file:
        data = json.load(file)


        for i in range(3):
            usernameAttempt = input("What is your username: ")
            passwordAttempt = input("What is your password: ")

            matchFound = False
            for user in data: #iterate through the list
                if user["username"] == usernameAttempt and user["password"] == passwordAttempt:
                    print("Login successful!")
                    return usernameAttempt
            print("Login failed! please try again:")
        print("Login failed! try another time!") #if the loop finishes without returning..
        return None
    

