from littlepythonhelpers import ReprMixin
import unittest as ut

class TestReprNoArgs(ut.TestCase):
    def setUp(self):
        class Foo(ReprMixin):
            pass
        self.iut = Foo()

    def test_no_args(self):
        self.assertEqual(repr(self.iut), 'Foo()')


class TestReprPositional(ut.TestCase):
    def setUp(self):
        class Foo(ReprMixin):
            def __init__(self, a, b):
                self.a = a
                self.b = b

            def repr_args(self):
                return [self.a, self.b]
        self.Foo = Foo

    def test_ints(self):
        iut = self.Foo(1,-2)
        self.assertEqual(repr(iut), 'Foo(1, -2)')

    def test_various(self):
        iut = self.Foo("a", None)
        self.assertEqual(repr(iut), "Foo('a', None)")
        iut = self.Foo(None, 1.5)
        self.assertEqual(repr(iut), 'Foo(None, 1.5)')
        iut2 = self.Foo([x for x in range(5)], {'a':1})
        self.assertEqual(repr(iut2), "Foo([0, 1, 2, 3, 4], {'a': 1})")
        iut3 = self.Foo(iut, iut2)
        self.assertEqual(repr(iut3),
            "Foo(Foo(None, 1.5), Foo([0, 1, 2, 3, 4], {'a': 1}))")

class TestReprKwarg(ut.TestCase):
    def setUp(self):
        class Foo(ReprMixin):
            def __init__(self, a=None, b=7, c=None):
                self.a = a
                self.b = b
                self.cc = c

            def repr_kwargs(self):
                return ['a', ('b', self.b, 7), ('c', self.cc)]

        self.Foo = Foo

    def test_ints(self):
        iut = self.Foo(a=1)
        self.assertEqual(repr(iut), "Foo(a=1)")
        iut = self.Foo(a=1, b=2, c=3)
        self.assertEqual(repr(iut), "Foo(a=1, b=2, c=3)")

class TestArgsAndKwargs(ut.TestCase):
    def setUp(self):
        class Foo(ReprMixin):
            def __init__(self, a, b, c=None, d=7, e=None):
                self.a = a
                self.b = b
                self.c = c
                self.d = d
                self.ee = e

            def repr_args(self):
                return [self.a, self.b]

            def repr_kwargs(self):
                return ['c', ('d', self.d, 7), ('e', self.ee)]

        self.Foo = Foo

    def test_no_kwarg(self):
        iut = self.Foo(1,2)
        self.assertEqual(repr(iut), "Foo(1, 2)")

    def test_ints(self):
        iut = self.Foo(1, 2, c=3, d=4, e=5)
        self.assertEqual(repr(iut), "Foo(1, 2, c=3, d=4, e=5)")


if __name__ == '__main__':
    ut.main()
