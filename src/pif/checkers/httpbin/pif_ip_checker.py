from json import loads

from requests import get

from pif.base import BasePublicIPChecker, registry

__author__ = 'Bruno Santeramo'
__copyright__ = 'Copyright (c) 2016-2024 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('HttpbinOrgIPChecker',)


class HttpbinOrgIPChecker(BasePublicIPChecker):
    """Checks IPs using httpbin.org."""

    uid = 'httpbin.org'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            data = loads(get('http://httpbin.org/ip', verify=False).text)
            return data['origin']
        except Exception as err:
            if self.verbose:
                self.logger.error(err)


registry.register(HttpbinOrgIPChecker)
