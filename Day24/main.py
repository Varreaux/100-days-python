#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Day24/Input/Names/invited_names.txt") as file:
    for name in file.readlines():
        with open("Day24/Input/Letters/starting_letter.txt") as base:
            with open(f"Day24/Output/ReadyToSend/for_{name}.txt", "w") as actual:
                actual.write(base.read().replace("[name]",f"{name.strip()}"))
            