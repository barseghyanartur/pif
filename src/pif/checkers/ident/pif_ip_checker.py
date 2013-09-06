__title__ = 'pif.checkers.ident.pif_ip_checker'
__version__ = '0.5'
__build__ = 0x000005
__author__ = 'Artur Barseghyan'
__all__ = ('IdentmeIPChecker', 'V4IdentmeIPChecker', 'V6IdentmeIPChecker')

from six.moves.urllib.request import urlopen
#from urllib import urlopen

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
