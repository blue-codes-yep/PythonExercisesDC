# Prompt the user for a number
# Compare that number to a number assigned
# If correctly guessed, tell them they are correct
# If guessesed incorrect, tell them they aren't.

user_input = int(input("What number am I thinking of "))

theSpecialNumber = 5

if user_input == theSpecialNumber:
    print("Wow aren't you good at guessing!")
else: 
    print("Incorrect, sorry.")

