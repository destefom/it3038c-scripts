import time
start_time = time.time()
from re import M


print('What is your name?')
myName = input()

print('Hello, ' + myName + '. That is a good name. How old are you?')
myAge = int(input())

programAge = int(time.time() - start_time)

print('%s? That\'s funny, I\'m only %s seconds old.' % (myAge, programAge))
print("I wish I was %s years old" % (myAge * 2))

time.sleep(3)
print('I\'m tired. I go sleep sleep now.')