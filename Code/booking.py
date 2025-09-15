#Importing everything we need
import json
Appointments = "Data/appointments.json"
from datetime import datetime, timedelta
from typing import List 



dtFmt = "%Y-%m-%d %H:%M"

def generateHourSlots(dateStr: str, startHour: int = 9, endHour: int = 18) -> List[str]:
    day = datetime.strptime(dateStr, "%Y-%m-%d")
    t   = day.replace(hour=startHour, minute=0, second=0, microsecond=0)
    end = day.replace(hour=endHour,   minute=0, second=0, microsecond=0)
    slots = []
    while t < end:
        slots.append(t.strftime(dtFmt))
        t += timedelta(hours=1)
    return slots

def loadAppointments():
    try:
        with open(Appointments, "r" ,encoding = "utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def getBookedSlots(doctorID: int, dateStr: str) -> List[str]:
    appts = loadAppointments()
    booked = []
    for a in appts:
        if a.get("doctorID") == doctorID and str(a.get("slot","")).startswith(dateStr):
            booked.append(a["slot"])
    return booked

def getFreeSlots(doctorID: int, dateStr: str, startHour = 9, endHour = 18) -> List[str]:
    freeSlots = []
    totalSlots = generateHourSlots(dateStr,startHour,endHour)
    bookedSlots = getBookedSlots(doctorID, dateStr)
    for a in totalSlots:
         if a not in bookedSlots:
            freeSlots.append(a)
    return(freeSlots)

def chooseSlots(doctorID: int , dateStr: str, startHour = 9, endHour = 18) -> List[str]:
    slots = getFreeSlots(doctorID, dateStr,startHour,endHour)
    print("Please select the time slot that suits you for",dateStr,":")

    if not slots:
        print("No free 1-hour slots on that date.")
        return None
    
    for index,a in enumerate(slots, start=1):
        print(index, a.split(" ")[1])
    while True:
        choice = input("Enter the number of your chosen slot. Press ENTER to cancel appointment").strip()
        if choice == "":
            return False
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(slots):
                return slots[choice - 1]
        print("Invalid choice. Please pick a number between 1 and", len(slots))




def createSlots(userName: str, docID: int, docName: str,specialty: str,SelectedAppt: str):
    record  = {
    "patientUsername": userName,
    "doctorID": docID,
    "doctor_name": docName,
    "specialty": specialty,
    "slot": SelectedAppt,
    "createdAt": datetime.now().strftime(dtFmt)
    }
    try:
        with open(Appointments, "r", encoding="utf-8") as f:
            appts = json.load(f)
    except FileNotFoundError:
        appts = []
    
    appts.append(record)
    with open(Appointments, "w", encoding = "utf-8") as f:
        json.dump(appts, f, indent=2)
    print("Appointment saved")




    
    

