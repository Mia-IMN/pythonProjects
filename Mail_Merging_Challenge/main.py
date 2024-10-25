with open("Input/Letters/starting_letter.txt") as letter_template:
    letter = letter_template.read()

with open("./Input/Names/invitees_names.txt") as names:
    extracted_names = names.readlines()

# names.readlines() - Read each line of file
# names.replace("banana", "apples") - replaces items
# names.strip() - removes spaces

for name in extracted_names:
    invitee = name.strip()
    x = letter.replace("[name]", invitee)
    with open(f"./Output/ReadyToSend/letter_for_{invitee}.txt", mode="w") as file:
        file.write(x)

