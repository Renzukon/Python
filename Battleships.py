# Python
from random import randint

board = []

#Sets up the board as a 5x5 with O's
for x in range(5):
  board.append(["O"] * 5)

#Combines the O's and X's from the board to make a "map"
def print_board(board): 
  for row in board:       
    print " ".join(row)
    
print "Let's play Battleship!"
print_board(board)

#Randomizes the values for the battle ship
def random_row(board): 
  return randint(0, len(board) - 1)
def random_col(board):
  return randint(0, len(board[0]) - 1)
  
#Assigns the values to the board 
ship_row = random_row(board)
ship_col = random_col(board)

#loops for 4 turns
for turn in range(4):  
  #Ends game if used up all guesses
  if turn == 3:        
  print "Game Over"  
  
  #Asks user for Input
  guess_row = int(raw_input("Guess Row:"))   
  guess_col = int(raw_input("Guess Col:"))    
  
  #Condition to check if correct guess
  if guess_row == ship_row and guess_col == ship_col:        
    print "Congratulations! You sunk my battleship!"      
    break;   
  else:  
    #checks if user guesses out of bounds     
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):         
      print "Oops, that's not even in the ocean."
    #Checks if user has already guessed same input  
    elif(board[guess_row][guess_col] == "X"):        
      print "You guessed that one already."       
    else:       
      #Sets X to incorrect guess
      print "You missed my battleship!"        
      board[guess_row][guess_col] = "X"  
  #Print statement to reprint board and turn for player
  print "Turn", turn + 1       
  print_board(board)
