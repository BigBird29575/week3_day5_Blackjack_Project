import random

PlayerAction = True
DealerAction = True


# deck of cards dealer hands

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 
        2, 3, 4, 5, 6, 7, 8, 9, 10, 
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        "J", "Q", "K", "A",
        "J", "Q", "K", "A",
        "J", "Q", "K", "A",
        "J", "Q", "K", "A"
        ]


player_cards = []

dealer_cards = []




# function to deal the cards

def shuffle_and_deal(player_turn):
    card = random.choice(deck)
    player_turn.append(card)
    deck.remove(card)




# calculate the total of each of hand

def sum(player_turn):
    sum = 0
    face = ['A', 'J', 'Q', 'K']
    for card in player_turn:
        if card in range(1,11):
            sum += card
        elif card in face:
            sum += 10
        else:
            if sum > 11:
                sum += 1
            else:
                sum += 11
    return sum




# check for winner

def show_dealer_cards():
    if len(dealer_cards) == 2:
        return dealer_cards[0]
    elif len(dealer_cards) > 2:
        return dealer_cards[0], dealer_cards[1]




# game loop

for x in range(2):
    shuffle_and_deal(player_cards)
    shuffle_and_deal(dealer_cards)

while PlayerAction or DealerAction:
    print(f"\n\nHouse draws    {show_dealer_cards()} and X")
    print(f"You draw      {player_cards}")
          
    if PlayerAction:
        stayorhit = input ("\n1: Stay\n2: Hit\n")
    if sum(dealer_cards) > 16:
        DealerAction = False
    else:
        shuffle_and_deal(dealer_cards)
    if stayorhit == '1':
        PlayerAction = False
    else:
        shuffle_and_deal(player_cards)
    if sum(player_cards) >= 21:
        break
    elif sum(dealer_cards) >= 21:
        break


if sum(player_cards) == 21:
    print(f"\n\nBlackjack You win with {sum(player_cards)}! House loses at {sum(dealer_cards)}")
elif sum(dealer_cards) == 21:
    print(f"{sum(player_cards)}\nYou lost.......wow. Jeez what a loser.\n\n House wins again with {sum(dealer_cards)}")
elif sum(player_cards) > 21:
    print(f"\nYou have {sum(player_cards)} for a total of {sum(player_cards)}")
    print(f"You busted all over the table. House wins again with {sum(dealer_cards)} now has to clean up your duck sauce.")
elif sum(dealer_cards) > 21:
    print(f"\nYou have {sum(player_cards)} for a total of {sum(player_cards)}")
    print(f"Blackjack!")
elif sum(dealer_cards) < 21:
    print(f"You win. You have {sum(player_cards)}, House Busts, they have accused you of cheating and want blood.")
elif sum(player_cards) < 21:
    print((f"\nYou bust at {sum(player_cards)}. You bet your family home on this bet and lost. What a chump! House rains Duck Sauce on you with {sum(dealer_cards)} No more credit!"))
print(player_cards)
print(dealer_cards)
 