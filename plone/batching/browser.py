# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ZTUtils import make_query

BatchTemplate = ViewPageTemplateFile("batchnavigation.pt")
BootstrapBatchTemplate = ViewPageTemplateFile("batchnavigation_bootstrap.pt")


class BatchMacrosView(BrowserView):

    @property
    def macros(self):
        return self.template.macros


class BatchView(BrowserView):
    """ View class for browser navigation  (classic) """

    index = BatchTemplate
    batch = None
    batchformkeys = None
    minimal_navigation = False

    def __call__(self, batch, batchformkeys=None, minimal_navigation=False):
        self.batch = batch
        self.batchformkeys = batchformkeys
        self.minimal_navigation = minimal_navigation
        return self.index()

    def make_link(self, pagenumber):
        raise NotImplementedError


class BootstrapBatchView(BatchView):
    index = BootstrapBatchTemplate


class PloneBatchView(BatchView):

    def make_link(self, pagenumber=None, omit_params=['ajax_load']):
        # Include request form parameters from parent request
        query_params = {}
        if "PARENT_REQUEST" in self.request:
            query_params.update(self.request["PARENT_REQUEST"].form)
        # update/override parent params with actual request params
        query_params.update(self.request.form)
        if self.batchformkeys:
            for key in list(query_params.keys()):
                if key not in self.batchformkeys:
                    del query_params[key]
        if omit_params:
            for key in omit_params:
                if key in query_params:
                    del query_params[key]

        start = max(pagenumber - 1, 0) * self.batch.pagesize
        query_params[self.batch.b_start_str] = start
        url = u"{0}?{1}".format(self.request.ACTUAL_URL, make_query(query_params))
        return url



class PloneBootstrapBatchView(BootstrapBatchView, PloneBatchView):
    pass
