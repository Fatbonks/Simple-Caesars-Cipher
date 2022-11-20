import string
import re


# Asks the user for the word or sentence that they want to encrypt or decrypt #
def get_sentence(user):
    # Forces the user to only input sentences that don't have numbers #
    while True:
        user = input("Please enter your sentence below\n:")
        if re.search(r'\d', user):
            print("Please input your sentence again without numbers")
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
    # Gets each Letter in the word that user has inputted #
    for letter in word:
        # gets the length of the alphabet for lowercase #
        for length_of_alphabet_lowercase in range(len(string.ascii_lowercase)):
            if letter == string.ascii_lowercase[length_of_alphabet_lowercase]:
                # Shift is what number the user inputted for their key #
                encrypted_word = (length_of_alphabet_lowercase + shift) % len(string.ascii_lowercase)
                # after the word gets encrypted it goes into this list #
                encrypted_list.insert(value, string.ascii_lowercase[encrypted_word])
                # value is where the next string that come is going to go that why I add one #
                value += 1
        # gets the length of the alphabet for uppercase #
        for length_of_alphabet_uppercase in range(len(string.ascii_uppercase)):
            if letter == string.ascii_uppercase[length_of_alphabet_uppercase]:
                # Shift is what number the user inputted for their key #
                encrypted_word = (length_of_alphabet_uppercase + shift) % len(string.ascii_uppercase)
                # after the word gets encrypted it goes into this list #
                encrypted_list.insert(value, string.ascii_uppercase[encrypted_word])
                # value is where the next string that come is going to go that why I add one #
                value += 1
        # checks if the string is a space and then adds it into the list #
        if letter == " ":
            encrypted_list.insert(value, letter)
            value += 1
        # checks if the letter is some sort of punctuation and if it is, it adds the Letter to the list #
        for punc in range(len(string.punctuation)):
            if letter == string.punctuation[punc]:
                encrypted_list.insert(value, letter)
                value += 1
    # goes through the list and then adds each letter in the list into a string to then be used in any other decrypter #
    for encrypted_letter in range(len(encrypted_list)):
        encoded_word = encoded_word + encrypted_list[encrypted_letter]
    return encoded_word


# Decrypts words using this formula (letter = (letter - key) % 26 #
def decrypt_word(word, shift, decrypted_list, decoded_word):
    value = 0
    # Gets each Letter in the word that user has inputted #
    for letter in word:
        # gets the length of the alphabet for uppercase #
        for length_of_alphabet_lowercase in range(len(string.ascii_lowercase)):
            if letter == string.ascii_lowercase[length_of_alphabet_lowercase]:
                # Shift is what number the user inputted for their key #
                encrypted_word = (length_of_alphabet_lowercase - shift) % len(string.ascii_lowercase)
                # after the word gets decrypted it goes into this list #
                decrypted_list.insert(value, string.ascii_lowercase[encrypted_word])
                value += 1

        for length_of_alphabet_uppercase in range(len(string.ascii_uppercase)):
            if letter == string.ascii_uppercase[length_of_alphabet_uppercase ]:
                encrypted_word = (length_of_alphabet_uppercase  - shift) % len(string.ascii_uppercase)
                decrypted_list.insert(value, string.ascii_uppercase[encrypted_word])
                # value is where the next string that come is going to go that why I add one #
                value += 1
        # checks if the string is a space and then adds it into the list #
        if letter == " ":
            decrypted_list.insert(value, letter)
            value += 1
        # checks if the letter is some sort of punctuation and if it is, it adds the Letter to the list #
        for punc in range(len(string.punctuation)):
            if letter == string.punctuation[punc]:
                decrypted_list.insert(value, letter)
                value += 1
    # goes through the list and then adds each letter in the list into a string to then be used in any other encrypter #
    for decrypted_letter in range(len(decrypted_list)):
        decoded_word = decoded_word + decrypted_list[decrypted_letter]
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
    encrypt_list = []
    decrypt_list = []
    new_encoded_word = ""
    new_decoded_word = ""
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
        input("press enter to continue")
    elif ans == 2:
        user_input = get_sentence(user_input)
        key = get_key(key)
        new_decoded_word = decrypt_word(user_input, key, decrypt_list, new_decoded_word)
        print(new_decoded_word)
        input("press enter to continue")
    elif ans != 1 or ans != 2:
        print("please input 1 or 2")
