age=int(input("Enter your age: "))
day=input("Enter weekday/weekend: ")
loyaltymember=input("Are you a loyalty member? (y/n): ")
tprice=20

if age<13:
    tprice*=0.5
    if day=="weekend":
        tprice+=5
        if loyaltymember=="y":
            tprice-=2
        print(f"The ticket price is {int(tprice)} $")
    elif day=="weekday":
        if loyaltymember=="y":
            tprice-=2
        print(f"The ticket price is {int(tprice)} $")
    else:
        print("Invalid day")
    
elif age>=60:
    tprice*=0.7
    if day=="weekend":
        tprice+=5
        if loyaltymember=="y":
            tprice-=2
        print(f"The ticket price is {int(tprice)} $")
    elif day=="weekday":
        if loyaltymember=="y":
            tprice-=2
        print(f"The ticket price is {int(tprice)} $")
    else:
        print("Invalid day")

if age<=0:
    print("Invalid age")

elif age>=13 and age<60:
    if day=="weekend":
        tprice+=5
        if loyaltymember=="y":
            tprice-=2
        print(f"Thse ticket price is {int(tprice)} $")
    elif day=="weekday":
        if loyaltymember=="y":
            tprice-=2
        print(f"Thse ticket price is {int(tprice)} $")
    else:
        print("Invalid day")

        