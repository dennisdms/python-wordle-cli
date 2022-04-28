import random
import math
import json

def main():
    valid_words = load_valid_words()
    wordle = valid_words[math.ceil(random.random() * len(valid_words))];

    guesses = []
    while len(guesses) < 6:
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
            save_attempt(wordle, guessses)
            print(show_data())
            return

    print("Out of attempts. The word was {}.".format(wordle))
    save_attempt(wordle, guesses)
    print(show_data())

def color_guess(guess, wordle):
    colored_guess = []
    for x,y in zip(guess, wordle):
        if x == y:
            x = "\033[1;32m{}\033[00m".format(x)
        elif x in wordle:
            x = "\033[1;33m{}\033[00m".format(x)

        colored_guess.append(x)
    return "".join(colored_guess)

def load_valid_words():
    valid_words = []
    with open('enable1.txt') as f:
        dictionary = f.readlines()
        for word in dictionary:
            word = word.strip("\n")
            if len(word) == 5:
                valid_words.append(word)
    
    return valid_words

def save_attempt(wordle, guesses):
    data = {"wordle": wordle, "guesses": guesses}
    with open('data.json', 'r+') as f:
        file_data = json.load(f)
        file_data['data'].append(data)
        f.seek(0)
        json.dump(file_data, f, indent = 4)

def show_data():
    with open('data.json') as f:
        data = json.load(f)
        for entry in data['data']:
            print("wordle: {}, guesses {}, attempts: {}".format(entry['wordle'], entry['guesses'], len(entry['guesses'])))

if __name__=="__main__":
    main()
