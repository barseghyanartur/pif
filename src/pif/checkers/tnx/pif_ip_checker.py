from requests import get

from pif.base import BasePublicIPChecker, registry

__title__ = 'pif.checkers.tnx.pif_ip_checker'
__author__ = 'Bruno Santeramo'
__copyright__ = 'Copyright (c) 2016 Bruno Santeramo'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('TnxNlIPChecker',)


class TnxNlIPChecker(BasePublicIPChecker):
    """Check IPs using tnx.nl."""

    uid = 'tnx.nl'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            data = get('http://tnx.nl/ip', verify=False).text.rstrip()
            return data
        except Exception as err:
            if self.verbose:
                self.logger.error(err)


registry.register(TnxNlIPChecker)
