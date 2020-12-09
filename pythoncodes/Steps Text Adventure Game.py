import random
import sys

playerHealth = 10
endKey = False
gameWon = False
gameOn = True
haveSword = False
weaknessRevealed = False
haveMysticStone = False


def gameOver():
    if not gameWon:
        print("GAME OVER")
        print("Thank you for playing")
    else:
        print("Congratulations, you have beaten Steps' Text Adventure game.")
        print("Thank you for playing")
    sys.exit()
    
def playerHit(maxLost):
    global playerHealth
    lifeLost = random.randrange(1, maxLost)
    playerHealth = playerHealth - lifeLost
    print("You have lost " + str(lifeLost) + " hit points")
    if playerHealth <= 0:
        print("You are out of hit points")
        gameOver()
    print("Player now has " + str(playerHealth) + " hit points left")

def firstRoom():
        print("You wake up in an unfamiliar room, bathed in darkness, all you see is a flashlight, "
              + "a note, and darkness")
        if endKey:
            print("You feel a heavy weight in your pocket, it is the key!")
        flashOn = False
        noteRead = False
        while not noteRead:
            if not flashOn:
                answer = input("type R to read the note, type F to turn on flashlight: ")
            else:
                answer = input("type R to read the note, type F to turn off the flashlight: ")
            if answer.lower() == "r" and not flashOn:
                print("It is too dark to read the note")
            elif answer.lower() == "r" and flashOn:
                print("Using the light from your flashlight you read the note")
                print("\"Hello " + playerName + ", I have chosen to capture you and submit you to a trial that will test your wit, skill, and knowledge of the Python programming language.")
                print("If you have paid attention in Steps' class, you should have no problem defeating my trial, if not..... you shall be trapped here forever!!!!")
                print()
                print("After you finish the note, overhead lights turn on, blinding you." +
                      " When your vision finally adjusts, you notice 2 doors in front of you.")
                noteRead = True
            elif answer.lower() == "f":
                if not flashOn:
                    print("You turn on the flashlight")
                else:
                    print("You turn off the flashlight")
                flashOn = not flashOn
            else:
                print("Unknown command.")
        answer = input("type L to enter the left door, R to enter the right door: ")
        if answer.lower() == "l":
            secondRoom()
        elif answer.lower() == "r":
            thirdRoom()
        else:
            print("A voice booms out from seemingly nowhere...")
            print("\"If you can't follow the simplest instructions, you will never succeed!\"")
            print("The doors lock and you are stuck in the room forever.")
            gameOver()

def secondRoom():
    print("You enter a room with no doors. There is a trap door, a broken ")
    print("window with the moonlight filtering in, and a picture of a lake. You can hear the sounds of dripping water and wind.")
    choiceMade = False
    while not choiceMade:
        answer = input("Type \"J\" to investigate the jar, type \"W\" to escape through the window, "
                       + "\ntype \"B\" to go back: ")
        if answer.upper() == "J":
            print("You open the jar, only to be sucked in by a supernatural force.")
            print("You fall for what seems an enternity, only to land in a reddish landscape.")
            underworld()
        elif answer.upper() == "W":
            print("You approach the broken window with dreams of escape in your mind, only to be shocked by an invisible force.")
            playerHit(6)
        elif answer.upper() == "B":
            print("You return to the previous room.")
            while True:
                answer = input("type L to enter the left door, R to enter the right door: ")
                if answer.upper() == "L":
                    secondRoom()
                elif answer.upper() == "R":
                    thirdRoom()
                else:
                    print("After hours of indecision standing in the starting room, the doors lock ")
                    print("and you are stuck in the room forever.")
                    gameOver()
