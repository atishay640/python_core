'''
Splash
'''

def do_play(game_status_dic):
    response = wanna_play()
    bid_amount(game_status_dic)

def wanna_play():
    print('---------------------------------------')
    print('---------------------------------------')
    print('---------------------------------------')
    print('------------{}------------------'.format('B-L-A-C-K'))
    print('------------{}--------------------'.format('J-A-C-K'))
    print('---------------------------------------')
    print('---------------------------------------')
    print('---------------------------------------')
    response = input("\t\tLet's Play ? (Y/n)\n")
    return response

def bid_amount(game_status_dic):
    bank =  game_status_dic['bank']
    print('###################{}###################'.format('--PLAYER--'))
    print('-----------------------------------------')
    print('--------------{} = ${}----------------'.format('Bank',bank.balance))
    print('-----------------------------------------')
    print('--------------{} = {}----------------'.format('Cards',game_status_dic['cards']))
    print('-----------------------------------------')
    print('-----------------------------------------')
    response = input("\t\tEnter Deal Amount ($) \n")
    print(int(response))
    amount = int(response)
    game_status_dic['amount'] = amount
    bank.debit(amount)
    game_status_dic['bank'] = bank
    print('###################{}###################'.format('--PLAYER--'))
    print('-----------------------------------------')
    game_status_dic['cards'] = game_status_dic['cards'] - 4

    print('--------------{} = ${}----------------'.format('Bank',bank.balance))
    print('-----------------------------------------')
    print('--------------{} = {}----------------'.format('Cards',game_status_dic['cards']))
    print('-----------------------------------------')
    print('--------------{} = ${}---------------'.format('Amount',game_status_dic['amount']))
    print('-----------------------------------------')
    print('-----------------------------------------')


def print_card(player,ran_card):
    print('-------------------------------------------------------------------------')
    print('-------------------------------|{}|---------------------------------'.format(player))
    print('-------------------------------------------------------------------------')

    print('\t\t\t\t\t\t\t|\t{}\t|'.format(ran_card.name))
    print('\t\t\t\t\t\t\t|\t\t\t|')
    print('\t\t\t\t\t\t\t|\t{}\t|'.format(ran_card.category))
    print('\t\t\t\t\t\t\t|\t\t\t|')
    print('\t\t\t\t\t\t\t|\t{}\t\t|'.format(ran_card.points))
    print('\t\t\t\t\t\t\t|\t\t\t|')
    print('\t\t\t\t\t\t\t|\t{}\t|'.format(ran_card.color))
    print('\t\t\t\t\t\t\t|\t\t\t|')

def print_scores(player_score,dealer_score):
    print('\n##################################################################')
    print('###################### Dealer score = {} ########################'.format(dealer_score))
    print('###################### Player score = {} ########################'.format(player_score))
    print('##################################################################\n')

def ask_for_stand_or_hit():
    response = input("\nPress 'S' for 'Stand' or Press 'H' for 'Hit' \n")
    if response.upper() == 'H':
        return  'Hit'
    elif response.upper() == 'S':
        return 'Stand'
    else:
        return 'Other'

def declare_results(result, player):
    print('\n##################################################################')
    print('%%%%%%%%%%%%%%%%%%%%% {} = {} %%%%%%%%%%%%%%%%%%%%%%%'.format(player, result))
    print('##################################################################\n')

def print_lost_balance():
    print('\n\n((((((((((((((((-------------------------------------------))))))))))))))))))')
    print('((((((((((((((((:: SORRY YOU HAVE LOST FULL BANK BALANCE  ::))))))))))))))))))')
    print('((((((((((((((((-------------------------------------------))))))))))))))))))')


def twice_credited(balance , amount):
    print('\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(' $$$$$$$$$$$$$$$$$$$$$$$$$$ Amount Credited  = {} $$$$$$$$$$$$$$$$$$$$$$$$$$$$$'.format(amount))
    print(' $$$$$$$$$$$$$$$$$$$$$$$$$$ Updated bank balance  = {} $$$$$$$$$$$$$$$$$$$$$$$$'.format(balance))
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n')
