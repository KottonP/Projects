import string

alphabet = list(string.ascii_lowercase)
text = list(input("Give text :").casefold())
# noinspection SpellCheckingInspection
alphacount = {}
for let in alphabet:
    alphacount.update({let: 0})

for let1 in alphabet:
    for let2 in text:
        if let1 == let2:
            alphacount[let1] += 1
            continue

for letter in alphacount.keys():
    if alphacount[letter] != 0:
        print(letter + " => " + str(alphacount[letter]))
