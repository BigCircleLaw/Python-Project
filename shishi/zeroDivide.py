def spam(numDivided, divideBy):
    if divideBy == 0:
        print('divideBy is error!!!')
        return None
    return (numDivided / divideBy)


def spam2(numDivided2, divideBy2):
    try:
        return (numDivided2 / divideBy2)
    except ZeroDivisionError:
        print('divideBy is error!!!')


print(spam(4, 5))
print(spam(6, 9))
print(spam(8, 7547))
print(spam(235, 52))
print(spam(8986, 0))

print(spam2(4, 5))
print(spam2(6, 9))
print(spam2(8, 7547))
print(spam2(235, 52))
print(spam2(8986, 0))
