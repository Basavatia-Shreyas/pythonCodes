game_won = False
game_lost = False
room_one_complete = False
room_two_complete = False
room_three_complete = False

 

def room_one():
    global room_one_complete
    madeChoice = False
    life = 10
    while not madeChoice:
        print("You wake up in a dark and misty room. The only source of light are torches on the wall. You don't know where you are.")
        print("As you start to get up you fly in the air. You look around and everything, even yourself looks transparent.")
        print("You see a door to the left and patched up doorway on the left")
        answer_1 = input("type r to go through the right door and l to go to the patched up doorway")
        if answer_1 == "r":
            print("you go into the room on the right. you see a body laying on the floor and a heavy door with a huge lock.")
            answer_2 = input("press d to go to the door, press e to exit the room and press b to inspect the body")
            if answer_2 == "d":
                  print("The door is locked")
            elif answer_2 == "e":
                  print("You see a door to the right and patched up doorway on the left")
            elif answer_2 == "b":
                  print("You move towards the body. You try to touch it but you get shocked and jerk your hand away")
                  print("you lose 10 life")
                  life -= 10
                  print(life)
            else:
                  print("Unknown command")
        elif answer_1 == "l":
            print("You move towards the patched up doorway")
            print("To your suprise, you magicly float through the doorway")
            print("You see a door and a window.")
            answer_3 = input("press d to go through the door, w to go to the window and e to exit")
            if answer_3 == "d":
                  print("you go outside. A bright volcano waits ahead. The ground is molten ash and a stream of lava flows to your right.")
                  answer_4 = input("Press l to go to the stream of lava and press v to go to the volcano.")
                  if answer_4 == "l":
                      print("th stream of lava is too hot for you")
                      print("lose all 10 lives")
                      life -= 10
                      print(life)
                      if life <= 0:
                          print("Sorry you lose")
                          madeChoice = True
                  elif answer_4 == "v":
                      print("you walk for hours until you finally see a cave up ahead. You head into the cave.")
                      madeChoice = True
                      room_one_complete = True
                  else:
                      print("unknown command")
            elif answer_3 == "w":
                  print("You see a bright red light that blinds you. You don't recover")
                  print("Lose 10 life")
                  life -= 10 
                  print(life)
                  if life <= 0:
                          print("Sorry you lose")
                          madeChoice = True
            elif answer_3 == "e":
                print("You see a door to the left and patched up doorway on the left")
                

            else:
                print("Unknown Command")




def room_two():
    madeChoice = False
    while not madeChoice:
        print("As you walk in the cave you see vains growing up the cave walls.")
        print("Finally after what seemed forever you see a light. But there is something or someone guarding it")
        print("You see a sword at the edge of the cave")
        answer_5 = input("Press s to take the sword and c to continue through the cave.")
        if answer_5 == "s":
            print("you go to pick up the sword but you can't. It falls through your hands")
        elif answer_5 == "c":
            print("As you get closer you see a dragon guarding the light source")
            answer_6 = input("press l to go to the light source and d to fight the dragon")
            if answer_6 == "l":
                print("The dragon sees you try to walk by. It attacks you but its wing goes strait through you. You continue walking to the light source as the dragon keeps trying to attack you.")
                print("You get to the light source. It's so bright you have to look in the opposite direction.")
                print("You get to the light. When you touch it you feel a surge flow through you")
                print("everything looks brighter and nothing looks transparent anymore")
                print("you see a key in front of you and you pick it up.")
            elif answer_6 == "d":
                print("You charge towards to dragon and pound him. But you magicly move throught it landing in front of the light.")
                print("It is so bright you get blinded.")
                print("Lose 10 life")
                if life <= 0:
                          print("Sorry you lose")
                          madeChoice = True
                
                  
print("Welcome to Shreyas' magical text adventure game(warning this may be hard for certian people)")
print("and remember, HAVE FUN")
print("you have 10 lives. Make the wrong choices and you will lose lives. game over when your out of lives.\n make the right choices to get to the end") 
user_input = input("press y to continue")
if user_input == "y":
    room_one()
    if room_one_complete == True:
        room_two()
    elif room_two_complete == True:
        game_won = True
        print("Congrats, you beat the game")
else:
    print("Sorry you lose") 
                

