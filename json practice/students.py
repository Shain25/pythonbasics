import json

highest=0
sname=""
num=1

# 1. Load the data from students.json
with open("students.json", "r") as file:
    data = json.load(file)

# 2+3 Calculate the average score and Find the winner
for student in data["students"]:
    avg = sum(student["scores"])/len(student["scores"])
    if avg>highest:
        highest=avg
        sname=student["name"]
print(f"The student with the highest score of {highest:.2f} is {sname}")

# 4 Add a new field "status"
for student in data["students"]:
    num+=1
    if sname==student["name"]:    
        student["status"]="Winner"
    else:
        student["status"]="Participant"

# 5+6 Add a new student and Save the list back to the file
if student["name"]!="Jeff":
    data["students"].append({"id":num,"name":"Jeff","scores":[10, 9, 10]})
    json.dump(data, open("students.json", "w"), indent=4)
else:
    print(f"The student {student["name"]} already exists")