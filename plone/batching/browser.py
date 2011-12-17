from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ZTUtils import  make_query

BatchTemplate = ViewPageTemplateFile("batchnavigation.pt")


class BatchMacrosView(BrowserView):
    @property
    def macros(self):
        return self.template.macros


class BatchView(BrowserView):
    """ View class for browser navigation  (classic) """

    template = BatchTemplate

    def __call__(self, batch):
        self.batch = batch
        return self.template()

    def make_link(self, pagenumber):
        raise NotImplementedError


class PloneBatchView(BatchView):
    def make_link(self, pagenumber=None):
        # XXX implement batchformkeys
        batchformkeys = None
        form = self.request.form
        if batchformkeys:
            batchlinkparams = dict([(key, form[key])
                                    for key in batchformkeys if key in form])
        else:
            batchlinkparams = form.copy()

        start = max(pagenumber - 1, 0) * self.batch.pagesize
        return '%s?%s' % (self.request.ACTUAL_URL, make_query(batchlinkparams,
                         {self.batch.b_start_str: start}))
