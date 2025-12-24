import random

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]  # 11 = Ace

def calculate_total(hand):
    total = sum(hand)
    ace_count = hand.count(11)

    while total > 21 and ace_count > 0:
        total -= 10   # Convert Ace from 11 to 1
        ace_count -= 1

    return total


print("♠️ Welcome to Blackjack ♠️")

# Deal initial cards
player_cards = [random.choice(cards), random.choice(cards)]
dealer_cards = [random.choice(cards), random.choice(cards)]

# Player turn
while True:
    player_total = calculate_total(player_cards)
    print("\nYour cards:", player_cards, "Total:", player_total)
    print("Dealer shows:", dealer_cards[0])

    if player_total == 21:
        print("🎉 BLACKJACK! You win!")
        exit()

    if player_total > 21:
        print("❌ You busted! Dealer wins.")
        exit()

    choice = input("HIT or STAND? ").lower()

    if choice == "hit":
        player_cards.append(random.choice(cards))
    elif choice == "stand":
        break
    else:
        print("Invalid choice.")

# Dealer turn
print("\nDealer's cards:", dealer_cards)

while calculate_total(dealer_cards) < 17:
    dealer_cards.append(random.choice(cards))

dealer_total = calculate_total(dealer_cards)
player_total = calculate_total(player_cards)

print("Dealer final cards:", dealer_cards, "Total:", dealer_total)

# Decide winner
if dealer_total > 21:
    print("🎉 Dealer busted! You win!")
elif dealer_total > player_total:
    print("😞 Dealer wins.")
elif dealer_total < player_total:
    print("🎉 You win!")
else:
    print("🤝 It's a draw!")
