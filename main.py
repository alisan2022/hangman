import random
import string

from words import words


def get_valid_word(words):

    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        # letters used
        # .join( ["a","b","cd"]) --> "a b cd"
        print("You have guessed these characters:"," ".join(used_letters))
        # what the current word is ( ie W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(word_list)

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You have already guessed that character. Please try again. ")

        else: print("Invalid character. ")
    print(word)


hangman()
