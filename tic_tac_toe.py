import sys
from random import randint

#data
board=[0,0,0,0,0,0,0,0,0]
#functions
def instruction():
    print("Witaj w grze Kółko i Krzyżyk\nJesteś graczem nr 1, plansza wygląda następująco\n")
    print(" {} {} {} \n {} {} {} \n {} {} {}".format(1,2,3,4,5,6,7,8,9))
def player_move():
    print("Twój Ruch\nPodaj numer pola")
    pc=int(input(":"))
    if (board[pc-1]==0):
        #print("Mój ruch")
        return pc-1
    else:
        print("Zły ruch")
        show_board()
        player_move()
def computer_move():
    pcmv = int(randint(0,8))
    if(board[pcmv]==0):
	       return pcmv
    else:
	       computer_move()

def show_board():
    print(" {} {} {} \n {} {} {} \n {} {} {}".format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]))

def game_end():
    print("Mamy nadzieję że jeszcze wrócisz ...\n")
    sys.exit(0)

def win_check():
    if (((board[0]==1)and(board[1]==1)and(board[2]==1))or((board[3]==1)and(board[4]==1)and(board[5]==1))or((board[6]==1)and(board[7]==1)and(board[8]==1))):
        print("Wygrałeś\aś !!!")
        game_end()
    elif (((board[0]==2)and(board[1]==2)and(board[2]==2))or((board[3]==2)and(board[4]==2)and(board[5]==2))or((board[6]==2)and(board[7]==2)and(board[8]==2))):
        print("Przegrałeś\\aś :(")
        game_end()
    elif (((board[0]==1)and(board[3]==1)and(board[6]==1))or((board[1]==1)and(board[4]==1)and(board[7]==1))or((board[2]==1)and(board[5]==1)and(board[8]==1))):
        print("Wygrałeś\aś !!!")
        game_end()
    elif (((board[0]==2)and(board[3]==2)and(board[6]==2))or((board[1]==2)and(board[4]==2)and(board[7]==2))or((board[2]==2)and(board[5]==2)and(board[8]==2))):
        print("Przegrałeś\\aś :(")
        game_end()
    elif (((board[0]==1)and(board[4]==1)and(board[8]==1))or((board[2]==1)and(board[4]==1)and(board[6]==1))):
        print("Wygrałeś\aś !!!")
        game_end()
    elif (((board[0]==2)and(board[4]==2)and(board[8]==2))or((board[2]==2)and(board[4]==2)and(board[6]==2))):
        print("Przegrałeś\\aś :(")
        game_end()


#working program below
instruction()
for x in range(0,8):
    print("Tura nr: ",x+1)
    mv_h=0
    mv_h=player_move()
    if not(0 in board):
        print("Koniec gry")
        break
    board[mv_h]=1
    #show_board()
    win_check()
    print("Ruch Komputera")
    mv_pc=0
    mv_pc=computer_move()
    if not(0 in board):
        print("Koniec gry")
        break
    board[mv_pc]=2
    show_board()
    win_check()

game_end()
