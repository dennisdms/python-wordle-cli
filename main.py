import sys
import argparse
import random
import math

def main(wordle, attempts, dictionary):
    if wordle is None:
        wordle = 'xxxxx'
    if attempts is None:
        attempts = 6
    # Load dictionary and and create valid words list based on wordle length
    valid_words = []
    with open('enable1.txt') as f:
        dictionary = f.readlines()
        for word in dictionary:
            word = word.strip("\n")
            if len(word) == len(wordle):
                valid_words.append(word)

    if wordle == 'xxxxx':
        wordle = valid_words[math.ceil(random.random() * len(valid_words))]

    guesses = []
    while len(guesses) < attempts:
        guess = input("Take your guess:\n")

        if guess == 'exit()':
            print("Exiting wordle-cli-python game")
            return

        if len(guess) != len(wordle):
            print("\nEnter a {} letter word.\n".format(len(wordle)))
            continue

        if guess not in valid_words:
            print("\nNot a valid word\n")
            continue

        guesses.append(guess)

        # Check for matching letters
        print("\n-----")
        for guess in guesses:
            colored_guess = color_guess(guess, wordle)
            print(colored_guess)
        print("-----\n")

        # Print the user their guess with green/yellow highlighted letters

        # Determine whether the user has won the game
        if guess == wordle:
            print("Congratulations!")
            return

    print("Out of attempts. The word was {}.".format(wordle))

def color_guess(guess, wordle):
    colored_guess = []
    for x,y in zip(guess, wordle):
        if x == y:
            x = "\033[1;32m{}\033[00m".format(x)
        elif x in wordle:
            x = "\033[1;33m{}\033[00m".format(x)

        colored_guess.append(x)
    return "".join(colored_guess)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Wordle Game")
    parser.add_argument('-w', '--wordle', type=str, help='Wordle')
    parser.add_argument('-n', '--attempts', type=int, help="Number of attempts")
    args = parser.parse_args()

    main(args.wordle, args.n)
