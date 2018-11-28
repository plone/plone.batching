# -*- coding: utf-8 -*-
from plone.batching.batch import BaseBatch
from plone.batching.batch import QuantumBatch
from plone.batching.browser import BatchMacrosView
from plone.batching.browser import BatchView
from plone.batching.browser import PloneBatchView
from plone.batching.utils import calculate_leapback
from plone.batching.utils import calculate_leapforward
from plone.batching.utils import calculate_pagenumber
from plone.batching.utils import calculate_pagerange
from plone.batching.utils import calculate_quantum_leap_gap
from plone.batching.utils import opt
from zope.component.testing import setUp
from zope.component.testing import tearDown

import doctest
import unittest


class TestUtilsOpt(unittest.TestCase):
    """ Test utils of plone.batching
    """

    def test_opt_standard(self):
        self.assertEqual(opt(1, 0, 5, 0, 100), (1, 5, 5))

    def test_opt_overlap(self):
        # overlap
        self.assertEqual(opt(1, 0, 5, 2, 7), (1, 7, 5))

    def test_opt_nosize_start_end(self):
        # no size given, but valid start and end parameters
        self.assertEqual(opt(1, 31, 0, 0, 100), (1, 31, 31))

    def test_opt_nosize_noend(self):
        # no size and no valid start and end parameters given
        self.assertEqual(opt(1, 0, 0, 0, 100), (1, 25, 25))

    def test_opt_start_bigger_length(self):
        # start > length
        self.assertEqual(opt(20, 0, 5, 0, 10), (10, 10, 5))

    def test_opt_end_smaller_start(self):
        # end > start
        self.assertEqual(opt(20, 10, 5, 0, 100), (20, 20, 5))


class TestUtils(unittest.TestCase):

    def test_calculate_pagenumber(self):
        self.assertEqual(calculate_pagenumber(5, 2), 3)

    def test_calculate_pagenumber_zerobatch(self):
        self.assertEqual(calculate_pagenumber(5, 0), 5)

    def test_calculate_pagerange(self):
        self.assertEqual(calculate_pagerange(3, 10, 2), (1, 3, 4))

    def test_calculate_quantum_leap_gap(self):
        self.assertEqual(calculate_quantum_leap_gap(20, 2), 5)

    def test_calculate_leapback(self):
        self.assertEqual(list(calculate_leapback(73, 100, 2)), [28, 43, 58])

    def test_calculate_leapforward(self):
        self.assertEqual(list(calculate_leapforward(3, 100, 2)), [18, 33, 48])


class TestBatch(unittest.TestCase):

    def test_previous_first(self):
        batch = BaseBatch(range(20), 5)
        self.assertFalse(batch.previous)

    def test_navlist_no_pagerange(self):
        # Well, actually with a default pagerange (7)
        # greater than the number of pages: all pages should be displayed

        for start in range(20):
            batch = BaseBatch(range(20), 5, start)
            self.assertListEqual(list(batch.navlist), [1, 2, 3, 4])

    def test_navlist_with_pagerange(self):
        # Until we reach page 3 we have 3 pages centered on 2
        for start in range(0, 10):
            batch = BaseBatch(range(20), 5, start, pagerange=3)
            self.assertListEqual(
                list(batch.navlist),
                [1, 2, 3],
                'Failing when starting at {}'.format(start)
            )

        # then we have 3 pages centered on page 3
        for start in range(10, 15):
            batch = BaseBatch(range(20), 5, start, pagerange=3)
            self.assertListEqual(
                list(batch.navlist),
                [2, 3, 4],
                'Failing when starting at {}'.format(start)
            )

        # XXX I consider this an errorm it should be [2, 3, 4]
        # when we are at the last page we have two pages starting at 3
        for start in range(15, 20):
            batch = BaseBatch(range(20), 5, start, pagerange=3)
            self.assertListEqual(
                list(batch.navlist),
                [3, 4],
                'Failing when starting at {}'.format(start)
            )

    def test_previous(self):
        batch = BaseBatch(range(20), 5, 5)
        prev = batch.previous
        self.assertTrue(isinstance(prev, BaseBatch))
        self.assertEqual(prev.start, 1)

    def test_getitem_out_of_batch(self):
        batch = BaseBatch(range(20), 5)
        self.assertRaises(IndexError, batch.__getitem__, 6)

    def test_getitem_resultcount(self):
        class MySeq(list):

            @property
            def actual_result_count(self):
                return len(self) + 1

        batch = BaseBatch(MySeq(range(20)), 5)
        self.assertEqual(batch[3], 3)
        self.assertEqual(list(batch), [0, 1, 2, 3, 4])
        self.assertRaises(IndexError, batch.__getitem__, 6)

    def test_getitem_negative(self):
        batch = BaseBatch(range(20), 5)
        self.assertEqual(batch[-4], 1)
        self.assertRaises(IndexError, batch.__getitem__, -6)

    def test_lastpage(self):
        batch = BaseBatch(range(20), 5)
        self.assertFalse(batch.islastpage)
        lastbatch = BaseBatch(range(20), 5, start=batch.last)
        self.assertTrue(lastbatch.islastpage)

    def test_lastpage_with_orphans(self):
        batch = BaseBatch(range(11), 10, orphan=1)
        self.assertEqual(1, batch.lastpage)
        batch = BaseBatch(range(109), 10, orphan=9)
        self.assertEqual(10, batch.lastpage)
        batch = BaseBatch(range(71), 10, orphan=2)
        self.assertEqual(7, batch.lastpage)
        batch = BaseBatch(range(0), 0, orphan=0)
        self.assertEqual(1, batch.lastpage)
        self.assertRaises(AssertionError, BaseBatch, [], 10, orphan=20)

    def test_items_not_on_page(self):
        batch = BaseBatch(range(20), 5, start=5)
        self.assertEqual(batch.items_not_on_page,
                         [0, 1, 2, 3, 4, 10, 11, 12,
                          13, 14, 15, 16, 17, 18, 19])
        self.assertEqual(list(batch), [5, 6, 7, 8, 9])

    def test_batch_bsize(self):
        sequence = range(279)
        # Random page
        batch = BaseBatch(sequence, 10, start=80)
        self.assertEqual(batch.length, 10)

        # Last page
        batch = BaseBatch(sequence, 10, start=270)
        self.assertEqual(batch.length, 9)

        # Beyond last page
        batch = BaseBatch(sequence, 10, start=280)
        self.assertEqual(batch.length, 0)

        # Single item batch
        batch = BaseBatch(range(1), 10)
        self.assertEqual(batch.length, 1)

        # Small sequence batch (to cover plone.z3cform.crud)
        small_sequence = range(3)
        # Page 1
        batch = BaseBatch.fromPagenumber(small_sequence, 2, 1)
        self.assertEqual(batch.length, 2)

        # Page 2
        batch = BaseBatch.fromPagenumber(small_sequence, 2, 2)
        self.assertEqual(batch.length, 1)

    def test_multiple_pages_smaller(self):
        """sequence smaller than batchsize"""
        batch = BaseBatch(range(12), 20)
        self.assertEquals(batch.multiple_pages, False)

    def test_multiple_pages_equals(self):
        """sequence equals batchsize"""
        batch = BaseBatch(range(12), 12)
        self.assertEquals(batch.multiple_pages, False)

    def test_multiple_pages_longer(self):
        """sequence longer than batchsize"""
        batch = BaseBatch(range(12), 10)
        self.assertEquals(batch.multiple_pages, True)

    def test_multiple_pages_orphan(self):
        """sequence with orphans"""
        self.assertFalse(BaseBatch(range(20), 20, orphan=0).multiple_pages)
        self.assertTrue(BaseBatch(range(21), 20, orphan=0).multiple_pages)
        self.assertFalse(BaseBatch(range(21), 20, orphan=1).multiple_pages)
        self.assertFalse(BaseBatch(range(22), 20, orphan=2).multiple_pages)
        self.assertTrue(BaseBatch(range(22), 20, orphan=1).multiple_pages)

    def test_pagenumber_never_over_numpages(self):
        """computed _pagenumber is never > numpages, this
           makes previous_pages not fail."""
        batch = BaseBatch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 9)
        self.assertEquals(list(batch.previous_pages), [1, 2, 3])
        self.assertEquals(batch._pagenumber, 4)
        # works especially with orphan
        batch = BaseBatch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 9, orphan=2)
        self.assertEquals(list(batch.previous_pages), [1, 2])
        self.assertEquals(batch._pagenumber, 3)


