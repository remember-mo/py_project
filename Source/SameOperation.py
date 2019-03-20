# coding: utf-8

class A(object):
    pass


class B(A):
    pass


a = A()
b = B()
print(isinstance(a, A))
print(isinstance(a, B))
print(isinstance(b, A))
print(isinstance(b, B))
