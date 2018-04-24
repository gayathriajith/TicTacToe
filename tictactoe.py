print('Welcome to Tic Tac Toe!')

from IPython.display import clear_output
import sys

def full_board_check(board):
    return (" " not in board)

def space_check(board, position):
    if(board[position]==" "):
        empty=True
    else:
        empty=False
    return empty
    
def win_check(board, mark):
        
    
    for i in range (1,8,3):
        if(board[i]==board[i+1] and board[i+1]==board[i+2] and board[i+2]==mark ):
            check = 'wins'
            print("******************************************************")
            print("*** You got an {mark}{mark}{mark} !!!  YOU WON!!!  ***")
            print("******************************************************")
            sys.exit("GAME OVER!")
            
    
    for i in range (1,4):
        if(board[i]==board[i+3] and board[i+3]==board[i+6] and board[i+6]==mark):
            check = 'wins'
            print("******************************************************")
            print(f"*** You got an {mark}{mark}{mark} !!!  YOU WON!!!  ***")
            print("******************************************************")
            sys.exit("GAME OVER!")
            
    if(board[3]==board[5] and board[5]==board[7] and board[7]==mark):
        check = 'wins'
        print("******************************************************")
        print(f"*** You got an {mark}{mark}{mark} !!!  YOU WON!!!  ***") 
        print("******************************************************")
        sys.exit("GAME OVER!")
        
    if(board[1]==board[5] and board[5]==board[9] and board[9]==mark):
        check = 'wins'
        print("******************************************************")
        print(f"*** You got an {mark}{mark}{mark} !!!  YOU WON!!!  ***")
        print("******************************************************")
        sys.exit("GAME OVER!")
        
def replay(marker,board):
    
    if(full_board_check(test_board)==True):
        sys.exit("GAME OVER!! ITS A TIE!! PLAY AGAIN!! ")
    else:
        yesorno = input("\nKeep Playing? ***[TYPE 'Y' or 'N'] ***")
        if(yesorno=='Y' or yesorno == 'y'):
            play = True
        
        elif(yesorno == 'N' or yesorno== 'n'):
            play = False
            sys.exit(" BYE BYE!")
        else: 
            print("\nTYPE Y to keep playing, N to stop playing!! ")
            replay(marker,board)
    
        if play==True and marker=='\033[1m\033[91mX\033[0m':
            playerY(board)
        if play==True and marker=='\033[1m\033[92mO\033[0m':
            playerX(board)
          
    
        
        
def display_board(board):
    clear_output()
    print(f"-----|-----|-----")
    print(f"     |     |     ")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")    
    print(f"     |     |     ")
    print(f"--7--|--8--|--9--")
    print(f"     |     |     ")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print(f"     |     |     ")
    print(f"--4--|--5--|--6--")
    print(f"     |     |     ")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")
    print(f"     |     |     ")
    print(f"--1--|--2--|--3--")
    
test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']  

       
    
def playerX(board):
    
    position=input(" Insert '\033[1m\033[91mX\033[0m' in : [Choose from position 1 to 9]")
    pos= int(position)
    if(pos not in range(0,10)):
        print("\n\nSorry! You entered wrong position!\n CHOOSE FROM POSITION 1 to 9 ")
        playerX(board)
    #marker X is colored and made bold
    marker = '\033[1m\033[91mX\033[0m'
    if(space_check(board, pos)==True):   
        
        place_marker(marker, pos)
    else:
        print("\n\nPosition already filled.")
        playerX(board)
    
  
    
def playerY(board):
    
    position = input(" Insert '\033[1m\033[92mO\033[0m' in : [Choose from position 1 to 9]")
    pos= int(position)
    if(pos not in range(0,10)):
        print("\n\nSorry! You entered wrong position!\n CHOOSE FROM POSITION 1 to 9 ")
        playerY(board)
    #marker O is colored and made bold
    marker='\033[1m\033[92mO\033[0m'
    if(space_check(board, pos)==True):   
        
        place_marker(marker, pos)
    else:
        print("\n\nPosition already filled.")
        playerY(board)
    

    
def place_marker(marker, position):
    
    
    
    test_board[position]=marker
    display_board(test_board)
    win_check(test_board,marker)

    replay(marker,test_board)
      

    
def start_game():
    
    play=None
    empty=None
    display_board(test_board)
    player1 = input("\tPlease pick a marker '\033[1m\033[91mX\033[0m' or '\033[1m\033[92mO\033[0m'")
    if(player1=='X'or player1=='x'):
        print("\nPlayer 1 has selected '\033[1m\033[91mX\033[0m'")
        print("\nPlayer 2 has selected '\033[1m\033[92mO\033[0m'")
        print("\nPlayer 1 gets the first chance")
        playerX(test_board)
        
        
    if(player1=='y'or player1=='Y'):
        print("\nPlayer 1 has selected '\033[1m\033[92mO\033[0m'")
        print("\nPlayer 2 has selected '\033[1m\033[91mX\033[0m'")
        print("\nPlayer 1 gets the first chance")
        playerY(test_board)
 
