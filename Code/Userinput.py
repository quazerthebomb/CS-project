import json
#import the data 
with open("Data/symptomdata.json", "r")as file:
    data = json.load(file)

counts = {speciality: 0 for speciality in data}
#search each word in the database
def keywordSearch(symptomList):
    words = symptomList.lower().split()
    for speciality,keywords in data.items():
        for keyword in keywords:
            if keyword in symptomList.lower():
                counts[speciality] += 1
            else:
                if keyword in words:
                    counts[speciality] +=1 
        return(counts)

