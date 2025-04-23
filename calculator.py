def calculator():
    num1=float(input("Enter first number "))
    op=input("Enter math operation ")
    num2=float(input("Enter second number "))
    
    if op == '+':
        res = num1 + num2
    elif op == '-':
        res = num1 - num2
    elif op == '*':
        res = num1 * num2
    elif op == '/':
        res = num1 / num2
    elif op == '^':
        res = num1 ** num2
    elif op == '%':
        res = num1 % num2
    else:
        print("Unsupported operation:", op)
        return
    
    print("Result is " , res)

calculator()

#Reliability: the calculator checks if you use a supported operation.
#you can't put a wrong content into the calculator.

#Maintainability: added option to enter float numbers.
#the user gets a message when puts an unsupported operation.

#Scalability: the software and its code is very simple to understand