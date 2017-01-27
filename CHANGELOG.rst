Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: text

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.8.2
-----
2016-12-22

- Minor code clean up and pep8 fixes.
- Added testing against PyPy.

0.8.1
-----
2016-11-24

- Minor improvements.

0.8
---
2016-11-20

- Fixed broken checkers.
- Rename several checker modules and classes.

0.7.4
-----
2016-11-19

- Fixed broken checkers.
- Added additional checkers.

0.7.3
-----
2016-01-23

- Added additional checkers.

0.7.2
-----
2016-01-03

- Added additional checkers.

0.7.1
-----
2014-10-09

- Added `argparse` to requirements.

0.7
---
2014-05-09

- Added command line tools.
- The ``print_info`` argument of the ``pif.utils.get_public_ip`` function is
  replaced with ``verbose``.
- The ``requests`` library is used instead of standard urlopen.

0.6
---
2014-01-20

- Lowered `six` requirement to 1.1.0.
- Fixes to whatsmyip checker (caused by changed whatsmyip api).

0.5
---
2013-09-06

- Python 3 support
