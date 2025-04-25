students = {
    "John": {
        "age": 28,
        "subjects": ["Math", "Science"],
        "grades": {85, 90}
    },
    "Alice": {
        "age": 22,
        "subjects": ["English", "History"],
        "grades": {88, 92}
    },
    "Bob": {
        "age": 25,
        "subjects": ["Physics", "Chemistry"],
        "grades": {78, 84}
    }
}

# 1. Add a new student
students["Jane"] = {
    "age": 30,
    "subjects": ["Biology", "Art"],
    "grades": [95, 89]
}

# 2. Update the grades
students["Alice"]["grades"] = [99,82]

# 3. Remove a subject
students["John"]["subjects"] = ["Math"]

# 4. Calculate the average grade of a specific student
grades = students["Alice"]["grades"]
average_grade = sum(grades) / len(grades)
print(type(grades))
print(f"The average grade of Alice is: {average_grade:.2f}")

# 5. Find the student with the highest grade
highest_grade=0
for name, student in students.items():
    if "grades" in student:
        max_now = max(student["grades"])
        if max_now > highest_grade:
            highest_grade = max_now
            top_student_name = name
            top_student = student
print(highest_grade, top_student_name ,top_student)

# 6. create a tuple for each student
student_tuples = [
    (name, student["age"], len(student["subjects"]))
    for name, student in students.items()
]

sorted_tuples = sorted(student_tuples, key=lambda x: x[2])

for student_tuple in sorted_tuples:
    print(student_tuple)