import string
import re
letters = list(string.ascii_letters + string.digits + ' ' + string.punctuation)
print(letters)

encode = input("stuff: ")
key = int(''.join(re.findall('[0-9-]', input("stuff: "))))
new_string = []

for letter in encode:
    new_string.append(letters[(letters.index(letter) + key) % len(letters)])

print(new_string)
