print('''In numeric month/day/year
E.G. 7/4/23''')

month,day,year = input('What date in the above format? ').split('/')
month = int(month)
day = int(day)
year = int(year)
if month * day == year:
    print('date is magic')
else:
    print('date not magic')