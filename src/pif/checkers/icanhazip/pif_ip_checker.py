import logging

from requests import get

from pif.base import BasePublicIPChecker, registry

__title__ = 'pif.checkers.icanhazip.com.pif_ip_checker'
__author__ = 'Bruno Santeramo'
__copyright__ = 'Copyright (c) 2016 Bruno Santeramo'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('IcanhazipIPChecker',)

logger = logging.getLogger(__name__)


class IcanhazipIPChecker(BasePublicIPChecker):
    """Check IPs using icanhazip.com."""

    uid = 'icanhazip.com'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            data = get('http://icanhazip.com/', verify=False).text.rstrip()
            return data
        except Exception as err:
            if self.verbose:
                logger.debug(err)


registry.register(IcanhazipIPChecker)
