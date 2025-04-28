#1 Create a list of dictionaries
listofdict=[
{
    "name":"jack",
    "grades": [97, 85, 78],
},
{
    "name":"john",
    "grades": [90, 82, 54],
},
{
    "name":"mike",
    "grades": [30, 45, 67],
}
]

# 2.5 Handle potential errors
for student in listofdict:
    if not student["grades"]:
        print(f"Student {student['name']} has no grades available.")
        continue

#2.1 Calculate the average grade
avg = list(map(lambda x: {"name": x["name"], "average": round(sum(x["grades"]) / len(x["grades"]),2)}, listofdict))
print(avg)

#2.2 Find students who passed
passed = list(filter(lambda x: x["average"] >= 50, avg))
print(passed)

#2.3 Sort students by their average grade.
sort= list(sorted(avg, key=lambda x: x["average"], reverse=True))
print(sort)

#2.4 Increase each student's grade by 5 points
inc= list(map(lambda x: {"name": x["name"], "grades": list(map(lambda y: y + 5 if y<=95 else y, x["grades"]))}, listofdict))
print(inc)

# 2.6 Generate a summary report
summary = [(student["name"], student["average"]) for student in avg]
print("Summary:", summary)
highest_grade = max(summary, key=lambda x: x[1])[1]
print("Highest Grade in the Class:", highest_grade)
top_students = list(filter(lambda x: x[1] == highest_grade, summary))
print("Top Students:", top_students)
print("\nSummary Report:")
print(f"Highest grade in the class: {highest_grade}")
print("Student(s) with the highest grade:")
for name, grade in top_students:
    print(f"- {name} with an average of {grade}")
