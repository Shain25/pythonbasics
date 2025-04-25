start=int(input("Enter a number: "))
end=int(input("Enter another number: "))
d=int(input("Enter a divisor: "))

a=0

for i in range(start, end+1):
    if i%d==0:
        print(i)
        a+=1
print("The number of integers divisible by 3 between", start, "and", end, "is", a)