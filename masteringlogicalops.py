#manual evaluation
 # 1. True
 # 2. True
 # 3. False
 # 4. 0
 # 5. True

#write boolean expressions
 #10<=x<=20
 #s != "" and "py" in s
 #n<0 or n>100
 #user_role == 'admin' and active=='True' or superuser=='True'
 #not(temperature<0 or temperature>35)

#Access Eligibility Checker
age=int(input("What is your age? "))
has_ticket=input("Do you have ticket? write y/n ")
vip_code=input("What is you vip code? leave blank if you don't have one ")

if age>=0:
    if age>=18 and has_ticket=='y' or vip_code=="GOLDVIP":
        eligible=True
        print("Access granted: <eligible>")
    else:
        print("not eligible")

#Form Input Validator
username=input("Enter username ")
password=input("Enter password ")
email=input("Enter email ")

if username!="" and len(password)>=8 and any(char.isdigit() for char in password) and email.count("@")==1 and email.endswith(".com"):
    print("Form Valid")
else:
    print("Form invalid")

#Discount & Surcharge Calculator
order_amount=float(10.90)
customer_type="member"
coupon_code="SAVE15"

if order_amount<50:
    order_amount*=1.05
    print(order_amount)

if customer_type=="member" or customer_type=="vip":
    order_amount*=0.9

if customer_type=="vip" and coupon_code=="SAVE15":
    order_amount*=0.85

print(f"Final Total: {order_amount:.2f}")