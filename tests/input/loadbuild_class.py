class C:
    @staticmethod
    def foobar():
        a = 1

class B(C):
    @staticmethod
    def barfoo():
        d = 1

class F(C, B):
    @staticmethod
    def raboof():
        e = 1

C.foobar()
F.raboof()
B.foobar()
