import random
import math
import json

from os.path import exists

def main():
    valid_words = load_valid_words()
    wordle = valid_words[math.ceil(random.random() * len(valid_words))];
    wordle_runner(wordle, valid_words, 'data2.json')

def wordle_runner(wordle, valid_words, path_to_data_file):
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

        # Determine whether the user has won the game
        if guess == wordle:
            save_attempt(wordle, guesses, path_to_data_file)
            labels, occurences = load_attempts(path_to_data_file)
            print("Congratulations!")
            print("\nPast Attempts:\n--------------------------------")
            print(ascii_bar_graph(labels, occurences))
            return

    # User has lost the game
    save_attempt(wordle, guesses, path_to_data_file)
    labels, occurences = load_attempts(path_to_data_file)
    print("Out of attempts. The word was {}.\n".format(wordle))
    print("\nPast Attempts:\n--------------------------------")
    print(ascii_bar_graph(labels, occurences))

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

def save_attempt(wordle, guesses, path_to_data_file):
    data = {"wordle": wordle, "guesses": guesses}
    with open(path_to_data_file, 'a+') as f:
        file_data = json.load(f)
        if 'data' not in file_data or type(file_data['data']) is not list: 
            file_data['data'] = []

        file_data['data'].append(data)
        f.seek(0)
        json.dump(file_data, f, indent = 4)
            
def load_attempts(path_to_file):
    labels = [1,2,3,4,5,6]
    attempts = [0,0,0,0,0,0]
    with open(path_to_file) as f:
        data = json.load(f)
        for entry in data['data']:
            attempts[len(entry['guesses'])-1] += 1

    return (labels, attempts)

def ascii_bar_graph(labels, occurences):
    ascii_bar = ""
    for i in range(len(labels)):
        ascii_bar += "{} |{}\n".format(labels[i], '*' * occurences[i])
    return ascii_bar

if __name__=="__main__":
    main()
