import random

rows, colums = (4,4)
game_board = [['*'] * colums] * rows


# to do this. create a list of all the taken spaces then check is the space to the left or right or up or down is avalable. If so. move them. 

def up():
  # move all the piece up
  
def down():
  # move all the pieces down
  
def right():
  # move all the pieces right
  
def left():
  # move all the pieces left
  
  
def move():
  # create the random 2 or 4 that spawns every time you
  new_piece = random.randint(0,1)
  print(new_piece)
  
  value = False
  while value ==False:
    value = generate_new_piece(new_piece)
    
  
  
def generate_new_piece(piece_num):
  
  # choose a random place to put it
  random_placex = random.randint(0,3)
  random_placey = random.randint(0,3)
  
  print(random_placex)
  print(random_placey)
  
  print(game_board[random_placex][random_placey])
  
  # if the piece is one and it is free, put a 2. 
  if piece_num == 1:
    if game_board[random_placex][random_placey] == '*':
      game_board[random_placex][random_placey] = 2
  # if the piece is a 0 and it is free, put a 4
  elif piece_num == 0:
    if game_board[random_placex][random_placey] == '*':
      game_board[random_placex][random_placey] = 4
  else:
    return False
  
  return True

print(game_board)
move()
move()
print(game_board)
  
