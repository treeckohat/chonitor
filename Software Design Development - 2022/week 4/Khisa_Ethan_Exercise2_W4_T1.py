s = input('Projected amount of total sales? ')
if s[0] == '$':
    s = s[1:]
    s = int(s)
else:
    s = int(s)
p=float(s*.23)
p=round(p,2)
print(f"Total profit: ${p}")