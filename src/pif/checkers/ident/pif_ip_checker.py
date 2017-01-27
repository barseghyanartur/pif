from requests import get

from pif.base import BasePublicIPChecker, registry

__title__ = 'pif.checkers.ident.pif_ip_checker'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'IdentMeIPChecker',
    'V4IdentMeIPChecker',
    # 'V6IdentMeIPChecker'
)


class IdentMeIPChecker(BasePublicIPChecker):
    """Check IPs using ident.me."""

    uid = 'ident.me'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            return get('http://ident.me', verify=False).text
        except Exception as err:
            if self.verbose:
                self.logger.error(err)


registry.register(IdentMeIPChecker)


class V4IdentMeIPChecker(BasePublicIPChecker):
    """Checks IPs using v4.ident.me."""

    uid = 'v4.ident.me'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            return get('http://v4.ident.me', verify=False).text
        except Exception as err:
            if self.verbose:
                self.logger.error(err)


registry.register(V4IdentMeIPChecker)


# class V6IdentMeIPChecker(BasePublicIPChecker):
#     """Check IPs using v6.ident.me."""

#     uid = 'v6.ident.me'

#     def get_public_ip(self):
#         """Get public IP.

#         :return str:
#         """
#         try:
#             return get('http://v6.ident.me', verify=False).text
#         except Exception as err:
#             if self.verbose:
#                 self.logger.error(err)


# registry.register(V6IdentMeIPChecker)
