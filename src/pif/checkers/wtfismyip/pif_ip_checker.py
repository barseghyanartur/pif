from requests import get

from pif.base import BasePublicIPChecker, registry

__author__ = 'Bruno Santeramo'
__copyright__ = 'Copyright (c) 2016-2024 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('WtfismyipComIPChecker',)


class WtfismyipComIPChecker(BasePublicIPChecker):
    """Checks IPs using wtfismyip.com."""

    uid = 'wtfismyip.com'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            return get('http://wtfismyip.com/text', verify=False).text.rstrip()
        except Exception as err:
            if self.verbose:
                self.logger.error(err)


registry.register(WtfismyipComIPChecker)
