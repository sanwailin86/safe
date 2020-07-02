import random
words = ["tiger", "elephant", "giraffe"]
chosen_word = random.choice(words)
guessed_letters = [""]

word_length = str(len(chosen_word))
for x in word_length:
    print("The chosen word contains " + x + " letters.")

def display_current_progress(chosen_word, guessed_letters):
    display_string = ""
    for x in chosen_word:
        if x in guessed_letters:
            display_string += x
        else:
            display_string += "_"

    return display_string

output = display_current_progress(chosen_word, guessed_letters)

tries = len(chosen_word) + 3

def game_still_going():
    if chosen_word == output:
        print("You have guessed the correct word!")
    elif tries == 0:
        print("You ran out of guesses!")
    else:
        print("You have given " + str(tries) + " guesses.")
game_still_going()

while tries > 0 and chosen_word != output:
    input_letter = input("Pick a letter: ")
    input_letter.lower()
    if len(input_letter) != 1:
        print("Please enter a single letter.")
    elif input_letter in guessed_letters:
        print(input_letter + " has already been guessed.")
    elif input_letter not in "abcdefghijklmnopqrstuvwxyz":
        print("Must enter a letter from a to z.")
    else:
        guessed_letters.append(input_letter)
        tries -= 1

    output = display_current_progress(chosen_word, guessed_letters)
    print(output)
    if output == chosen_word or tries == 0:
        break
    print("You have " + str(tries) + " guess left.")

game_still_going()

Print("Thank you!")



