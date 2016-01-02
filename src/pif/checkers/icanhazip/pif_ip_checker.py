#from __future__ import print_function

__title__ = 'pif.checkers.icanhazip.com.pif_ip_checker'
__author__ = 'Bruno Santeramo'
__copyright__ = 'Copyright (c) 2016 Bruno Santeramo'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('IcanhazipIPChecker',)

#import re

from requests import get

from pif.base import BasePublicIPChecker, registry

class IcanhazipIPChecker(BasePublicIPChecker):
    """
    Checks IPs using icanhazip.com.
    """
    uid = 'icanhazip.com'

    def get_public_ip(self):
        """
        Gets public IP.

        :return str:
        """
        try:
            data = get('http://icanhazip.com/').text.rstrip()
            return data
        except Exception as e:
            if self.verbose:
                print(e)


registry.register(IcanhazipIPChecker)
