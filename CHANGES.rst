Changelog
=========

1.0.3 (unreleased)
------------------

- Nothing changed yet.


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

