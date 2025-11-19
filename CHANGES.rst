Changelog
=========

.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

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
