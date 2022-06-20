class C:
    @staticmethod
    def test1():
        a = 1

    @staticmethod
    def test2(x, y, z):
        a = x * y + z

    # @staticmethod -- TODO: Fix decorators
    @staticmethod
    def testS():
        a = 3

c = C()
c.test1()
c.test2(42, 5, -1)
C.testS()
