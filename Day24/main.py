#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as file:
    names = file.read()
    name_list = names.split()
    # or
    # names = file.readlines()

for name in name_list:
    with open("./Input/Letters/starting_letter.docx") as letter:
        specific_letter = letter.read()
        specific_letter.strip("t")  # to remove any leading or trailing space. input char to strip them off.
        new_letter = specific_letter.replace(PLACEHOLDER, f"{name}")
        with open(f"./Output/ReadyToSend/letter_for_{name}.docx", mode="w") as name_letter:
            name_letter.write(f"{new_letter}")


