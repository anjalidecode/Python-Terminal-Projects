import random

cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]  # 10 = J, Q, K

print("♣️ Welcome to Baby Blackjack ♣️")

# Deal initial cards
player_cards = [random.choice(cards), random.choice(cards)]
dealer_cards = [random.choice(cards), random.choice(cards)]

player_total = sum(player_cards)
dealer_total = sum(dealer_cards)

print("\nYour cards:", player_cards, "Total:", player_total)
print("Dealer shows:", dealer_cards[0])

# Player turn
while player_total < 21:
    choice = input("Do you want to HIT or STAND? ").lower()

    if choice == "hit":
        card = random.choice(cards)
        player_cards.append(card)
        player_total += card
        print("You got:", card)
        print("Your total:", player_total)

        if player_total > 21:
            print("❌ You BUSTED! Dealer wins.")
            exit()

    elif choice == "stand":
        break
    else:
        print("Invalid choice. Type HIT or STAND.")

# Dealer turn
print("\nDealer's cards:", dealer_cards, "Total:", dealer_total)

while dealer_total < 17:
    card = random.choice(cards)
    dealer_cards.append(card)
    dealer_total += card

print("Dealer final cards:", dealer_cards, "Total:", dealer_total)

# Decide winner
if dealer_total > 21:
    print("🎉 Dealer busted! You win!")
elif player_total > dealer_total:
    print("🎉 You win!")
elif dealer_total > player_total:
    print("😞 Dealer wins!")
else:
    print("🤝 It's a draw!")
