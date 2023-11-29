from requests import get

from pif.base import BasePublicIPChecker, registry

__author__ = 'Bruno Santeramo'
__copyright__ = 'Copyright (c) 2016-2024 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('IpechoNetIPChecker',)


class IpechoNetIPChecker(BasePublicIPChecker):
    """Check IPs using ipecho.net."""

    uid = 'ipecho.net'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            return get('http://ipecho.net/plain', verify=False).text
        except Exception as err:
            if self.verbose:
                self.logger.error(err)


registry.register(IpechoNetIPChecker)
