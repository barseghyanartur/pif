from __future__ import print_function

__title__ = 'pif.checkers.myexternalip.com.pif_ip_checker'
__author__ = 'Syradium'
__copyright__ = 'Copyright (c) 2016 Syradium'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('MyExternalIPChecker',)

from requests import get
from pif.base import BasePublicIPChecker, registry


class MyExternalIPChecker(BasePublicIPChecker):
    """
    Checks IPs using myexternalip.com.
    """
    uid = 'myexternalip.com'

    def get_public_ip(self):
        """
        Gets public IP.

        :return str:
        """
        try:
            data = get('http://myexternalip.com/raw').text.rstrip()
            return data
        except Exception as e:
            if self.verbose:
                print(e)


registry.register(MyExternalIPChecker)
