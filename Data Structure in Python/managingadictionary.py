diction = {
    "Alice": [90, 28],
    "Bob": [80, 25],
    "John": [72, 42]
}
#1
diction["Jane"] = [85, 30]
#2
diction["Alice"] = [95, 29]
#3
del diction["John"]
#4
avg=sum(value[0] for value in diction.values()) / len(diction)
print(f"The average first value is: {avg}")
#5
highest_key = max(diction, key=lambda k: diction[k][0])
print(f"The key with the highest first value is: {highest_key}")