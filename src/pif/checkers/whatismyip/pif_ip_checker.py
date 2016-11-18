import logging
import re

from requests import get

from pif.base import BasePublicIPChecker, registry

__title__ = 'pif.checkers.whatismyip.pif_ip_checker'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('WhatismyipIPChecker',)

logger = logging.getLogger(__name__)


class WhatismyipIPChecker(BasePublicIPChecker):
    """Checks IPs using whatismyip.com."""

    uid = 'whatismyip.com'

    def get_public_ip(self):
        """Gets public IP.

        :return str:
        """
        try:
            data = get('http://www.whatismyip.com/ip-address-lookup/').text
            return re.compile(r'name="ip"(.*) value="(\d+\.\d+\.\d+\.\d+)"') \
                     .search(data) \
                     .group(2)
        except Exception as err:
            if self.verbose:
                logger.error(err)


registry.register(WhatismyipIPChecker)
