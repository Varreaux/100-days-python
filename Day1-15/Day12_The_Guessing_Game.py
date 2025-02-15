from Day12_art import logo
from random import randint

print(logo)
print("Welcome to the number guessing game! :)\n"
    "I'm thinking of a number between 1 and 100.")

solution = randint(1,100)
print(f"Dev hack lol -- the solution is: {solution}")

def get_attemps():
    difficulty = input("Please choose your difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        print("Incorrect input. Try again...")
        return get_attemps()

def check_guess(guess):
    if guess > solution:
        print("Too high")
    elif guess < solution:
        print("Too low")
    else:
        print(f"You got it! The answer was {solution}.")
        exit()

def get_guess():
    user_input = input("Please make a guess: ")
    if user_input.isdigit():
        return int(user_input)
    else:
        print("bro...it's gotta be a number...try again.")
        return get_guess()

attemps = get_attemps()

while(True):
    check_guess(get_guess())
    attemps-=1
    if(attemps == 0):
        print("You've run out of guesses, you lose -- no worries though, you can try again as much as you want :)")
        exit()
    else:
        print("Guess again.\n")
        if attemps > 1:
            print(f"You have {attemps} chances remaining to guess the number")
        else:
            print(f"You have {attemps} chance remaining to guess the number")

        