def arena():
    global endKey
    global weaknessRevealed
    print("All of a sudden a large black dragon decends on the arena, casting a large shadow with its leathery wings.")
    print("It lands directly in front of you, and it prepares to attack.")
    dragonAlive = True
    attemptDodge = False
    while dragonAlive:
        if weaknessRevealed:
            answer = input("Use \"D\" to dodge, \"A\" to attack, \"R\" to run, and \"C\" to attack the Dragon's crystal: ")
        else:
            answer = input("Use \"D\" to dodge, \"A\" to attack, and \"R\" to run: ")
        if answer.upper() == "D":
            if not attemptDodge:
                print("You attempt to dodge the dragon's fire breath, it narrowly misses you, however the dragon keeps a closer eye on you")
                print("While dodging you see a glowing crystal on the dragon's chest.")
                weaknessRevealed = True
                attemptDodge = True
            else:
                print("You attempt to dodge the dragon's fire breath, but it is one step ahead of you, and you are bathed in its fire.")
                gameOver()
        elif answer.upper() == "A":
            if haveSword:
                print("You attack the dragon with your sword, the dragon's hide is thick, but the attack stuns him for a moment, allowing you to escape his counter attack.")
            else:
                print("You attempt to strike the dragon with your fists, but its hide is covered in thick hard scales, and you do no damage.")
                print("The dragon retaliates and smacks you with its paw")
                playerHit(8)
        elif answer.upper() == "R":
                print("You run away from the dragon while it chases you.")
                print("You manage to escape the arena, but you are hit by a fireball before you exit.")
                playerHit(6)
                print("You scramble out of the arena, alive, but singed.")
                underworld()
        elif answer.upper() == "C":
            if haveSword:
                print("You reach the dragon's chest, and swing your sword into his heart crystal, which shatters. The dragon falls down.")
                print("As the dragon's body disapears into mist, it leaves behind a massive key.")
                print("You touch the key, and your vision goes white.")
                dragonAlive = False
            else:
                print("You manage to reach the dragon's chest, but you have no weapon to attack with. The dragon laughs at your attempt ")
                print("and swats you with his paw.")
                playerHit(5)
        else:
            print("You scramble around in confusion, while the dragon laughs and eats you alive.")
            gameOver()
    endKey = True
    firstRoom2()

def desertCave():
    global haveSword
    topLed = False
    midLed = False
    botLed = False
    print("You descend the stairs of the cave, until it opens into a massive room filled with electronic gadgets and gizmos.")
    print("You see a massive container at the other end of the room, on the container glows 3 different red lights.")
    print("You approach a terminal next to the massive container. You lay your fingers on the keyboard and the monitor flickers on.")
    while True:
        print("The screen is blank except for 3 icons, marked by \"1,\" \"2,\" and \"3\"")
        answer = input("Type 1, 2, or 3, to click on the cooresponding icon, type \"B\" to go back: ")
        if answer == "1":
            print("A question appears on the screen. It asks you: \"What type of data does the input function return in python?\"")
            answer = input("What do you type into the terminal?")
            if answer.lower() == "string":
                print("That is correct!")
                print("The top light on the container turns green.")
                topLed = True
            else:
                print("That is incorrect")
                print("The computer electrocutes you")
                playerHit(3)
        elif answer == "2":
            print("A question appears on the screen. It asks you: \"What is the first thing we type when defining a function in python?\"")
            answer = input("What do you type into the terminal?")
            if answer.lower() == "def":
                print("That is correct!")
                print("The middle light on the container turns green.")
                midLed = True
            else:
                print("That is incorrect")
                print("The computer electrocutes you")
                playerHit(3)
        elif answer == "3":
            print("A question appears on the screen. It asks you: \"In python, if we want code to be apart of a while loop or if statement, what do we have to press before we start typing?\"")
            answer = input("What do you type into the terminal?")
            if answer.lower() == "tab" or answer.lower() == "indent":
                print("That is correct!")
                print("The bottom light on the container turns green.")
                botLed = True
            else:
                print("That is incorrect")
                print("The computer electrocutes you")
                playerHit(3)
        elif answer.upper() == "B":
            print("You leave the strange futuristic cave and return to where you first fell into the underworld.")
            underworld()
        else:
            print("Unknown Command")
        if topLed and midLed and botLed:
            print("The container opens revealing a glimmering sword. You take the sword, and exit the cave.")
            haveSword = True
            underworld()

