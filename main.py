import string

encrypted = []
words_inserted = 0
print(string.ascii_lowercase)
print(len(string.ascii_lowercase))

for i in range(27):
    encrypted.insert(i, "")

encrypted.insert(27, "EOF")

Test_string = "i"
test_string2 = "c"
aph_num = 0
for i in range(len(string.ascii_lowercase) - 1):
    if test_string2 == string.ascii_lowercase[i]:
        aph_num = i
        break

for i in range(27):
    encrypted.insert(i + aph_num, "i")

print(encrypted)
