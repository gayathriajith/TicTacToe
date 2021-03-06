
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
    
def win_check(board,mark):
        
    
    for i in range (1,8,3):
        if(board[i]==board[i+1] and board[i+1]==board[i+2] and board[i+2]==mark ):
            check = 'wins'
            print("******************************************************")
            print(f"*** You got an {mark}{mark}{mark} !!!  YOU WON!!!  ***")
            print("******************************************************")
            again = input("Play again? Y to continue and ANY KEY to exit")
            if(again=='Y' or again=='y'):
                start_game()
            else:
                sys.exit("GAME OVER")
            
    
    for i in range (1,4):
        if(board[i]==board[i+3] and board[i+3]==board[i+6] and board[i+6]==mark):
            check = 'wins'
            print("******************************************************")
            print(f"*** You got an {mark}{mark}{mark} !!!  YOU WON!!!  ***")
            print("******************************************************")
            again = input("Play again? Y to continue and ANY KEY to exit")
            if(again=='Y' or again=='y'):
                start_game()
            else:
                sys.exit("GAME OVER")
                
                
            
    if(board[3]==board[5] and board[5]==board[7] and board[7]==mark):
        check = 'wins'
        print("******************************************************")
        print(f"*** You got an {mark}{mark}{mark} !!!  YOU WON!!!  ***")
        print("******************************************************")
        again = input("Play again? Y to continue and ANY KEY to exit")
        if(again=='Y' or again=='y'):
            start_game()
        else:
            sys.exit("GAME OVER")
        
    if(board[1]==board[5] and board[5]==board[9] and board[9]==mark):
        check = 'wins'
        print("******************************************************")
        print(f"*** You got an {mark}{mark}{mark} !!!  YOU WON!!!  ***")
        print("******************************************************")
        again = input("Play again? Y to continue and ANY KEY to exit")
        if(again=='Y' or again=='y'):
            start_game()
        else:
            sys.exit("GAME OVER")
        
def replay(marker,board):
    
    if(full_board_check(board)==True):
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
    
        if play==True and marker=='X':
            playerY(board)
        if play==True and marker=='O':
            playerX(board)
          
    
        
        
def display_board(board):
    print('\n'*100)
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
    return


       
    
def playerX(board):
    
    position=input(" Insert 'X' in : [Choose from position 1 to 9]")
    pos= int(position)
    if(pos not in range(0,10)):
        print("\n\nSorry! You entered wrong position!\n CHOOSE FROM POSITION 1 to 9 ")
        playerX(board)
    marker = 'X'
    if(space_check(board, pos)==True):   
        
        place_marker(board, marker, pos)
    else:
        print("\n\nPosition already filled.")
        playerX(board)
    
  
    
def playerY(board):
    
    position = input(" Insert 'O' in : [Choose from position 1 to 9]")
    pos= int(position)
    if(pos not in range(0,10)):
        print("\n\nSorry! You entered wrong position!\n CHOOSE FROM POSITION 1 to 9 ")
        playerY(board)
    marker='O'
    if(space_check(board, pos)==True):   
        
        place_marker(board, marker, pos)
    else:
        print("\n\nPosition already filled.")
        playerY(board)
    

    
def place_marker(board,marker, position):
    
    
    
    board[position]=marker
    display_board(board)
    win_check(board,marker)

    replay(marker,board)
      

def start_game():
    
    test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']  
    play=None
    empty=None
    display_board(test_board)
    player1 = input("\tPlease pick a marker 'X' or 'O'")
    if(player1=='X'or player1=='x'):
        print("\nPlayer 1 has selected 'X'")
        print("\nPlayer 2 has selected 'O'")
        print("\nPlayer 1 gets the first chance")
        playerX(test_board)
        
        
    if(player1=='O'or player1=='o'):
        print("\nPlayer 1 has selected 'O'")
        print("\nPlayer 2 has selected 'X'")
        print("\nPlayer 1 gets the first chance")
        playerY(test_board)
 
start_game()
