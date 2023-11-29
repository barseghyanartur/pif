from requests import get

from pif.base import BasePublicIPChecker, registry

__author__ = 'Bruno Santeramo'
__copyright__ = 'Copyright (c) 2016-2024 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('IpifyOrgIPChecker',)


class IpifyOrgIPChecker(BasePublicIPChecker):
    """Check IPs using ipify.org."""

    uid = 'ipify.org'

    def get_public_ip(self):
        """Gets public IP.

        :return str:
        """
        try:
            return get('http://api.ipify.org', verify=False).text
        except Exception as err:
            if self.verbose:
                self.logger.error(err)


registry.register(IpifyOrgIPChecker)
