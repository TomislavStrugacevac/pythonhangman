import random
import sys

word_list = ["Tree", "Car", "Book", "Dog", "Cat", "House", "Chair", "Mountain", "Ocean", "Sun", "Moon", "Star",
             "Flower", "River", "Bird", "Computer", "Table", "Lamp", "Phone", "Pizza"]

chosen_word = (random.choice(word_list)).lower()
word_length = len(chosen_word)
guessed_word_one = ["_" for _ in range(word_length)]
guessed_word = "".join(guessed_word_one)
attempt_number = 0


def find_letters(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def hangman(guess_the_word):
    global attempt_number
    global guessed_word

    print("The current word is", guess_the_word)
    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter in chosen_word:
        indexes = find_letters(chosen_word, guessed_letter)
        # print(indexes)

        for i in indexes:
            guessed_word_one[i] = guessed_letter
        guessed_word = "".join(guessed_word_one)
        gallows(attempt_number)
        print("")
        print(guessed_word)

        if "_" not in guessed_word:
            print("YOU WIN!")
        else:
            hangman(guessed_word)

    else:
        print("That letter is not in the word")
        attempt_number += 1
        gallows(attempt_number)

        hangman(guess_the_word)


def gallows(i):
    if i == 0:
        next()
    elif i == 1:
        print("       /")
    elif i == 2:
        print("       / \\")
    elif i == 3:
        print("       /|\\")
    elif i == 4:
        print("        | ")
        print("       /|\\")
    elif i == 5:
        print("        | ")
        print("        | ")
        print("       /|\\")
    elif i == 6:
        print("        \\ ")
        print("        | ")
        print("        | ")
        print("       /|\\")
    elif i == 7:
        print("   _____  ")
        print("        \\ ")
        print("        | ")
        print("        | ")
        print("       /|\\")
    elif i == 8:
        print("   _____  ")
        print("  0     \\ ")
        print("        | ")
        print("        | ")
        print("       /|\\")
    elif i == 9:
        print("   _____  ")
        print("  0     \\ ")
        print("  |     | ")
        print("        | ")
        print("       /|\\")
    elif i == 10:
        print("   _____  ")
        print("  0     \\ ")
        print(" /|     | ")
        print("        | ")
        print("       /|\\")
    elif i == 11:
        print("   _____  ")
        print("  0     \\ ")
        print(" /|\\    | ")
        print("        | ")
        print("       /|\\")
    elif i == 12:
        print("   _____  ")
        print("  0     \\ ")
        print(" /|\\    | ")
        print(" /      | ")
        print("       /|\\")
    elif i == 13:
        print("   _____  ")
        print("  0     \\ ")
        print(" /|\\    | ")
        print(" / \\    | ")
        print("       /|\\")
        print("YOU LOSE!!!!")
        sys.exit(0)


hangman(guessed_word)
