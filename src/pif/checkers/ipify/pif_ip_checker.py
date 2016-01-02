#from __future__ import print_function

__title__ = 'pif.checkers.ipify.org.pif_ip_checker'
__author__ = 'Bruno Santeramo'
__copyright__ = 'Copyright (c) 2016 Bruno Santeramo'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('IpifyIPChecker',)

#import re

from requests import get

from pif.base import BasePublicIPChecker, registry

class IpifyIPChecker(BasePublicIPChecker):
    """
    Checks IPs using ipify.org.
    """
    uid = 'ipify.org'

    def get_public_ip(self):
        """
        Gets public IP.

        :return str:
        """
        try:
            data = get('https://api.ipify.org').text
            return data
        except Exception as e:
            if self.verbose:
                print(e)


registry.register(IpifyIPChecker)
