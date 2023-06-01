import re
import json
import random
import time
import colordict

def open_quotes(filename, phrases=None):
    '''Open a file that contains a list of 3 word phrases to guess in the game'''
    try:
        with open(filename, 'r') as file:
            for line in file:
                phrases.append(line.strip())
            #print(phrases)
        return True
    except (OSError):
        # This will catch if json file does not exist and create it at the end
        phrases = []
        return False


def get_letter_positions(letter, string):
    '''Return an array with the list of positions of a character in a string, case insensitive'''
    positions = [index for index, char in enumerate(string) if char.lower() == letter.lower()]
    return positions


if __name__ == '__main__':
    quotes_array = []
    if not open_quotes('phrases.txt', quotes_array):
        print('Could not open quotes.json file, cannot continue.')
        exit(1)
    #else:
        #print(quotes_array)

    # choose a random phrase from the file
    phrase = quotes_array[ random.randint(0, len(quotes_array)) ]
    # Make the string with the underscore instead of the letters in the phrase
    placeholder = re.sub(r'\S', '_', phrase)

    points = 0
    tries = [] # array that will contain all the previous guesses
    time_start = time.time()
    while True:
        print(f"-> {colordict.clrs['BLUE' if '_' in placeholder else 'GREEN']['B']}{placeholder}{colordict.clrs['RESET']['B']}")
        if '_' not in placeholder:
            break

        while True: # iterate input until receiving a single character
            letter = input(f"{colordict.clrs['GREEN']['F']}Enter letter: {colordict.clr_reset}")
            if len(letter) == 1:
                break
            print(f"{colordict.clrs['RED']['B']}*** just type a letter, avoid responses with more than 1 character{colordict.clrs['RESET']['B']}")

        letter_l = letter.lower()
        if letter_l in placeholder.lower() or letter_l in tries:
            print((f"{colordict.clrs['RED']['B']}*** letter already " + ('tried' if letter in tries else 'guessed') + colordict.clrs['RESET']['B']))
            continue

        if letter_l not in tries:
            tries.append(letter_l)

        letter_positions = get_letter_positions(letter, phrase)
        if letter_positions:
            points += 5
            for n in letter_positions:
                placeholder = placeholder[:n] + phrase[n] + placeholder[n+1:]
        else:
            points = max(0, points - 1)
            print(f"{colordict.clrs['RED']['B']}Letter \"{letter}\" is a wrong guess{colordict.clrs['RESET']['B']}")

    time_end = time.time()
    timepassed = int(time_end - time_start)

    extrapoints = 100 if timepassed <= 30 else 0

    print(f"{colordict.clrs['BLUE']['B']}You guessed it! Points received: {points+extrapoints}{colordict.clrs['RESET']['B']}")
    print()
    if extrapoints:
        print(f"{colordict.clrs['RED']['B']}Done in just {timepassed} seconds!!! Extra 100 points for you!{colordict.clrs['RESET']['B']}")
