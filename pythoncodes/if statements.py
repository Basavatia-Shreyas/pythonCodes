import random

computer_number = random.randrange(0, 101)
print(computer_number)

guessed = False

while True:
    if not guessed:
        answer = input("guess the number")
        if int(answer) == computer_number:
            guessed = True
            print("you got it")
            break
        elif int(answer) > computer_number:
            print("your guess is too high.")
        else:
            print("your guess is too low")

    else:
        break
