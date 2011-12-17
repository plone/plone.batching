from zope.component.testing import setUp, tearDown
import unittest
import doctest

from plone.batching.utils import calculate_pagerange, opt


class TestUtils(unittest.TestCase):
    """ Test utils of plone.batching
    """

    def test_opt(self):
        self.assertEqual(opt(1, 0, 5, 0, 100), (1, 5, 5))
        # overlap
        self.assertEqual(opt(1, 0, 5, 2, 7), (1, 7, 5))

    def test_calculate_pagenumber(self):
        pass

    def test_calculate_quantum_leap_gap(self):
        pass

    def test_calculate_leapback(self):
        pass

    def test_calculate_leapforward(self):
        pass


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        unittest.makeSuite(TestUtils),
        doctest.DocFileSuite('batching.txt',
            package='plone.batching',
            optionflags=doctest.ELLIPSIS | doctest.REPORT_ONLY_FIRST_FAILURE,
            setUp=setUp, tearDown=tearDown),
        ])
    return suite
