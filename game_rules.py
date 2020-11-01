from object_classes import Card, Deck, Player

player_one = Player("Pepa")
player_two = Player("Manu")

new_deck = Deck()
new_deck.shuffle()
split_half = int(len(new_deck.all_cards)/2)


game_on = True
round_num = 0
min_cards = 7 # Minimum number of cards to play WAR


for x in range(split_half):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


while game_on:
    round_num += 1
    print(f"Round #{round_num}")

    if len(player_one.all_cards) == 0:
        print(f"Player {player_one.name}, out of cards! PLAYER {player_two.name} WINS!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print(f"Player {player_two.name}, out of cards! PLAYER {player_one.name} WINS!")
        game_on = False
        break

    #Let's start a new round!
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            print(player_one_cards[-1], "is higher than", player_two_cards[-1])
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            print(f"Round for Player {player_one.name}!")
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            print(player_one_cards[-1], "is less than", player_two_cards[-1])
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            print(f"Round for Player {player_two.name}!")
            at_war = False

        else:
            print("War!")

            if len(player_one.all_cards) < min_cards:
                print(f"Player {player_one.name} cannot declare war")
                print(f"PLAYER {player_two.name} WINS!")
                game_on = False
                break

            elif len(player_two.all_cards) < min_cards:
                print(f"Player {player_two.name} cannot declare war")
                print(f"PLAYER {player_one.name} WINS!")
                game_on = False
                break
            
            else:
                for num in range(min_cards):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())