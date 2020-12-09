
def main():

    from random import randint

    player = input('rock (r), paper(p), scissors (s)').lower()
    chosen = randint(1,3)


    if chosen == 1:
        computer = "0"
    elif chosen == 2:
        computer = "____"
    else:
        computer = ">8"
    print('rock = 0 \npaper = ____ \nscissors = >8')
    if player == "r":
        player = '0'
    elif player == 's':
        player = '>8'
    elif player == 'p':
        player = '____'
    else:
        print('enter r, p, or s')
        exit()
    print(player, 'VS', computer)


    if player == computer:
        print('draw')
    elif player == '0' and computer == '>8':
        print('Player Wins!')
    elif player == '0' and computer == '____':
        print('Computer Wins!')
    elif player == '____' and computer == '0':
        print('Player Wins!')
    elif player == '____' and computer == '>8':
        print('Computer Wins!')
    elif player == '>8' and computer == '0':
        print('Computer Wins!')
    elif player == '>8' and computer == '____':
        print('Player Wins!')

    again = input('Do you want to play again? y/n').lower()
    if again == 'y':
        main()

    else:
        exit()
main()
