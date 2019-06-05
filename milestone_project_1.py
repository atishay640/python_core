# tic tac game



default_status_list = ['0','1','2','3','4','5','6','7','8','9']
actual_status_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player1 = ('')
player2 = ('')
X = ''
O = ''



def create_ui(status_list):
    print('\n')
    print('\n')
    print('        |   |   ')

    print('      {} | {} | {} '.format(status_list[7],status_list[8],status_list[9]))
    print('     ___|___|___')
    print('        |   |   ')

    print('      {} | {} | {} '.format(status_list[4],status_list[5],status_list[6]))
    print('     ___|___|___')
    print('        |   |   ')

    print('      {} | {} | {} '.format(status_list[1],status_list[2],status_list[3]))
    print('        |   |   ')


def choose_x_o():
    print('\n')
    print('\n')
    print('\n')
    print("You are Player 1:\n")
    print("What do you want to choose from 'O' or 'X' ??? (Type 'O' or 'X' and hit Enter)\n\n")
    print('Type Below :')
    global player1
    global player2
    global O
    global X


    player1 = input()
    if player1 != '' and player1 != None and 'X' == player1.upper() or 'O' == player1.upper():
        if 'X' == player1.upper():
            X = 'Player-1'
            O = 'Player-2'
        elif 'O' == player1.upper():
            O = 'Player-1'
            X = 'Player-2'

        print("\n Player1 : -> {}".format(player1) )
        if player1 == 'X':
            player2 = 'O'
            print("\n Player2 : -> {}".format(player2) )
        elif  player1 == 'O':
            player2 = 'X';
            print("\n Player2 : -> {}".format(player2) )

    else:
        print("Choose either 'O' or 'X' ")

def start_player_moves():
    status = None
    while status != 'WIN':
        try:
            print("------------ Basic Matrix coordinates ----------")
            create_ui(default_status_list)
            print("\n")
            print(" Player1 move ({}):\n".format(player1) )
            value = int(input())
            actual_status_list[value] = player1
            print('\n\n')
            create_ui(actual_status_list)
            print("------------------------------------------------")
            player1_status = track_winner(player1)
            if player1_status[1] == 'WIN':
                status = player1_status[1]
                declare_winner(player1_status[0])
                break
            elif player1_status[1] == 'TIE':
                declare_tie()
                break


            create_ui(default_status_list)
            print("\n")
            print(" Player2 move ({}):\n".format(player2) )
            value = int(input())
            actual_status_list[value] = player2
            print('\n\n')
            create_ui(actual_status_list)
            print("------------------------------------------------")
            player2_status = track_winner(player2)
            if player2_status[1] == 'WIN':
                status = player2_status[1]
                declare_winner(player2_status[0])
                break
            elif player2_status[1] == 'TIE':
                declare_tie()
                break
        except ValueError:
            print('value error')


def track_winner(player):
    status = None
    if (actual_status_list[7] == player and actual_status_list[8] == player and actual_status_list[9] == player):
        status = 'WIN'
    elif (actual_status_list[4] == player and actual_status_list[5] == player and actual_status_list[6] == player):
        status = 'WIN'
    elif (actual_status_list[1] == player and actual_status_list[2] == player and actual_status_list[3] == player):
        status = 'WIN'
    elif (actual_status_list[7] == player and actual_status_list[4] == player and actual_status_list[1] == player):
        status = 'WIN'
    elif (actual_status_list[8] == player and actual_status_list[5] == player and actual_status_list[2] == player):
        status = 'WIN'
    elif (actual_status_list[9] == player and actual_status_list[6] == player and actual_status_list[3] == player):
        status = 'WIN'
    elif (actual_status_list[7] == player and actual_status_list[5] == player and actual_status_list[3] == player):
        status = 'WIN'
    elif (actual_status_list[9] == player and actual_status_list[5] == player and actual_status_list[1] == player):
        status = 'WIN'
    elif ' ' not in actual_status_list:
        status = "TIE"

    return (player,status)


def declare_winner(player):
    print("$$$$$$$$$$$$$$$$$$ ************************* $$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$ **** Congratulations **** $$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$ ************************* $$$$$$$$$$$$$$$$$$$$\n")

    if player == 'O':
        print("WINNER : -> "+ O )
    elif player == 'X':
        print("WINNER : -> "+ X )

def declare_tie():
    print("\n#################### ***************** #######################")
    print("##################### **** IT'S TIE**** #######################")
    print("##################### ***************** #######################")



def start():
    print('\n \n----@ TIC-TAC-TOE GAME @----')
    create_ui(default_status_list)
    choose_x_o()
    start_player_moves()


start()
