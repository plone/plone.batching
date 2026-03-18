from pathlib import Path
from setuptools import setup

version = "3.0.0a3.dev0"

long_description = (
    f"{Path('README.rst').read_text()}\n"
    f"{Path('CHANGES.rst').read_text()}\n"
    f"{(Path('docs') / 'usage.rst').read_text()}"
)

# See pyproject.toml for package metadata
setup(
    long_description=Welcome to Plone batching's documentation!
==========================================

This package includes facilities for creating a batched sequence.

It originated from the the PloneBatch module written for Plone which in
itself has been based on Zope2's ZTUtils.Batch.

Changelog
=========

.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

3.0.0a2 (2026-03-16)
--------------------

Internal:


- Update configuration files.
  [plone devs]


3.0.0a1 (2025-11-19)
--------------------

Breaking changes:


- Replace ``pkg_resources`` namespace with PEP 420 native namespace.
  Support only Plone 6.2 and Python 3.10+. (#3928)


2.0.7 (2025-09-10)
------------------

Internal:


- Update configuration files.
  [plone devs] (6e36bcc4)
- Move distribution to src layout [gforcada] (#4217)


2.0.6 (2023-06-16)
------------------

Internal:


- Update configuration files.
  [plone devs] (55bda5c9, 69cb8571, 9e6e627d)


2.0.5 (2023-05-22)
------------------

Internal:


- Update configuration files.
  [plone devs] (12f48b08, 50c0e759)


2.0.4 (2023-03-14)
------------------

Internal:


- Update configuration files.
  [plone devs] (e42131fe)


2.0.3 (2023-02-22)
------------------

Internal:


- Use (GitHub) organization level linting workflow.
  [gforcada] (#1)
- Update package config to use pre-commit.
  [maurits] (#2)


2.0.2 (2023-02-07)
------------------

Bug fixes:


- Declare all dependencies, as reported by z3c.dependencychecker.
  [gforcada] (#1)
- Update tox configuration with dependencies test environments.
  [gforcada] (#1)


2.0.1 (2023-01-26)
------------------

Bug fixes:


- Unify repository configuration via github.com/plone/meta.
  [gforcada] (#1)


Internal:


- Update configuration for default Plone meta.
  [maurits] (#34)


2.0.0 (2022-11-30)
------------------

Bug fixes:


- Final release.
  [gforcada] (#600)


2.0.0a1 (2021-04-21)
--------------------

Breaking changes:


- Update for Plone 6 with Bootstrap markup
  [petschki, agitator] (#28)


New features:


- Include request form parameters from parent request to allow batching in plone.app.standardtiles and filtering with collective.collectionfilter.
  [agitator] (#26)


1.1.6 (2020-04-20)
------------------

Bug fixes:


- Minor packaging updates. (#1)


1.1.5 (2018-11-29)
------------------

Bug fixes:


- Do not show batch navigation for single page with orphan. [maurits] (#9)


1.1.4 (2018-09-27)
------------------

Bug fixes:

- Fix navlist different in Python2 and Python 3 (Refs. #21)
  [ale-rt]

- Python 3 fixes.
  [thet]


1.1.3 (2018-06-04)
------------------

New features:

- Pagination: made label and arrows easier to customise.
  [iham]


1.1.2 (2017-07-20)
------------------

Bug fixes:

- Added missing Zope2 dependency.  [davisagli]


1.1.1 (2016-08-12)
------------------

Fixes:

- Use zope.interface decorator.
  [gforcada]


1.1.0 (2016-02-12)
------------------

.. warning:: Upgrade Warning!
    If you customized the batchnavigation.pt file or use specific CSS styles for it, you might have to update them to reflect the new HTML structure.

New:

- Refactor batchnavigation HTML layout to use nav/ul/li elements instead of div/span.
  [davilima6]

- Switches deprecated ``listingBar`` CSS class to ``pagination``.
  [davilima6]

- Make ellipses stylable and provide more CSS hooks to pagination markup.
  [davilima6]


1.0.8 (unreleased)
------------------

New:

- Make ellipses stylable and provide more CSS hooks to pagination markup. This also deprecates the CSS class ``listingBar`` in favor of more commonly used ``pagination``, which will be the canonical one in Plone 5.0.2 and up.
  [davilima6]


1.0.7 (2016-01-08)
------------------

Fixes:

- Fixed missing test in released package.
  [thet]


1.0.6 (2016-01-08)
------------------

New:

- Introduce a "omit_params" option for the ``make_link`` method and filter out
  ``ajax_load`` by default. When loading the contents with batchnavigation via
  ajax, it doesn't render the links with ajax_load enabled, which would
  probably lead to usability troubles.
  [thet]

Fixes:

- PEP 8, UTF 8 headers, docs cleanup.
  [thet]


1.0.5 (2015-07-18)
------------------

- Make sure pagenumber value is not bigger that numpages
  or it fails in previous_pages when using orphan
  [gbastien]

- Allow orphan size to be equal to batch size. This allows
  the edge case of batch size 0 with default orphan size 0.
  [do3cc]


1.0.4 (2015-04-28)
------------------

- Fix lastpage computation with orphaning
  [gbastien]


1.0.3 (2015-02-20)
------------------

- Fix issue with orphaning
  [do3cc]

1.0.2 (2014-04-13)
------------------

- Fix issue where a start >= end will always return last item.
  https://dev.plone.org/ticket/13880\
  [thepjot]

- Fix multiple_pages if the length of the sequence is exactly the
  page length.
  [gaudenz]

1.0.1 (2014-01-27)
------------------

- Fix issue with sequences when the reported length was different
  than len() iteration would return the full unbatched sequence.
  [alecm]


1.0 (2013-05-23)
----------------

- Use index instead of template attribute in BatchView to be able to customize
  only the template.
  [vincentfretin, thomasdesvenain]

- Fixed wrong msgid for 'First item'.
  [vincentfretin]


1.0b1 (2013-01-17)
------------------

- Nothing changed yet.


1.0a1 (2012-04-25)
------------------

- Factored out Plone batching implementation to separate egg (PLIP #12235)
  [tom_gross]

Usage
=====

A batch defined in plone.batching usually consists of two things:

 1. A batch object.
    This is usually a wrapper for a sequence, which provides slices of information.

 #. A batch view.
    This is needed for display.
    It contains links to navigate to the slices defined in 1.

Both elements can be defined and accessed in Python code AND pagetemplates.

Batch navigation in templates
-----------------------------

For the use of batching features in Page Templates *plone.batching* the first thing you have to do is to create a sequence batch and put it in a template variable named *batch*.
You should do this in a view class if possible::

  <div tal:define="batch view/batchresults;">

or you can do it in the template itself if necessary::

  <div tal:define="Batch python:modules['plone.batching'].Batch;
                   b_size python:30;b_start python:0;b_start request/b_start | b_start;
                   batch python:Batch(results, b_size, int(b_start), orphan=1);">

For the navigation you add the following snippet to your template::

 <tal:batchnavigation
     define="batchnavigation nocall:context/@@batchnavigation"
     replace="structure python:batchnavigation(batch)" />

For backwards compatibility *plone.batching* provides a drop in metal macro *navigation* in the *batch_macros* template.
Add it to the template like this::

 <div metal:use-macro="context/batch_macros/macros/navigation" />


Usage in Python code
--------------------

A batch is instantiated like this::

  >>> from plone.batching import Batch
  >>> batch = Batch(range(100), size=15, orphan=10)

This generates 5 subbatches with 15 items from the sequence [0, 1, ..., 99] and one subbatch with the last 25 items (including 10 orphaned items).
For a detailed description of available parameters for a batch look at the API of the BaseBatch class.

Another way to instaniate a batch is like this::

  >>> batch = Batch.fromPagenumber(range(100), pagesize=15, pagenumber=1)

This results in 6 batches with 15 items and one batch with the last 10 items.
This way of creating a batch is meant as a short cut and does not support all the options the canonical constructor supports.

For big sequences there is another base class provided by the package: *QuantumBatch*.
This batch generates quantum leaps for quicker navigation.

::

  >>> from plone.batching.batch import QuantumBatch
  >>> qb = QuantumBatch(range(1000), 10, start=500, quantumleap=1)
  >>> qb.leapforward
  [69, 84]
  >>> qb.leapback
  [18, 33]

It is possible to navigate the batch stored in the two attributes *leapback* and *leapforward* with 5 clicks.

Usage in Views
--------------

Plone.batching comes with a customizable batch View *batchnavigation* with the view class *BatchView*.
The view comes with a template.
All you have to do, if you want to customize it, is to override the make_link-method.
This method should return a string with the link to the given *pagenumber*.
Here is an example from the folder_contents implementation in plone.app.content::

  >>> from plone.batching.browser import BatchView
  >>> from ZTUtils import make_query

  >>> class MyBatchView(BatchView):
  ...     def make_link(self, pagenumber):
  ...         batchlinkparams = self.request.form.copy()
  ...         return '%s?%s' % (self.request.ACTUAL_URL,
  ...                 make_query(batchlinkparams, {'pagenumber': pagenumber}))

One thing you have to keep in mind is to call the batch view with a batch as the first argument.

::

  >>> from Products.Five import BrowserView
  >>> class MyContentView(BrowserView):
  ...     def batch(self):
  ...         " "  # see above how a batch is defined
  ...
  ...     def batching(self):
  ...         return MyBatchView(self.context, self.request)(self.batch)

Now you can use this in the template of your view.

::

   <div tal:replace="structure view/batching" />

Incompatibilities
-----------------

XXX __len__ method

,
)
