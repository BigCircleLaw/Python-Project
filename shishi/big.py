import types


class A(object):
    def __init__(self):
        pass

    # @classmethod
    # def print_list(cls):
    #     print(cls._list)


@classmethod
def pr_list(cls):
    print(cls._list)


setattr(A, 'print_list', pr_list)


class B(A):
    _list = list()

    def __init__(self):
        self.a = 2
        B._list.append(self)

    def print_a(self):
        print(self.a)


aa = A()
a = B()
b = B()


def s(self, val):
    self.a = val


set_a = types.MethodType(s, a)

pr_a = a.print_a
setattr(B, 'set', s)
c = B()
a.print_a()
set_a(20)
a.print_a()

c.print_a()
c.set(10)
c.print_a()


def x(func):
    print(type(func.__name__))
    print(func.__name__)


@x
def z():
    pass


B.print_list()
