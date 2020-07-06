import random

tries_left = 6

def play():
    words = ["tiger", "elephant", "giraffe", "crocodile", "panda", "monkey", "bear"]
    chosen_word = random.choice(words)
    guessed_letters = [""]
    global tries_left

    word_length = str(len(chosen_word))
    for x in word_length:
        print("The chosen word contains " + x + " letters and the hint is an animal.")
    for x in chosen_word:
        print("_", end ="")

    def get_current_progress(chosen_word, guessed_letters):
        display_string = ""
        for x in chosen_word:
            if x in guessed_letters:
                display_string += x
            else:
                display_string += "_"
        return display_string
        print(display_string)

    output = get_current_progress(chosen_word, guessed_letters)


    while tries_left > 0 and chosen_word != output:
        input_letter = input("\nPick a letter: ")
        input_letter.lower()
        if len(input_letter) != 1:
            print("Please enter a single letter.")
        elif input_letter in guessed_letters:
            print(input_letter + " has already been guessed.")
        elif input_letter not in "abcdefghijklmnopqrstuvwxyz":
            print("Must enter a letter from a to z.")
        else:
            guessed_letters.append(input_letter)

        if input_letter not in chosen_word:
            tries_left -= 1

        output = get_current_progress(chosen_word, guessed_letters)
        print(output)
        print("You have " + str(tries_left) + " guesses left.")

    if output == chosen_word:
        print("\n"+ chosen_word.upper() + " is correct!")
        print("You have successfully guessed the correct word! \nThank you for playing!\n")


    if tries_left == 0:
                print("You ran out of guesses!\n")

while True:
    print("Welcome to Hangman Game!")
    answer = str(input("Do you want to play again, Y/N ?: "))
    answer.lower()
    if answer == "y":
        play()
    elif answer == "n":
        print("Thank you for playing and hope to see you again soon!")
        break
    else:
        print("Please enter either Y or N: ")
