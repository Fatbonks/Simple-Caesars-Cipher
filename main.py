import string
import re


# Asks the user for the word or sentence that they want to encrypt or decrypt #
def get_sentence(user):
    # Forces the user to only input sentences that don't have numbers #
    while True:
        user = input("Please enter your sentence below\n:")
        if re.search(r'[0-9]', user_input):
            print("Please input your sentence again without numbers,\nSpaces and punctuation will work")
        else:
            return user


# Asks the user for the key/shift #
def get_key(shift):
    # Forces the user to only input numbers #
    while True:
        try:
            shift = int(input("Please enter your key below\n:"))
            return shift
        except ValueError:
            print("Please only enter numbers")


user_input = ''
key = 0
while True:
    user_input = get_sentence(user_input)
    key = get_key(key)
    print(user_input)
    print(key)
    break
