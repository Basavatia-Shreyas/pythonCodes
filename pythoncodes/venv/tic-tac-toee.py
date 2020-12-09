# Get started with interactive Python!
# board = 'x','x','x','x','x','x','x','x','o','x','x','x'

# You can also write comments for your students to read like this.
# When you're done, add this to your website using the embed code.

def player_select():
    player_1 = ''
    player_2 = ''
    player_1 = input('player 1, do you want to be X or O?').upper()
    player_2 = input('player 2, do you want to be X or O?').upper()
    if player_1 == 'X':
        player_2 = 'O'
        # global player_1
        # global player_2
    elif player_1 == "O":
        player_2 = 'X'
        # global player_1
        # global player_2
    else:
        print('enter X or O')
        player_select()
    print('player 1 is {} and player 2 is {}.'.format(player_1, player_2))

    def game_play():
        not_won = False
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        player_1_location = []
        player_2_location = []
        while not_won == False:
            player_1_location.append(input("Player 1 enter a location 1-9"))
            player_2_location.append(input("Player 2 enter a location 1-9"))
            for i in player_1_location:
                if i == '1':
                    board[0].append(player_1)
                elif i == '2':
                    board[1].append(player_1)
                elif i == '3':
                    board[2].append(player_1)
                elif i == '4':
                    board[3].append(player_1)
                elif i == 5:
                    board[4].append(player_1)
                elif i == 6:
                    board[5].append(player_1)
                elif i == 7:
                    board[6].append(player_1)
                elif i == 8:
                    board[7].append(player_1)
                elif i == 9:
                    board[8].append(player_1)
                else:
                    print('Enter a location 1-9')
            for i in player_2_location:
                if i == '1':
                    board[0].append(player_2)
                elif i == '2':
                    board[1].append(player_2)
                elif i == 3:
                    board[2].append(player_2)
                elif i == 4:
                    board[3].append(player_2)
                elif i == 5:
                    board[4].append(player_2)
                elif i == 6:
                    board[5].append(player_2)
                elif i == 7:
                    board[6].append(player_2)
                elif i == 8:
                    board[7].append(player_2)
                elif i == 9:
                    board[8].append(player_2)
                else:
                    print('Enter a location 1-9')
            game_board(board)
            # win_check(board,)
            print(player_1_location)
            print(player_2_location)
            if win_check == False:
                not_won = True
                print('Player {} won'.format())
                exit()
            else:
                pass

    def game_board(board):
        print("   |   |   ")
        print(" {} | {} | {}  ".format(board[6], board[7], board[8]))
        print("   |   |   ")
        print('___________')
        print("   |   |   ")
        print(" {} | {} | {}  ".format(board[3], board[4], board[5]))
        print("   |   |   ")
        print('___________')
        print("   |   |   ")
        print(" {} | {} | {}  ".format(board[0], board[1], board[2]))
        print("   |   |   ")

    game_play()


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def game_start():
    print("welcome to tic tac toe")
    player_select()


game_start()
