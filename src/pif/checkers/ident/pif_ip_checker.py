__title__ = 'pif.checkers.ident.pif_ip_checker'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('IdentmeIPChecker', 'V4IdentmeIPChecker', 'V6IdentmeIPChecker')

from six import PY3

try:
    from six.moves.urllib.request import urlopen
except ImportError as e:
    if PY3:
        from urllib.request import urlopen
    else:
        from urllib import urlopen

from pif.base import BasePublicIPChecker, registry

class IdentmeIPChecker(BasePublicIPChecker):
    """
    Checks IPs using ident.me.
    """
    uid = 'ident.me'

    def get_public_ip(self):
        """
        Gets public IP.

        :return str:
        """
        try:
            data = str(urlopen('http://ident.me').read())
            return data
        except Exception as e:
            pass

registry.register(IdentmeIPChecker)


class V4IdentmeIPChecker(BasePublicIPChecker):
    """
    Checks IPs using v4.ident.me.
    """
    uid = 'v4.ident.me'

    def get_public_ip(self):
        """
        Gets public IP.

        :return str:
        """
        try:
            data = str(urlopen('http://v4.ident.me').read())
            return data
        except Exception as e:
            pass

registry.register(V4IdentmeIPChecker)


class V6IdentmeIPChecker(BasePublicIPChecker):
    """
    Checks IPs using v6.ident.me.
    """
    uid = 'v6.ident.me'

    def get_public_ip(self):
        """
        Gets public IP.

        :return str:
        """
        try:
            data = str(urlopen('http://v6.ident.me').read())
            return data
        except Exception as e:
            pass

registry.register(V6IdentmeIPChecker)
