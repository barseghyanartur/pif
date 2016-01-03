from __future__ import print_function

__title__ = 'pif.checkers.wtfismyip.com.pif_ip_checker'
__author__ = 'Bruno Santeramo'
__copyright__ = 'Copyright (c) 2016 Bruno Santeramo'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('WtfismyipIPChecker',)

from requests import get

from pif.base import BasePublicIPChecker, registry

class WtfismyipIPChecker(BasePublicIPChecker):
    """
    Checks IPs using wtfismyip.com.
    """
    uid = 'wtfismyip.com'

    def get_public_ip(self):
        """
        Gets public IP.

        :return str:
        """
        try:
            data = data = get('http://wtfismyip.com/text').text.rstrip()
            return data
        except Exception as e:
            if self.verbose:
                print(e)


registry.register(WtfismyipIPChecker)
