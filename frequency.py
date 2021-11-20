import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
import string

load_dotenv()
CODE = os.getenv("CODE").upper()
ELEMENTS = string.ascii_uppercase
KEY = {i: i for i in ELEMENTS}


def letter_frequency():
    frequencies = []
    total = 0
    for letter in ELEMENTS:
        print (f"{letter} occurs {CODE.count(letter)}")
        frequencies.append(CODE.count(letter))
        total += frequencies[-1]

    percentages = list(map(lambda x: 100*(x/total), frequencies))

    plt.bar(list(ELEMENTS), percentages)
    plt.show()


def command_replace_letter():
    try:
        origin = input("\nWhich letter do you want to replace?  ").upper()
        if KEY[origin].islower():
            print ("That letter has already been replaced. You can undo it if you want.")
            return

        target = input("\nWhich letter should this turn into?   ")
        KEY[origin] = target.lower()
    except:
        print ("Something went wrong, try again")


def prepare_cipher():
    CIPHER = CODE

    for element in ELEMENTS:
        if element in KEY.keys() and KEY[element].islower():
            CIPHER = CIPHER.replace(element, KEY[element])
    
    return CIPHER


def command_undo_letter():
    try:
        global KEY
        letter = input("\nWhich letter would you like to undo?  ").upper()
        KEY[letter] = letter
    except:
        print ("Something went wrong, try again")

def command_restore_letter():
    try:
        global KEY
        letter = input("\nWhich letter would you like to restore?   ").lower()
        if letter in KEY.values():
            for element in KEY:
                if letter == KEY[element]:
                    KEY[element] = element
        else:
            print ("That letter has not been decoded yet. Maybe try this again")
    except:
        print ("Something went wrong, try again")




while True:
    command = input("\nCommand:   ")

    if command == "frequency":
        letter_frequency()

    if command == "replace":
        command_replace_letter()

    if command == "code":
        print (CODE)

    if command == "cipher":
        CIPHER = prepare_cipher()
        print (CIPHER)

    if command == "key":
        print (KEY)

    if command == "undo":
        command_undo_letter()

    if command == "restore":
        command_restore_letter()