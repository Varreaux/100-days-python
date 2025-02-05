from Day14_art import logo, vs
from Day14_data import data
from random import randint
print(logo)

used_indexes = []
current_score = 0
def get_new_person(index_a):
    index_b = randint(0, len(data)-1)
    if index_a == "":
        index_a = randint(0, len(data)-1)
        while index_a == index_b:
            index_a = randint(0, len(data) - 1)
        used_indexes.extend([index_a, index_b])
        return data[index_a], data[index_b]
    else:
        while index_b in used_indexes:
            index_b = randint(0, len(data) - 1)
        used_indexes.append(index_b)
        return index_a, data[index_b]


def get_solution(a, b):
    if a['follower_count']>b['follower_count']:
        return "A", a
    else:
        return "B", b


person = ""
while True:
    person_a, person_b = get_new_person(person)
    solution, person = get_solution(person_a, person_b)
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}, hack {person_a['follower_count']}.")
    print(vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}, hack {person_b['follower_count']}.")

    A_or_B = input("Who has more followers? Type 'A' or 'B': ").upper()
    while A_or_B not in ["A","B"]:
        print("Not a valid answer, try again..")
        A_or_B = input("Who has more followers? Type 'A' or 'B': ").upper()

    print("\n"*50,
          logo)

    if solution == A_or_B:
        current_score+=1
        if current_score == len(data)-1:
            print(f"You're right and you reached the max score of {current_score}! Game Over, congrats!")
            exit()
        print(f"You're right! Current score: {current_score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}.")
        exit()