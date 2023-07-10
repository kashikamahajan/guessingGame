import random

sec_num=random.randint(1,100)

guess=0
trys=0

print("You will have 10 guesses")
while trys<10:

    trys=trys+1
    guess=int(input("Enter Guess: "))

    if guess==sec_num:
        print("Guessed it right!")
        break
    elif abs(guess-sec_num)<5:
        print("burning warm")
    elif abs(guess-sec_num)<20 and abs(guess-sec_num)>5 :
        print("warm")
    elif guess>1 & guess<100:
        print("cold")
    else:
        print("Invalid Input")

if(guess!=sec_num):
    print("Opps! Ran out of guesses! The number was")
    print(sec_num)