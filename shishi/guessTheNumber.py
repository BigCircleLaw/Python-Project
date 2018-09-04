import random


def getResult():
    print('Take a guess.')
    num = int(input())
    if num > value:
        print('Your guess is too high.')
        return True
    elif num < value:
        print('Your guess is too low.')
        return True
    else:
        print('Good jod!', end=' ')
        return False


value = random.randint(1, 20)

count = 1
while getResult():
    count = count + 1
print('You guessed my number in ' + str(count) + ' guess!')
