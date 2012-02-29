A batch defined in plone.batching usually consists of two things:

 1. A batch object. This is usually a wrapper for a sequence, which
    provides slices of information
 #. A batch view. This is needed for display. It contains links to
    navigate to the slices defined in 1.

Both elements can be defined and accessed in Python code AND pagetemplates.

Batch navigation in templates
-----------------------------

For the use of batching features in Page Templates *plone.batching* 
the first thing you have to do is to create a sequence batch and put
it in a template variable named *batch*.
You should do this in a view class if possible ::

  <div tal:define="batch view/batchresults;">

or you can do it in the template itself if necessary  ::

  <div tal:define="Batch python:modules['Products.CMFPlone'].Batch;
                   b_size python:30;b_start python:0;b_start request/b_start | b_start;
                   batch python:Batch(results, b_size, int(b_start), orphan=1);">

For the navigation you add the following snippet to your template ::

 <tal:batchnavigation
     define="batchnavigation nocall:context/@@batchnavigation"
     replace="structure python:batchnavigation(batch)" />

For backwards compatibility *plone.batching* provides a drop in metal macro 
*navigation* in the *batch_macros* template. Add it to the template like this::

 <div metal:use-macro="context/batch_macros/macros/navigation" />


Usage in Python code
--------------------

A batch is instantiated like this: ::

  >>> from plone.batching import Batch
  >>> batch = Batch(range(100), size=15, orphan=10)

This generates 5 subbatches with 15 items from the sequence [0, 1, ..., 99]
and one subbatch with the last 25 items (including 10 orphaned items).
For a detailed description of available parameters for a batch 
look at the API of the BaseBatch class.
 
Another way to instaniate a batch is like this: ::

  >>> batch = Batch.fromPagenumber(range(100), pagesize=15, pagenumber=1)
  
This results in 6 batches with 15 items and one batch with the last 10 items.
This way of creating a batch is meant as a short cut and does not support
all the options the canonical constructor supports.

For big sequences there is another base class provided by the package:
*QuantumBatch*. This batch generates quantum leaps for quicker navigation. ::

  >>> from plone.batching.batch import QuantumBatch
  >>> qb = QuantumBatch(range(1000), 10, start=500, quantumleap=1)
  >>> qb.leapforward
  [69, 84]
  >>> qb.leapback
  [18, 33]

It is possible to navigate the batch stored in the two attributes
*leapback* and *leapforward* with 5 clicks.

Usage in Views
--------------

Plone.batching comes with a customizable batch View *batchnavigation* with
the view class *BatchView*. The view comes with a template. All you have to
do, if you want to customize it, is to override the make_link-method.
This method should return a string with the link to the given *pagenumber*.
Here is an example from the folder_contents implementation in
plone.app.content: ::

  >>> from plone.batching.browser import BatchView
  >>> from ZTUtils import make_query

  >>> class MyBatchView(BatchView):
  ...     def make_link(self, pagenumber):
  ...         batchlinkparams = self.request.form.copy()
  ...         return '%s?%s' % (self.request.ACTUAL_URL,
  ...                 make_query(batchlinkparams, {'pagenumber': pagenumber}))

One thing you have to keep in mind is to call the batch view with a batch as
the first argument. ::

  >>> class MyContentView(BrowserView):
  ...     def batch(self):
  ...         " "  # see above how a batch is defined
  ...     
  ...     def batching(self):
  ...         return MyBatchView(self.context, self.request)(self.batch)

Now you can use this in the template of your view. ::

   <div tal:replace="structure view/batching" />

Incompatibilities
-----------------

XXX __len__ method

