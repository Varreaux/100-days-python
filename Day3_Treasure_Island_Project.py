print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

cross = input("You find yourself at a crossroad, do you take the scary pass or the normal one?\n")
if cross in ['N','n', "Normal","normal"]: print("Ok, you proceed normally :)")
else:
    print("sorry you made the irrational choice, you lose")
    exit()

swim = input("You are trying to get to an island: take the boat or swim?\n")
if swim in ['b','B',"Boat","boat"]: print("You are of sound mind :) you get to the island no problem")
else:
    print("Why would you swim? makes no sense. Troubled waters, you need to double back. Game over.")
    exit()

door = input("You are faced with 3 doors. Yellow, Blue, Red. Which one do you pick?\n")
if door in ['Y',"Yellow"]: print("Congrats you win!")
else: print("Sorry wrong door. Game over.")