numb1, numb2 = input('What are your numbers? ').split()
while numb1 != numb2:
    print("Not a match")
    numb1, numb2 = input('What are your numbers? ').split()
if numb1 == numb2:
    print('You should SNAP.')