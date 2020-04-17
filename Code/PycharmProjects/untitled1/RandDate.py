import random as rand

while True:
    num = input('Please enter the number of desired dates : ')
    if not num.isdigit():
        print('Please enter a valid number!')
        continue
    else:
        num = int(num)
        break

while True:
    year = input('Please enter the year of the dates : ')
    if not year.isdigit():
        print('Please enter a valid year!')
        continue
    else:
        if int(year) <= 0:
            print('Please enter a valid year!')
            continue

        break

Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
leap: bool   # if true, year is a leap year
date: str
dateList = []  # List to save our dates in the form: DD-MM-YYYY
dateP = []  # List to save our date as a tuple in the form: (day, month)

# Iteration to check if the year is a leap year
if int(year) % 4 != 0:
    leap = False
elif int(year) % 100 != 0:
    leap = True
elif int(year) % 400 != 0:
    leap = False
else:
    leap = True

# Beginning of date creation
for i in range(num):
    y = rand.randint(1, 12)
    if y in [1, 3, 5, 7, 8, 10, 12]:  # The specified months have 31 days
        x = rand.randint(1, 31)
    elif y == 2:    # February has 28 or 29 days, depending if it is a leap year
        if leap:
            x = rand.randint(1, 29)
        else:
            x = rand.randint(1, 28)
    else:
        x = rand.randint(1, 30)
    date = '{:0=2d}-{:0=2d}-{}'.format(x, y, year)
    # Check if the random date already exists on our list
    if date not in dateList:
        dateList.append(date)
        dateP.append((x, y))
    elif date in dateList:
        i -= 1

# Printing of the dates in the form: Day-Month(from the Months list)-Year
for d in dateP:
    print('{}-{}-{}'.format(d[0], Months[d[1] - 1], year))

# Printing of the dates in the form: DD-MM-YYYY
print('And in list form: ', dateList)

if leap:
    print('The year {} is a leap year!'.format(year))
else:
    print('The year {} is not a leap year!'.format(year))
