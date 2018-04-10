while True:
    print('Who are you?')
    name = input()
    if name != 'yuan':
        continue
    print('Hello, yuan. What is password?')
    password = input()
    if password == '0615':
        break
print('Access granted.')