def underworld():
    print("All around you, you see nothing but red sand, except for a large dome to the north")
    enterArena = False
    while True:
        answer = input("Enter \"S, E, or W\" to explore the wasteland or \"N\" to approach the dome: ")
        if answer.upper() == "S" or answer.upper() == "E":
            if answer.upper() == "S":
                direc = "south"
            else:
                direc = "north"
            print("You wander for hours to the " + direc + ". Hours turn into days, and you become dehydrated and battered by the elements.")
            print("Eventually you return to the exact spot you were when you entered the landscape.")
            playerHit(5)
        elif answer.upper() == "N":
            print("You approach the dome to find it houses a large arena, however, the arena is suspiciously empty.")
            answer = input("Type \"E\" to enter the arena, or \"B\" to leave: ")
            if answer.upper() == "E":
                print("You approach the arena...")
                arena()
            elif answer.upper() == "B":
                print("You leave the dome.")
            else:
                print("Unknown command")
        elif answer.upper() == "W":
            print("You walk for hours to the west, and just before giving up hope, you spot an oasis.")
            print("In the middle of the oasis, there is a golden pond surronded by palm trees. In the pond there is an island")
            print("With steps leading down into a desert cave.")
            while True:
                answer = input("Type \"C\" to enter the cave or \"B\" to go back.")
                if answer.upper() == "C":
                    desertCave()
                elif answer.upper() == "B":
                    underworld()
                else:
                    print("Unknown command")
def firstRoom2():
    global haveSword
    global haveMysticStone
    print("You return to the room you started in.")
    if endKey:
      print("You feel a heavy weight in your pocket, it is the key from the dragon!")
    if haveMysticStone:
      print("In your pocket is the mystical stone you retrieved from the great oak tree!")
    while True:
        answer = input("Type L to enter the left door, R to enter the right door: ")
        if answer.lower() == "l":
            secondRoom()
        elif answer.lower() == "r":
            thirdRoom()
        else:
            print("Unknown Command")

def spiderFight():
    spiderHealth = 10
    attackLegs = False
    attackHead = False
    attackThorax = False
    stage = 1
    while spiderHealth > 0:
        while spiderHealth > 0:
            answer = input("Enter \"A\" to attack, \"D\" to dodge, \"R\" to run: ")
            if answer.upper() == "A":
                answer = input("Enter \"L\" to attack the spider's legs, \"H\" to attack the spider's head, \"T\" to attack the spider's torso")
                if answer.upper() == "L":
                    if not attackLegs:
                        print("You attack the spiders legs with the sword, it causes minimal damage. The spider looks like its protecting its legs more closely now.")
                        spiderHit = random.randint(3,6)
                        spiderHealth -= spiderHit
                        print("The spider has lost " + str(spiderHit) + " health points, the spider now has " + str(spiderHealth) + " health points left")
                        attackLegs = True
                    else:
                        print("You try to attack the spider's legs, but it anticipates your attack and the spider retaliates with its fangs.")
                        playerHit(10)
                elif answer.upper() == "H":
                    if not attackHead:    
                        print("You attack the spider's head with your sword, causing massive damage. The spider looks like its protecting its head more closely now.")
                        spiderHit = random.randint(5,8)
                        spiderHealth -= spiderHit
                        print("The spider has lost " + str(spiderHit) + " health points, the spider now has " + str(spiderHealth) + " health points left")
                        attackHead = True
                    else:
                        print("You try to attack the spider's head, but it anticipates your attack, and the spider retaliates with its fangs.")
                        playerHit(10)
                elif answer.upper() == "T":
                    if not attackThorax:    
                        print("You attack the spider's thorax with your sword, causing medium damage. The spider looks like its protecting its thorax more closely now.")
                        spiderHit = random.randint(3,6)
                        spiderHealth -= spiderHit
                        print("The spider has lost " + str(spiderHit) + " health points, the spider now has " + str(spiderHealth) + " health points left")
                        attackThorax = True
                    else:
                        print("You try to attack the spider's thorax, but it anticipates your attack, and the spider retaliates with its fangs.")
                        playerHit(10)
                else:
                    print("You sit dazed and confused, mesmerized by the spider's stare. You are devoured whole.")
                    gameOver()
            elif answer.upper() == "D":
                print("You fail to dodge the spider's attack.")
                playerHit(10)
            elif answer.upper() == "R":
                print("You try to run but you find no escape. You are devoured by the spider as you run in a circle.")
                gameOver()
            else:
                print("You sit dazed and confused, mesmerized by the spider's stare. You are devoured whole.")
                gameOver()
    print("After defeating the spider, your vision goes white...")
    firstRoom2()
