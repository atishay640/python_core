'''
Root file of game
'''
from milestone_project_2.pages import splash
from milestone_project_2.classes import bank_
from milestone_project_2.classes import card_
import random

list_of_cards =[]
game_status_dic = {}
random_cards_list =[]

def generate_deck():
    for num in range(2,11):
        card = card_.Card(name='number', points=num, color='Black', category='Pikes')
        list_of_cards.append(card)
        card = card_.Card(name='number', points=num, color='Black', category='Clovers')
        list_of_cards.append(card)
        card = card_.Card(name='number', points=num, color='Red', category='Tiles')
        list_of_cards.append(card)
        card = card_.Card(name='number', points=num, color='Red', category='Hearts')
        list_of_cards.append(card)

    card = card_.Card(name='Jack', points=10, color='Black', category='Pikes')
    list_of_cards.append(card)
    card = card_.Card(name='Jack', points=10, color='Black', category='Clovers')
    list_of_cards.append(card)
    card = card_.Card(name='Jack', points=10, color='Red', category='Tiles')
    list_of_cards.append(card)
    card = card_.Card(name='Jack', points=10, color='Red', category='Hearts')
    list_of_cards.append(card)

    card = card_.Card(name='Queen', points=10, color='Black', category='Pikes')
    list_of_cards.append(card)
    card = card_.Card(name='Queen', points=10, color='Black', category='Clovers')
    list_of_cards.append(card)
    card = card_.Card(name='Queen', points=10, color='Red', category='Tiles')
    list_of_cards.append(card)
    card = card_.Card(name='Queen', points=10, color='Red', category='Hearts')
    list_of_cards.append(card)

    card = card_.Card(name='King', points=10, color='Black', category='Pikes')
    list_of_cards.append(card)
    card = card_.Card(name='King', points=10, color='Black', category='Clovers')
    list_of_cards.append(card)
    card = card_.Card(name='King', points=10, color='Red', category='Tiles')
    list_of_cards.append(card)
    card = card_.Card(name='King', points=10, color='Red', category='Hearts')
    list_of_cards.append(card)

    card = card_.Card(name='Ace', points=(1, 11), color='Black', category='Pikes')
    list_of_cards.append(card)
    card = card_.Card(name='Ace', points=(1, 11), color='Black', category='Clovers')
    list_of_cards.append(card)
    card = card_.Card(name='Ace', points=(1, 11), color='Red', category='Tiles')
    list_of_cards.append(card)
    card = card_.Card(name='Ace', points=(1, 11), color='Red', category='Hearts')
    list_of_cards.append(card)



def start(game_status_dic):
    splash.do_play(game_status_dic)
    action(game_status_dic)


def action(game_status_dic):
    count = 0
    status = None
    player_score = 0
    dealer_score = 0
    splash.print_card('DEALER',random_cards_list[count])

    if isinstance( random_cards_list[count].points , tuple ):
        if dealer_score + 11 <= 21:
            dealer_score += random_cards_list[count].points[1]
        else:
            dealer_score += random_cards_list[count].points[0]
    else:
        dealer_score += random_cards_list[count].points

    count = count +1

    splash.print_card('DEALER',random_cards_list[count])

    if isinstance( random_cards_list[count].points , tuple ):
        if dealer_score + 11 <= 21:
            dealer_score += random_cards_list[count].points[1]
        else:
            dealer_score += random_cards_list[count].points[0]
    else:
        dealer_score += random_cards_list[count].points

    count = count +1

    splash.print_card('PLAYER',random_cards_list[count])

    if isinstance(random_cards_list[count].points , tuple ):
        if player_score + 11 <= 21:
            player_score += random_cards_list[count].points[1]
        else:
            player_score += random_cards_list[count].points[0]
    else:
        player_score += random_cards_list[count].points

    count = count +1

    splash.print_card('PLAYER',random_cards_list[count])

    if isinstance( random_cards_list[count].points , tuple ):
        if player_score + 11 <= 21:
            player_score += random_cards_list[count].points[1]
        else:
            player_score += random_cards_list[count].points[0]
    else:
        player_score += random_cards_list[count].points

    splash.print_scores(player_score,dealer_score)

    if is_blackjack(player_score):
        splash.declare_results('BlackJack','PLAYER')
        game_status_dic['bank'] = game_status_dic['bank'].credit()
        return 0
    elif is_blackjack(dealer_score):
        splash.declare_results('BlackJack','DEALER')
        return 0


    while (status != 'Blackjack'  or  status != 'Bust!' or status != 'Winner'):

        response = splash.ask_for_stand_or_hit()
        if response == 'Hit':
            count += 1
            splash.print_card('PLAYER',random_cards_list[count])
            if isinstance( random_cards_list[count].points , tuple ):
                if player_score + 11 <= 21:
                    player_score += random_cards_list[count].points[1]
                else:
                    player_score += random_cards_list[count].points[0]
            else:
                player_score += random_cards_list[count].points
            splash.print_scores(player_score,dealer_score)

            if is_bust(player_score):
                splash.declare_results('Bust!','PLAYER')
                status = 'Bust!'
                splash.print_scores(player_score,dealer_score)
                return 0

        elif response == 'Stand':
            if dealer_score > player_score:
                splash.declare_results('Winner','DEALER')
                splash.print_scores(player_score,dealer_score)
                return 0

            count += 1
            splash.print_card('DEALER',random_cards_list[count])
            if isinstance( random_cards_list[count].points , tuple ):
                if dealer_score + 11 <= 21:
                    dealer_score += random_cards_list[count].points[1]
                else:
                    dealer_score += random_cards_list[count].points[0]
            else:
                dealer_score += random_cards_list[count].points

            splash.print_scores(player_score,dealer_score)

            if is_bust(dealer_score):
                splash.declare_results('Bust!','DEALER')
                status = 'Bust!'
                splash.print_scores(player_score,dealer_score)
                credit_player_balance()
                return 0

            if dealer_score > player_score:
                splash.declare_results('Winner','DEALER')
                status = 'Winner'
                splash.print_scores(player_score,dealer_score)
                return 0



def initialize():
    generate_deck()
    game_status_dic['bank'] = bank_.Bank(balance=10000)
    game_status_dic['cards'] =  len(list_of_cards)
    generate_random_cards()

def generate_random_cards():
    random_cards_list.clear()
    indices = random.sample(range(0,52),15)
    for ran_num in indices:
        random_cards_list.append(list_of_cards[ran_num])

def is_blackjack(score):
    if score == 21:
        return True

def is_bust(score):
    if score > 21:
        return True

def next():
    game_status_dic['cards'] = 0
    game_status_dic['cards'] =  len(list_of_cards)
    generate_random_cards()
    splash.bid_amount(game_status_dic)
    action(game_status_dic)

def credit_player_balance():
    bank = game_status_dic['bank']
    amount = game_status_dic['amount']
    bank.credit(amount*2)
    game_status_dic['bank'] = bank
    splash.twice_credited(bank.balance,amount*2)


def play():
    initialize()
    start(game_status_dic)
    while(game_status_dic['bank'].balance > 0):
        next()
    else:
        splash.print_lost_balance()




