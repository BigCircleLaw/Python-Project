def log(func):
    def aaa():
        print(func.__name__)
        return func()
    return aaa


@log
def now():
    print('liuziyuan')

now()