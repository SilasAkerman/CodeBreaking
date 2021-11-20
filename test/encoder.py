import os
from dotenv import load_dotenv
import string

load_dotenv()
TEXT = os.getenv("TEXT")
KEY = {}

def create_key():
    global KEY
    KEY = {}

    alphabet = string.ascii_uppercase
    for letter in alphabet:
        replacement = input(f"\nWhich letter should replace {letter}?   ").lower()
        if not replacement in string.ascii_lowercase or replacement in KEY.values():
            print ("Your key was not accepted, please try the whole key process again")
            break

        KEY.update({letter: replacement})
    
    print (KEY)


def encrypt_text():
    CIPHER = ""
    for element in TEXT:
        if element in KEY.keys():
            CIPHER += KEY[element]
        else:
            CIPHER += element.lower()
    
    print (CIPHER)



while True:
    command = input("\nCommand:   ")

    if command == "create_key":
        create_key()

    if command == "encrypt":
        encrypt_text()