def greatOakTree():
    global haveMysticStone
    global playerHealth
    print("The massive hollow cavern you enter inside the tree is covered in spider webs. You see a hole in the ground covered in thick spider webs.")
    print("Vines cover the walls of the cavern, and far above you, you see a ledge wide enough for a man to stand on.")
    while True:
        answer =  input("Type \"H\" to enter the hole, type \"V\" to climb the vines, type \"B\" to leave the tree.")
        if answer.upper() == "H":
            print("The spider webs are too thick the penetrate, your attempt to enter the hole is futile.")
        elif answer.upper() == "V":
            print("You attempt to climb the vines, but you lose your footing, and you fall. Thankfully, the spider webs covering the hole slows your fall, and you land alive, although bruised in a dark chamber beneath the tree.")
            playerHit(3)
            print("The only thing you can see in the chamber, is a small glowing stone in the center. As you approach the stone, the hair on the back of your neck starts to stand on end. You pick up the stone.")
            print("As you grasp the stone, you feel energy surge into your body. (Your hit points have restored to 10)")
            playerHealth = 10
            print("You turn around but you are met with a massive spider! It prepares to strike...")
            haveMysticStone = True
            spiderFight()
        elif answer.upper() == "B":
            print("You exit the tree and return to where you first entered the forest")
            forest()
        else:
            print("Unknown command")
                

    
def forest():
    global haveMysticStone
    global gameWon
    print("You are surrounded by mist and tall trees. A full moon lights your surroundings, but you feel like someone, or some... thing, is watching you.")
    while True:
        print("The house you came from lies to the south, you spot an unnaturally large oak tree to the west, and nothing to the north and east.")
        answer = input("Type \"N, S, E, W\" to explore the forest")
        if answer.upper() == "S":
            print("As you walk back towards the house you escaped from, you hear a booming voice from the forest.")
            print("\"Only a fool walks back towards captivity!\" Evil laughter fills the forest and the darkness intensifies until you can't even see your hands in front of you.")
            print("You feel the forest floor disapear beneath your feet, and you fall deeper and deeper into the darkness.... you will never escape now...")
            gameOver()
        elif answer.upper() == "E":
            print("You walk deeper and deeper into the forest, until you come across a small clearing with a small stone pedestal. On the top of the pedestal has a small opening where a item may sit...")
            while True:
                if haveMysticStone:
                    answer = input("Type \"M\" to place mystical stone in the pedestal, \"B\" to go back: ")
                else:
                    answer = input("Type \"B\" to go back: ")
                if answer.upper() == "M" and haveMysticStone:
                    print("You place the mystic stone in the pedestal, and the darkness starts to lift from the forest. Flowers begin to bloom in the clearing. Suddenly you know the way home, and are free.")
                    gameWon = True
                    gameOver()
                elif answer.upper() == "B":
                    print("You walk back west.")
                    break
                else:
                    print("Unknown command.")
        elif answer.upper() == "N":
            print("You wander for hours to the north, or what you think is the north... eventually you see the light from the house you escaped, somehow you have returned to the same spot where you started...")
        elif answer.upper() == "W":
            print("You walk through the forst to the west, approaching the large oak tree. The tree looks as tall as a sky scraper, and has a large opening at the base of the trunk.")
            while True:
                  answer = input("Type \"E\" to enter the tree, \"B\" to go back.")
                  if answer.upper() == "E":
                      print("You enter the tree...")
                      greatOakTree()
                  elif answer.upper() == "B":
                      print("You return to the spot where you first entered the forest")
                      break
                  else:
                      print("Unknown Command")
                    
    

def thirdRoom():
    global endKey
    global gameWon
    print("The room is empty except for a large elaborate door with a large magical lock sealing it shut.")
    while True:
        answer = input("Type \"O\" to open the door or \"L\" to leave: ")
        if answer.upper() == "O":
            if endKey:
                print("The door opens into what you think is the night, but as the light from the small house fades as you walk further and further into the unknown forest, you realize you are far from being safe....")
                forest()
            else:
               print("The door is obviously locked.")
        elif answer.upper() == "L":
            firstRoom2()
        else:
            print("Unknown Command")




print("Welcome to Steps' spooky scary Text Adventure game!")
print()
print("Where all the frights happen in your mind!")
print("Depending on your choices, you will either escape to freedom, or ")
print("be trapped forever in captivity, you have 10 health points, and when your health ")
print("reaches 0, thats game over. Good Luck!")
print()
playerName = input("Please enter your name: ")
playerName = playerName.capitalize()
while True:
    answer = input("Hello " + playerName + ", are you ready to start? (Enter Y for yes N for no) ")
    if answer.lower() == "y":
        print()
        firstRoom()
    elif answer.lower() == "n":
        print("Those who never try, never succeed.")
        gameOver()
    else:
        print("Somebody needs to follow directions")