# 1. Inputs (use input() in this exact order)
code1=input(str("put a single word ")).lower()
code2=input(str("put a single word ")).lower()
code3=input(str("put a single word ")).lower()
numA=int(input("put a number "))
numB=int(input("put a number "))

# 2. Validation
if code1.isalpha()==False or code2.isalpha()==False or code3.isalpha()==False:
    print("Invalid codeword")
    
if numA<1 or numB<1:
    print("Invalid numbers")

# 3. Variable Operations (create these variables)
combined=code1+"-"+code2+"-"+code3
secret_number=(numA*numB)+numA-numB
swapped_A=numB
swapped_B=numA
avg_value=(numA+numB)/2
message_length=len(combined)
is_palindrome=combined.replace("-","") == combined[::-1].replace("-","")

# 4. Output
print(f"Secret Code: {combined}")
print(f"Secret Number: {secret_number}")
print(f"Swapped Values: {swapped_A, swapped_B}")
print(f"Average of Originals: {avg_value}")
print(f"Combined Length: {message_length}")
print(f"Palindrome: {is_palindrome}")