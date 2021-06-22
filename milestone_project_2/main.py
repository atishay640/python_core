'''
Milestone Project 2 - Blackjack Game
'''

# Number Cards :-> 1,2,3,4,5,6,7,8,9,10.
# king, queen, jack :-> 10 each
# Ace :-> 1 or 11 (your choice)

# Game will be played between 'Dealer' and 'Player'
# Player will have $1000 in their bank which can be used when 'Deal'

#RULES:
# 1. Each player'Dealer' and 'Player' will have 2 cards each.
# 2. Dealer's 1 card will be hidden.
# 3. If anyone of them will have scored 21 initailly when both of them having 2 cards. The played will be treated as 'Blackjack'
# 4. In both the players, if any player exceed score more than 21 will be treated as 'Bust!' and the other one will 'winner'
# 5. 'Player' have two options either 'Stand' or 'Hit'
# 6. 'Stand' :-> 'Player' don't want to add more cards. In this case 'Dealer' can 'Hit' as many cards as he reached the total score more then the 'Player'.
# 7. 'Hit' :->  If 'Player' click hit a new card will be added. 'Player' can hit 'Hit' as many time until the score goes to 21 or more then the 'Dealer'.
# 8. Total cards for playing will be '52' or a deck of cards.
# 9. once any player's score total reached to 21. another player can hit cards.
# 10. If during the game bank balance reached $0 then 'Dealer' will win the whole game. and 'Player' lost their invested Monney.

from milestone_project_2.classes import black_jack

if __name__ == '__main__':
    black_jack.play()
