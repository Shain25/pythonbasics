#Salary Breakdown
salary=int(input("What is your salary? "))
netsa=salary*0.78
rent=int(input("How much do you pay for rent? "))

if netsa>rent:
    if netsa-rent>1000:
        print("Rent and save!")
    else:
        print("Just rent")

else:
    print("Not enough")

#Shipping Calculator
price=79
quan=9
sum=price*quan

if sum>500:
    print(f"You got free shipping and a discount. Total cost is {sum*0.9}")
else:
    if sum>200:
        print(f"You got free shipping! Total cost is {sum}")
    else:
        print(f"Total cost is {sum+50}")

#Medieval Guard Duty
age=19
has_gold_pass=True
is_royal=False
is_blacklisted=False

if age>=18 & is_blacklisted==False:
    if has_gold_pass==True | is_royal==True:
        print("You are allowed in!")
    else:
        print("You are not allowed in")
else:
    print("You are not allowed in")

#Car Insurance Quote
driverage=22
accdientc=0
accp=accdientc*500

if age<25:
    if 3000+accp<5000:
        print("Standard")
    else:
        print("High Risk")
else:
     if 2000+accp<5000:
        print("Standard")
     else:
        print("High Risk")

#Lab Safety Checklist
temp=37
pressure=22
volt=230

if (20<temp<80 and pressure<50 and 20<volt<250):
    print("Safe to proceed")
else:
    print("Unsafe conditions")

#Wizard's Final Exam
spellp=75
accy=45
ctrl=90
avg=(spellp+accy+ctrl)/3

if spellp<40 or accy<40 or ctrl<40:
    print ("Fail")
else:
    if avg<60:
       print ("Fail")
    elif 60<=avg<=74:
       print ("Apprentice")
    elif 75<=avg<=89:
       print ("Mage")
    elif avg>=90:
       print ("Archmage")