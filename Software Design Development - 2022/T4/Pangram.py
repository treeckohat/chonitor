sentence = input("sentence? ").lower()
check = 0
if 'q' in sentence:
    check = check + 1
if 'w' in sentence:
    check = check + 1
if 'e' in sentence:
    check = check + 1
if 'r' in sentence:
    check = check + 1
if 't' in sentence:
    check = check + 1
if 'y' in sentence:
    check = check + 1
if 'u' in sentence:
    check = check + 1
if 'i' in sentence:
    check = check + 1
if 'o' in sentence:
    check = check + 1
if 'p' in sentence:
    check = check + 1
if 'a' in sentence:
    check = check + 1
if 's' in sentence:
    check = check + 1
if 'd' in sentence:
    check = check + 1
if 'f' in sentence:
    check = check + 1
if 'g' in sentence:
    check = check + 1
if 'h' in sentence:
    check = check + 1
if 'j' in sentence:
    check = check + 1
if 'k' in sentence:
    check = check + 1
if 'l' in sentence:
    check = check + 1
if 'z' in sentence:
    check = check + 1
if 'x' in sentence:
    check = check + 1
if 'c' in sentence:
    check = check + 1
if 'v' in sentence:
    check = check + 1
if 'b' in sentence:
    check = check + 1
if 'n' in sentence:
    check = check + 1
if 'm' in sentence:
    check = check + 1

if check == 26:
    print('is a pangram')
else:
    print('not a pangram')