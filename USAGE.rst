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

XXX

Usage in Views
--------------

XXX

Customized batching
-------------------

XXX

Incompatibilities
-----------------

XXX __len__ method

