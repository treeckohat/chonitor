letter = input('letter? ')
while len(letter) != 1:
    letter = input('letter? ')
if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
    print('It is a vowel')
else:
    print('It is a consonant')