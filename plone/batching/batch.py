from ZTUtils.Batch import Batch as ZTUBatch
from ZTUtils import make_query
from ExtensionClass import Base

from plone.batching.interfaces import IBatch
from zope.interface import implements

from plone.batching.utils import (
    opt, calculate_leapback, calculate_leapforward,
    calculate_pagenumber, calculate_pagerange, calculate_quantum_leap_gap)


class Batch(object):
    """ A sequence batch implementation
    """

    implements(IBatch)

    b_start_str = 'b_start'
    quantumleap = 0
    leapback = leapforward = 0

    def __init__(self, items, pagesize=20, pagenumber=1, navlistsize=5, orphan=0, overlap=0):
        """
        Encapsulate sequence in batches of pagesize.
        """
        self.items = items
        self.pagesize = pagesize
        self.pagenumber = pagenumber
        self.navlistsize = navlistsize

    def fromStartEnd(cls, sequence, size, start=0, end=0, orphan=0, overlap=0,
                 pagerange=7, quantumleap=0, b_start_str='b_start'):
        """ Encapsulate sequence in batches of size
        sequence    - the data to batch.
        size        - the number of items in each batch. This will be computed if left out.
        start       - the first element of sequence to include in batch (0-index)
        end         - the last element of sequence to include in batch (0-index, optional)
        orphan      - the next page will be combined with the current page if it does not contain more than orphan elements
        overlap     - the number of overlapping elements in each batch
        pagerange   - the number of pages to display in the navigation
        quantumleap - 0 or 1 to indicate if bigger increments should be used in the navigation list for big results.
        b_start_str - the request variable used for start, default 'b_start'
        """

        start, end, sz = opt(start, end, size, orphan, len(sequence))
        pagenumber = calculate_pagenumber(start, size, overlap)

#        self.b_start_str = b_start_str
#
#        # QuantumLeap - faster navigation for big result sets
#        self.quantumleap = quantumleap
#        self.leapback = self.leapforward = []
#        if self.quantumleap:
#            self.leapback = calculate_leapback(self.pagenumber, self.numpages, self.pagerange)
#            self.leapforward = calculate_leapforward(self.pagenumber, self.numpages, self.pagerange)

        return cls(sequence, size, pagenumber, pagerange, orphan, overlap)
    fromStartEnd = classmethod(fromStartEnd)

    def fromRange(cls, length, pagesize=20, pagenumber=1, navlistsize=5):
        """
        Create a batch from a range of a given length
        """
        items = range(length)
        return cls(items, pagesize, pagenumber, navlistsize)
    fromRange = classmethod(fromRange)
            
    def __len__(self):
        return len(self.items)

    @property
    def firstpage(self):
        return 1

    @property
    def size(self):
        return len(self)
        
    def __iter__(self):
        """
        Iterate over a single batch
        """
        start = (self.pagenumber-1) * self.pagesize
        end = start + self.pagesize
        return self.items[start:end].__iter__()

    @property
    def navlist(self):
        start = self.pagenumber - (self.navlistsize / 2)
        if start < 1:
            start = 1
        end = start + self.navlistsize - 1
        if end > self.lastpage:
            end = self.lastpage

        return range(start, end+1)

    @property
    def items_on_page(self):
        if self.islastpage:
            remainder = self.size % self.pagesize
            if remainder == 0:
                return self.pagesize
            else:
                return remainder
        else:
            return self.pagesize

    @property
    def items_not_on_page(self):
        start = (self.pagenumber-1) * self.pagesize
        end = start + self.pagesize
        return self.items[:start] + self.items[end:]

    @property
    def next_item_count(self):
        """
        Number of elements in next batch
        """
        nextitems = self.size - (self.pagenumber * self.pagesize)
        if nextitems > self.pagesize:
            return self.pagesize
        return nextitems

    @property
    def islastpage(self):
        return self.lastpage == self.pagenumber

    @property
    def multiple_pages(self):
        return bool(self.size / self.pagesize)

    @property
    def has_next(self):
        return (self.pagenumber * self.pagesize) < self.size

    @property
    def show_link_to_first(self):
        return 1 not in self.navlist

    @property
    def show_link_to_last(self):
        return self.lastpage not in self.navlist

    @property
    def before_last_page_not_in_navlist(self):
        return (self.lastpage - 1) not in self.navlist

    @property
    def has_previous(self):
        return self.pagenumber > 1

    @property
    def previous_pages(self):
        return self.navlist[:self.navlist.index(self.pagenumber)]
    
    @property
    def next_pages(self):
        return self.navlist[self.navlist.index(self.pagenumber)+1:]

    @property
    def previouspage(self):
        return self.pagenumber - 1

    @property
    def nextpage(self):
        return self.pagenumber + 1

    @property
    def lastpage(self):
        pages = self.size / self.pagesize
        if self.size % self.pagesize:
            pages += 1
        return pages

    @property
    def second_page_not_in_navlist(self):
        return 2 not in self.navlist



