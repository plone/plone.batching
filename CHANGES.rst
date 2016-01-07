Changelog
=========

1.0.6 (unreleased)
------------------

New:

- For generating the batching urls, don't use ACTUAL_URL, but the context's
  absolute_url. This allows for mutliple batchnavigations on different contexts
  shown on one page via some collage or mosaic view.
  ATTENTION: CAN'T BE DONE THAT WAY!
  PROBLEM: On views, which are no defaultView but explicitly called (e.g.
  ``@@folder_contents``), the links would be generated wrong. Couldn't
  determine the actual shown view within one request cycle, so I gave up on
  this. It's just a corne use case anyways...

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

- Factored out Plone batching implementation to seperate egg (PLIP #12235)
  [tom_gross]
