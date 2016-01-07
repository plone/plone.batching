# -*- coding: utf-8 -*-
from Acquisition import aq_parent
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import queryMultiAdapter
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
        query_params = {}
        query_params.update(self.request.form)
        if self.batchformkeys:
            for key in query_params.keys():
                if key not in self.batchformkeys:
                    del query_params[key]
        if omit_params:
            for key in omit_params:
                if key in query_params:
                    del query_params[key]

        def _get_context(ctx):
            """Return the context which should be used to generate the url.
            If it's a default view, return walk up the hierachy until the
            originating context is found.
            """
            # Plone soft-dependency. If no adapter is found, just return ctx.
            context_state = queryMultiAdapter(
                (ctx, self.request), name='plone_context_state')
            if context_state and context_state.is_default_page():
                return _get_context(aq_parent(ctx))
            return ctx
        context = _get_context(self.context)

        start = max(pagenumber - 1, 0) * self.batch.pagesize
        query_params[self.batch.b_start_str] = start
        url = u"{0}?{1}".format(
            context.absolute_url(),
            make_query(query_params)
        )
        return url


class PloneBootstrapBatchView(BootstrapBatchView, PloneBatchView):
    pass
