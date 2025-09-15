#importing all the functions
from booking import chooseSlots, createSlots
from login import userloginCheck
from Userinput import keywordSearch
from doctorSelect import selectDoc
from datetime import datetime

userName = userloginCheck()
if not userName:
    print("Exiting program now.")
    exit()

symptomInput = input("Please write about what is wrong with you. Do not mention any symptoms that dont apply to you: ")



docID, docName, speciality = selectDoc(keywordSearch(symptomInput)) 
def askForDate():
    while True:
        try:   
        
                selectedDay = input("Which date would you like to book? please enter in a format of YYYY-MM-DD: ").strip()
                datetime.strptime(selectedDay, "%Y-%m-%d")
                return selectedDay
        except ValueError:
            print("Invalid date format. Example: 2025-08-26")
chosenDay = askForDate()




selectedAppt = chooseSlots(docID,chosenDay,9,18)
if not selectedAppt:
     print("Exiting program now.")
     exit()
createSlots(userName,docID,docName,speciality,selectedAppt)

