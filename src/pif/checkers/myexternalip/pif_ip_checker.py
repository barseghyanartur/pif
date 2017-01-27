from requests import get

from pif.base import BasePublicIPChecker, registry

__title__ = 'pif.checkers.myexternalip.pif_ip_checker'
__author__ = 'Syradium'
__copyright__ = 'Copyright (c) 2016 Syradium'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('MyExternalIPOrgIPChecker',)


class MyExternalIPOrgIPChecker(BasePublicIPChecker):
    """Check IPs using myexternalip.com."""

    uid = 'myexternalip.com'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            return get('http://myexternalip.com/raw').text.rstrip()
        except Exception as err:
            if self.verbose:
                self.logger.error(err)


registry.register(MyExternalIPOrgIPChecker)
