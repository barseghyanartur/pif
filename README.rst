===
pif
===
Discovers your public IP address using pre-defined checkers (external services).

Installation
============
Install with latest stable version from PyPI

.. code-block:: sh

    pip install pif

or install the latest stable version from source

.. code-block:: sh

    pip install -e hg+https://bitbucket.org/barseghyanartur/pif@stable#egg=pif

or install into python path

.. code-block:: sh

    python setup.py install

That's all. See the `Usage and examples` section for more.

Usage and examples
==================
Basic usage
-----------
Get public IP

.. code-block:: python

    from pif import get_public_ip
    get_public_ip()

Get public IP using preferred checker

.. code-block:: python

    get_public_ip('v4.ident.me')

List available checkers

.. code-block:: python

    from pif.utils import list_checkers
    list_checkers()

Registering a custom IP checker
-------------------------------
`pif` ships with a number of pre-defined public IP checkers. But you may extend
it by defining your own ones as follows.

.. code-block:: python

    from pif.base import BaseIPChecker, registry

    class MyPublicIPChecker(BaseIPChecker):
        uid = 'mypublicipchecker' # UID of the checker

        def get_public_ip(self):
            # TODO: Implement your logic

    # Register the checker
    registry.register(MyPublicIPChecker)

    # Get public IP using the preferred checker
    get_public_ip('mypublicipchecker')

Command line usage
------------------
It's possible to get your public IP address from command line using the
`pif.commands.get_public_ip` module.

.. code-block:: text

    optional arguments:
      -h, --help            show this help message and exit
      -c PREFERRED_CHECKER, --checker PREFERRED_CHECKER
                            `preferred_checker` value
      -v VERBOSE, --verbose VERBOSE
                        `verbose` value

:Example: (simple)

.. code-block:: sh

    get-public-ip

:Example: (with preferred checked and verbose output)

.. code-block:: sh

    get-public-ip -c v4.ident.me -v 1

Testing
=======
Simply type:

.. code-block:: sh

    ./runtests.py

or use tox:

.. code-block:: sh

    tox

or use tox to check specific env:

.. code-block:: sh

    tox -e py35

License
=======
GPL 2.0/LGPL 2.1

Support
=======
For any issues contact me at the e-mail given in the `Author` section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
