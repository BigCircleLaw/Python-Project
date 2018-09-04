
def collatz(number):
    if (number%2) == 0:
        print(int(number / 2))
        return number / 2
    else:
        print(int(3 * number + 1))
        return 3 * number + 1

def aaa(shshi):
    try:
        int(shshi)
    except ValueError:
        print('请输入一个大于1的整数:')

value = 0
while value == 0:
    str = input()
    # aaa(str)
    try:
        int(str)
    except ValueError:
        print('请输入一个大于1的整数:')
        continue
    if int(str) <= 1:
        print('请输入一个大于1的整数:')
    else:
        value = int(str)

while value != 1:
    value = collatz(value)


