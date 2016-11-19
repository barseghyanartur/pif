import logging

from requests import get

from pif.base import BasePublicIPChecker, registry

__title__ = 'pif.checkers.ipify.org.pif_ip_checker'
__author__ = 'Bruno Santeramo'
__copyright__ = 'Copyright (c) 2016 Bruno Santeramo'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('IpifyIPChecker',)

logger = logging.getLogger(__name__)


class IpifyIPChecker(BasePublicIPChecker):
    """Check IPs using ipify.org."""

    uid = 'ipify.org'

    def get_public_ip(self):
        """Gets public IP.

        :return str:
        """
        try:
            data = get('http://api.ipify.org', verify=False).text
            return data
        except Exception as err:
            if self.verbose:
                logger.error(err)


registry.register(IpifyIPChecker)
