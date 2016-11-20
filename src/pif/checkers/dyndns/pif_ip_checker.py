import re

from requests import get

from pif.base import BasePublicIPChecker, registry

__title__ = 'pif.checkers.dyndns.pif_ip_checker'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DyndnsComIPChecker',)


class DyndnsComIPChecker(BasePublicIPChecker):
    """Checks IPs using checkip.dyndns.com."""

    uid = 'dyndns.com'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            data = get('http://checkip.dyndns.com/', verify=False).text
            if data:
                return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)') \
                         .search(data) \
                         .group(1)
        except Exception as err:
            if self.verbose:
                self.logger.error(err)


registry.register(DyndnsComIPChecker)