class TestQuantumBatch(unittest.TestCase):

    def test_quantumbatch(self):
        qbatch = QuantumBatch(range(200), 3, start=120, quantumleap=1)
        self.assertEqual(list(qbatch.leapback), [18, 28])
        self.assertEqual(list(qbatch.leapforward), [54])


class DummyTemplate(object):
    macros = 'here are PT macros normally'

    def __call__(self):
        return "Template called!"


class TestBrowser(unittest.TestCase):

    def test_batchmacrosview(self):
        view = BatchMacrosView(None, None)
        setattr(view, 'template', DummyTemplate())   # fake view creation
        self.assertEqual(view.macros, 'here are PT macros normally')

    def test_batchview_base(self):
        from zope.publisher.browser import TestRequest
        view = BatchView(None, TestRequest())
        setattr(view, 'index', DummyTemplate())   # fake view creation
        self.assertRaises(NotImplementedError, view.make_link, 0)
        rendered = view([1, 2, 3], ['a', 'b'])
        self.assertEqual(rendered, "Template called!")
        self.assertEqual(view.batch, [1, 2, 3])
        self.assertEqual(view.batchformkeys, ['a', 'b'])

    def test_batchview_plone(self):
        from zope.publisher.browser import TestRequest
        batch = BaseBatch([1, 2, 3, 4, 5, 6, 7], 3)
        request = TestRequest(form={'a': 'foo', 'c': 'bar'})
        setattr(request, 'ACTUAL_URL', 'http://nohost/dummy')
        view = PloneBatchView(None, request)
        view(batch, ['a', 'b'])
        self.assertEqual(view.make_link(3),
                         'http://nohost/dummy?a=foo&b_start:int=6')

    def test_batchview_plone_ajax_load(self):
        from zope.publisher.browser import TestRequest
        batch = BaseBatch([1, 2, 3, 4, 5, 6, 7], 3)
        request = TestRequest(form={'a': 'foo', 'ajax_load': 1})
        setattr(request, 'ACTUAL_URL', 'http://nohost/dummy')
        view = PloneBatchView(None, request)
        view(batch)  # don't set allowed params (batchformkeys) like above.
        # allow all, but filter for ajax_load separately
        self.assertEqual(view.make_link(3),
                         'http://nohost/dummy?a=foo&b_start:int=6')


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        unittest.makeSuite(TestUtilsOpt),
        unittest.makeSuite(TestUtils),
        unittest.makeSuite(TestBatch),
        unittest.makeSuite(TestBrowser),
        unittest.makeSuite(TestQuantumBatch),
        doctest.DocFileSuite('batching.rst',
                             package='plone.batching',
                             optionflags=doctest.ELLIPSIS,
                             setUp=setUp, tearDown=tearDown),
    ])
    return suite
