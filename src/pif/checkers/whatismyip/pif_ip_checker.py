import re

from requests import get

from pif.base import BasePublicIPChecker  # , registry

__title__ = 'pif.checkers.whatismyip.pif_ip_checker'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('WhatismyipComIPChecker',)


class WhatismyipComIPChecker(BasePublicIPChecker):
    """Checks IPs using whatismyip.com."""

    uid = 'whatismyip.com'

    def get_public_ip(self):
        """Gets public IP.

        :return str:
        """
        try:
            data = get(
                'http://www.whatismyip.com/ip-address-lookup/',
                verify=False
            ).text
            return re.compile(r'name="ip"(.*) value="(.+)"') \
                     .search(data) \
                     .group(2)
        except Exception as err:
            if self.verbose:
                self.logger.error(err)


# registry.register(WhatismyipComIPChecker)
