__title__ = 'pif.checkers.whatismyip.pif_ip_checker'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('WhatismyipIPChecker',)

import re

from six import PY3

try:
    from six.moves.urllib.request import urlopen
except ImportError as e:
    if PY3:
        from urllib.request import urlopen
    else:
        from urllib import urlopen

from pif.base import BasePublicIPChecker, registry

class WhatismyipIPChecker(BasePublicIPChecker):
    """
    Checks IPs using whatismyip.com.
    """
    uid = 'whatismyip.com'

    def get_public_ip(self):
        """
        Gets public IP.

        :return str:
        """
        try:
            data = str(urlopen('http://www.whatismyip.com/ip-address-lookup/').read())
            return re.compile(r'name="IP"(.*) value="(\d+\.\d+\.\d+\.\d+)"').search(data).group(2)
        except Exception as e:
            pass

registry.register(WhatismyipIPChecker)
