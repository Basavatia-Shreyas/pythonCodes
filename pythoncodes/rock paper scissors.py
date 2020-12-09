import random


game_end = False
print("Welcome to Steps' Rock, Paper scissor game! ")

       
while (game_end == False):
    player_hand = input("Enter 1 for Rock, 2 for Paper, 3 for Scissor, or E to stop playing ")
    cpu_hand = random.randint(1, 3)
    
    if (player_hand == "E"):
        game_end = True
    elif (cpu_hand == int(player_hand)):
        print("The computer played the same thing as you did, tie!")
    elif (cpu_hand == 1):
        print("the computer played Rock")
        if (int(player_hand) == 2):
            print("You win")
        else:
            print("you lose")
    elif (cpu_hand == 2):
        print("the computer played paper")
        if (int(player_hand) == 3):
            print("You win")
        else:
            print("You Lose")
    elif (cpu_hand == 3):
        print("the computer played scissor")
        if (int(player_hand) == 1):
            print("you win")
        else:
            print("You Lost")
print("Thank You for playing")
        
