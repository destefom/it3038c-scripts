# birthday date (how old you are in seconds)

import datetime

while True:
    print('What is your birthday? (Day Month Year)')
    bday = input()

    birthday = datetime.datetime.strptime(bday, '%d %B %Y')
    print(birthday)
    break 

jintian = datetime.datetime.today()
timedelta = (jintian - birthday).total_seconds()

print("You are ", timedelta, " seconds old!")