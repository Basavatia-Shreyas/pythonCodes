player_age = input("please enter your age:")

player_age = int(player_age)

if player_age < 7:
    print("your too young for camp")
elif player_age >= 7 and player_age<= 17:
    print("you can attend camp!")
else:
    print("your too old for camp") 
    
