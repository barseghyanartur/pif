__title__ = 'pif.checkers.whatismyip.pif_ip_checker'
__version__ = '0.5'
__build__ = 0x000005
__author__ = 'Artur Barseghyan'
__all__ = ('WhatismyipIPChecker',)

import re

from six.moves.urllib.request import urlopen
#from urllib import urlopen

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
            data = str(urlopen('http://www.whatismyip.com/ip-tools/ip-address-lookup/').read())
            return re.compile(r'name="IP" value="(\d+\.\d+\.\d+\.\d+)"').search(data).group(1)
        except Exception as e:
            pass

registry.register(WhatismyipIPChecker)
