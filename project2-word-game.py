import re
import json
import random
import colordict

def open_quotes(filename, phrases=None):
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


def find_letter_positions(letter, string):
    positions = [match.start() for match in re.finditer(re.escape(letter), string)]
    return positions


quotes_array = []
if not open_quotes('phrases.txt', quotes_array):
    print('Could not open quotes.json file, cannot continue.')
    exit(1)
#else:
    #print(quotes_array)

phrase_position = random.randint(0, len(quotes_array))
#print('position: ',phrase_position)
phrase = quotes_array[phrase_position]
#print('Phrase: ',phrase)

placeholder = re.sub(r'\S', '_', phrase)
points = 0
while True:
    print(f"-> {colordict.clrs['BLUE']['B']}{placeholder}{colordict.clr_reset}")
    #print(f"-----> {placeholder}")
    if '_' not in placeholder:
        break

    while True:
        letter = input(f"{colordict.clrs['GREEN']['F']}Enter letter: {colordict.clr_reset}")
        if len(letter) == 1:
            break
        print(f"{colordict.clrs['RED']['B']}*** just type a letter, avoid responses with more than 1 character{colordict.clr_reset}")

    if letter.lower() in placeholder.lower():
        print((f"{colordict.clrs['RED']['B']}*** letter already guessed{colordict.clr_reset}"))
        continue

    if letter.lower() in phrase.lower():
        points += 5
        letter_positions = find_letter_positions(letter.lower(), phrase.lower())
        for n in letter_positions:
            placeholder = placeholder[:n] + phrase[n] + placeholder[n+1:]
    else:
        print(f"{colordict.clrs['RED']['B']}Letter \"{letter}\" is a wrong guess{colordict.clr_reset}")
        points = max(0, points - 1)

print(f'You guessed it! Points received: {points}')
