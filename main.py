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


# Encrypts words using this formula (letter = (letter + key) % 26 #
def encrypt_word(word, shift, encrypted_list, encoded_word):
    value = 0
    for element in word:
        for i in range(len(string.ascii_letters) - 1):
            if element == string.ascii_letters[i]:
                encrypted_word = (i + shift) % len(string.ascii_letters)
                encrypted_list.insert(value, string.ascii_letters[encrypted_word])
                value += 1
        if element == " ":
            encrypted_list.insert(value, element)
            value += 1
        for punc in range(len(string.punctuation)):
            if element == string.punctuation[punc]:
                encrypted_list.insert(value, element)
                value += 1
    for i in range(len(encrypted_list)):
        encoded_word = encoded_word + encrypted_list[i]
    return encoded_word


# Decrypts words using this formula (letter = (letter - key) % 26 #
def decrypt_word(word, shift, decrypted_list, decoded_word):
    value = 0
    for element in word:
        for i in range(len(string.ascii_letters) - 1):
            if element == string.ascii_letters[i]:
                encrypted_word = (i - shift) % len(string.ascii_letters)
                decrypted_list.insert(value, string.ascii_letters[encrypted_word])
                value += 1
        if element == " ":
            decrypted_list.insert(value, element)
            value += 1
        for punc in range(len(string.punctuation)):
            if element == string.punctuation[punc]:
                decrypted_list.insert(value, element)
                value += 1
    for letter in range(len(decrypted_list)):
        decoded_word = decoded_word + decrypted_list[letter]
    return decoded_word


# variables
user_input = ''
key = 0
encrypt_list = []
decrypt_list = []
new_encoded_word = ""
new_decoded_word = ""
# main routine #
while True:
    # Forces valid input #
    while True:
        try:
            ans = int(input("1:Encrypt\n2:Decrypt\nAnswer here:"))
            break
        except ValueError:
            print("please only use numbers")
    if ans == 1:
        user_input = get_sentence(user_input)
        key = get_key(key)
        new_encoded_word = encrypt_word(user_input, key, encrypt_list, new_encoded_word)
        print(new_encoded_word)
    elif ans == 2:
        user_input = get_sentence(user_input)
        key = get_key(key)
        new_decoded_word = decrypt_word(user_input, key, decrypt_list, new_decoded_word)
        print(new_decoded_word)
    input("press enter to continue")
