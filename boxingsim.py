import random

Jab=1
Cross=2
Lead_Hook=3
Rear_Uppercut=4

pmove=int(input("Pick your move number: 1-Jab, 2-Cross, 3-Lead_Hook, 4-Rear_Uppercut "))

move=random.randint(1, 4)

#Jab stronger than Rear Uppercut, Rear Uppercat stronger than Lead Hook and Cross, Cross stronger than Jab, Lead Hook stronger than Cross and Jab
if pmove!=1 and pmove>move:
    print("You won!")
elif pmove==move:
    print("Tie!")
elif pmove==1 and move==4:
    print("You won!")
else:
    print("You lose!")