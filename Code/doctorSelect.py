import json
from datetime import datetime, timedelta
from typing import List
with open("Data/mockdata.json", "r") as file:
    data = json.load(file)


def selectDoc(counts):
    recent = 0
    selectedSpecialty = ""
    for a in counts.keys():
        if counts[a] > recent:
            recent = counts[a]
            selectedSpecialty = a
    for a in data:
        if a["specialty"] == selectedSpecialty:
            return a["id"], a["name"], selectedSpecialty
        

        









