==================================
pif
==================================
Discovers your public IP address using pre-defined checkers (external services).

Installation
==================================
Install with latest stable version from PyPI

    $ pip install pif

or install the latest stable version from source

    $ pip install -e hg+https://bitbucket.org/barseghyanartur/pif@stable#egg=pif

or install into python path

    $ python setup.py install

That's all. See the `Usage and examples` section for more.

Usage and examples
==================================
Basic usage
----------------------------------
Get public IP

>>> from pif import get_public_ip
>>> get_public_ip()

Get public IP using preferred checker

>>> get_public_ip('whatismyip.com')

List available checkers

>>> from pif.utils import list_checkers
>>> list_checkers()

Registering a custom IP checker
----------------------------------
`pif` ships with a number of pre-defined public IP checkers. But you may extend it by defining your own ones as
follows.

>>> from pif.base import BaseIPChecker, registry
>>>
>>> class MyPublicIPChecker(BaseIPChecker):
>>>     uid = 'mypublicipchecker' # UID of the checker
>>>
>>>     def get_public_ip(self):
>>>         # Implement your logic
>>>
>>> registry.register(MyPublicIPChecker) # Register the checker
>>>
>>> get_public_ip('mypublicipchecker') # Get public IP using the preferred checker

Command line usage
----------------------------------
It's possible to generate a signed URL from command line using the `pif.commands.get_public_ip`
module.

>>> optional arguments:
>>>   -h, --help            show this help message and exit
>>>   -c PREFERRED_CHECKER, --checker PREFERRED_CHECKER
>>>                         `preferred_checker` value
>>>   -v VERBOSE, --verbose VERBOSE
>>>                         `verbose` value

:Example: (simple)

    $ get-public-ip

:Example: (with preferred checked and verbose output)

    $ get-public-ip -c whatismyip.com -v 1

License
==================================
GPL 2.0/LGPL 2.1

Support
==================================
For any issues contact me at the e-mail given in the `Author` section.

Author
==================================
Artur Barseghyan <artur.barseghyan@gmail.com>
