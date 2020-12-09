import random

number = random.randint(0, 20)
isguessed = False
count = 0

while (isguessed == False and count <4):
    print("guesses made: " + str(count))
    guess = input("enter your guess ")
    guess = int(guess)
    if(guess == number):
        isguessed = True
    elif(guess > number):
        print("your guess is too high")
        count = count + 1
    elif(guess < number):
         print("your guess is too low") 
         count  = count + 1
    else:
        count = count + 1
if(isguessed == True):
    print("congrats" + "\nyou guessed the number in " + str(count) + " tries") 
else:
    print("sorry you didn't guess the number") 
