num=0
while num!='exit':
    num=input("Enter a number, or enter 'exit' to stop the program: ")
    
    if num == 'exit':
        print ("Exiting the program ")
        break

    try:
        if int(num)%2==0:
            print("Even")
        elif int(num)%2==1:
            print("Odd")
    except ValueError:
            print("Error! Please enter a valid number.")