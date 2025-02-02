from random import choice

def check_hand(hand_total, eleven):
    while hand_total>21:
        if eleven>0:
            eleven-=1
            hand_total-=10
        else:
            break
    return hand_total, eleven

print("Welcome to blackjack")
deck = ["A",2,3,4,5,6,7,8,9,10,10,10,10]
hand = []
eleven = 0
your_hand_total =0
for i in range(2):
    card = choice(deck)
    if card == 'A':
        your_hand_total +=11
        eleven+=1
    else:
        your_hand_total += card
    hand.append(card)
    your_hand_total, eleven = check_hand(your_hand_total,eleven)

card = choice(deck)
dealer_hand1 = [card]
if card == "A":
    dealer_total = 11
else:
    dealer_total = card

print(f"This is your hand: {hand}\t (total: {your_hand_total})")
print(f"The dealer has: {dealer_hand1}")

another_card = input("Would you like another card? (y/n) ").lower()
print("\n" * 50)

while another_card in ['y', 'yes', 'ye', 'ya']:
    print("\n"*50)
    card = choice(deck)
    hand.append(card)
    if card == "A":
        eleven += 1
        your_hand_total += 11
    else:
        your_hand_total += card
    your_hand_total, eleven = check_hand(your_hand_total, eleven)
    if your_hand_total > 21:
        print(f"Your hand: {hand}\nBUST! your total is {your_hand_total}")
        exit()

    print(f"This is your hand: {hand}\t (total: {your_hand_total})")
    print(f"The dealer has: {dealer_hand1}")
    another_card = input("Would you like another card? (y/n) ").lower()
    print("\n" * 50)

if dealer_total == 11:
    eleven = 1
else:
    eleven = 0

while dealer_total <17:
    card = choice(deck)
    if card == "A":
        eleven+=1
        dealer_total+=11
    else:
        dealer_total+=card
    dealer_hand1.append(card)
    dealer_total, eleven = check_hand(dealer_total, eleven)
    if dealer_total > 21:
        print(f"Dealer's hand: {dealer_hand1}\nBUST! their total is {dealer_total}")
        exit()

print(f"Your hand: {hand} (total: {your_hand_total})\n"
      f"Dealer's hand: {dealer_hand1} (total: {dealer_total})\n")

if your_hand_total > dealer_total:
    print("You win!")
elif your_hand_total == dealer_total:
    print("Same score...PUSH!")
else:
    print("Sorry, dealer wins :)")
