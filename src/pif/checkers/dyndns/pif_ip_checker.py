__title__ = 'pif.checkers.dyndns.pif_ip_checker'
__version__ = '0.5'
__build__ = 0x000005
__author__ = 'Artur Barseghyan'
__all__ = ('DyndnsIPChecker',)

import re

from six.moves.urllib.request import urlopen
#from urllib import urlopen

from pif.base import BasePublicIPChecker, registry

class DyndnsIPChecker(BasePublicIPChecker):
    """
    Checks IPs using checkip.dyndns.com.
    """
    uid = 'dyndns.com'

    def get_public_ip(self):
        """
        Gets public IP.

        :return str:
        """
        try:
            data = str(urlopen('http://checkip.dyndns.com/').read())
            return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)
        except Exception as e:
            pass

registry.register(DyndnsIPChecker)
