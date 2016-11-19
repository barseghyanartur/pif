import logging

from requests import get

from pif.base import BasePublicIPChecker, registry

__title__ = 'pif.checkers.ipecho.net.pif_ip_checker'
__author__ = 'Bruno Santeramo'
__copyright__ = 'Copyright (c) 2016 Bruno Santeramo'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('IpechoIPChecker',)

logger = logging.getLogger(__name__)


class IpechoIPChecker(BasePublicIPChecker):
    """Check IPs using ipecho.net."""

    uid = 'ipecho.net'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            data = get('http://ipecho.net/plain', verify=False).text
            return data
        except Exception as err:
            if self.verbose:
                logger.error(err)


registry.register(IpechoIPChecker)
