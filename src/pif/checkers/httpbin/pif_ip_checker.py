import logging

from requests import get

from json import loads

from pif.base import BasePublicIPChecker, registry

__title__ = 'pif.checkers.httpbin.org.pif_ip_checker'
__author__ = 'Bruno Santeramo'
__copyright__ = 'Copyright (c) 2016 Bruno Santeramo'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('HttpbinIPChecker',)


logger = logging.getLogger(__name__)


class HttpbinIPChecker(BasePublicIPChecker):
    """Checks IPs using httpbin.org."""

    uid = 'httpbin.org'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            data = loads(get('http://httpbin.org/ip').text)
            return data['origin']
        except Exception as err:
            if self.verbose:
                logger.debug(err)


registry.register(HttpbinIPChecker)
