import logging

from requests import get

from pif.base import BasePublicIPChecker, registry

__title__ = 'pif.checkers.ident.pif_ip_checker'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'IdentmeIPChecker',
    'V4IdentmeIPChecker',
    'V6IdentmeIPChecker'
)

logger = logging.getLogger(__name__)


class IdentmeIPChecker(BasePublicIPChecker):
    """Check IPs using ident.me."""

    uid = 'ident.me'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            data = get('http://ident.me', verify=False).text
            return data
        except Exception as err:
            if self.verbose:
                logger.error(err)


registry.register(IdentmeIPChecker)

# ********************************************************
# ********************************************************
# ********************************************************


class V4IdentmeIPChecker(BasePublicIPChecker):
    """Checks IPs using v4.ident.me."""

    uid = 'v4.ident.me'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            data = get('http://v4.ident.me', verify=False).text
            return data
        except Exception as err:
            if self.verbose:
                logger.error(err)


registry.register(V4IdentmeIPChecker)

# ********************************************************
# ********************************************************
# ********************************************************


class V6IdentmeIPChecker(BasePublicIPChecker):
    """Check IPs using v6.ident.me."""

    uid = 'v6.ident.me'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            data = get('http://v6.ident.me', verify=False).text
            return data
        except Exception as err:
            if self.verbose:
                logger.error(err)


registry.register(V6IdentmeIPChecker)
