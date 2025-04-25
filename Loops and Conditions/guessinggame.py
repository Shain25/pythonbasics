import random
unum=int(input("Guess the number between 1 and 20: "))
rand=random.randint(1, 20)
gue=4

while unum!=rand and gue>0:
    if unum>rand:
        print("Too high!")
    elif unum<rand:
        print("Too low!")
    gue-=1
    unum=int(input("Guess again: "))
    if gue==0:
        print("Game Over! the correct number was", rand)
if unum==rand:
    print("Correct! You guessed it!")