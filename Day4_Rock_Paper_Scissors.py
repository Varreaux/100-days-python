rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
hands = [rock, paper, scissors]
hand = int(input("Choose your hand. 0 = rock, 1 = paper, 2 = scissors\n"))
if hand>2 or hand<0:
    print("You typed in an invalid number. You lose.")
    exit()
print(f"Your hand:\n{hands[hand]}")
comp_hand = random.randint(0, 2)
print(f"The computer's hand:\n{hands[comp_hand]}")

if hand==2 and comp_hand == 0:
    print("you lose:(")
elif hand==0 and comp_hand == 2 or hand > comp_hand:
    print("you win!")
elif hand == comp_hand:
    print("draw, go again.")
else:
    print("you lose:(")


