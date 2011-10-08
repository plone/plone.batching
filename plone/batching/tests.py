from zope.component.testing import setUp, tearDown
import unittest, doctest

class TestUtils(unittest.TestCase):

    def test_opt(self):
        pass

    def test_calculate_pagenumber(self):
        pass

    def test_calculate_pagerange(self):
        pass

    def test_calculate_quantum_leap_gap(self):
        pass

    def test_calculate_leapback(self):
        pass

    def test_calculate_leapforward(self):
        pass


def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite('batching.txt',
            package='plone.batching',
            optionflags=doctest.ELLIPSIS,
            setUp=setUp, tearDown=tearDown)))

if __name__ == "__main__":
    unittest.main(defaultTest='test_suite')