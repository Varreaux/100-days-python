student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("Day26/nato_phonetic_alphabet.csv")
temp = {row.letter:row.code for (index, row) in df.iterrows()}
print(temp)
print("\n\n\n")

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input = input("give me a name please\n")
answer = [temp[a.upper()] for a in input]
print(f"The word is 'Morgan':\n{answer}")
