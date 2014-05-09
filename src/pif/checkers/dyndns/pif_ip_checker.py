__title__ = 'pif.checkers.dyndns.pif_ip_checker'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DyndnsIPChecker',)

import re

from requests import get

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
            data = get('http://checkip.dyndns.com/').text
            return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)
        except Exception as e:
            if self.verbose:
                print(e)


registry.register(DyndnsIPChecker)
