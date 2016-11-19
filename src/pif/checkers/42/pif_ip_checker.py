import logging

from requests import get

from pif.base import BasePublicIPChecker, registry

__title__ = 'pif.checkers.42.pl.pif_ip_checker'
__author__ = 'Bruno Santeramo'
__copyright__ = 'Copyright (c) 2016 Bruno Santeramo'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Ip42IPChecker',)

logger = logging.getLogger(__name__)


class Ip42IPChecker(BasePublicIPChecker):
    """Checks IPs using ipecho.net."""

    uid = 'ip.42.pl'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            data = get('http://ip.42.pl/raw', verify=False).text
            return data
        except Exception as err:
            if self.verbose:
                logging.error(err)


registry.register(Ip42IPChecker)
