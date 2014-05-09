from __future__ import print_function

__title__ = 'pif.checkers.whatismyip.pif_ip_checker'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('WhatismyipIPChecker',)

import re

from requests import get

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
            data = get('http://www.whatismyip.com/ip-address-lookup/').text
            return re.compile(r'name="IP"(.*) value="(\d+\.\d+\.\d+\.\d+)"').search(data).group(2)
        except Exception as e:
            if self.verbose:
                print(e)


registry.register(WhatismyipIPChecker)
