import logging

from requests import get

from pif.base import BasePublicIPChecker, registry

__title__ = 'pif.checkers.myexternalip.com.pif_ip_checker'
__author__ = 'Syradium'
__copyright__ = 'Copyright (c) 2016 Syradium'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('MyExternalIPChecker',)

logger = logging.getLogger(__name__)


class MyExternalIPChecker(BasePublicIPChecker):
    """Check IPs using myexternalip.com."""

    uid = 'myexternalip.com'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            data = get('http://myexternalip.com/raw').text.rstrip()
            return data
        except Exception as err:
            if self.verbose:
                logger.error(err)


registry.register(MyExternalIPChecker)
