__title__ = 'pif.base'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BasePublicIPChecker', 'registry')

import socket

from pif.conf import get_setting
from pif.exceptions import InvalidRegistryItemType

class BasePublicIPChecker(object):
    """
    Base public IP checker.
    """
    uid = None
    verbose = False

    def __init__(self, verbose=False):
        """
        :param bool verbose:
        """
        assert self.uid
        self.verbose = verbose

    def get_local_ip(self):
        """
        Gets local IP

        :return str:
        """
        return socket.gethostbyname(socket.gethostname())

    def get_public_ip(self):
        """
        Get public IP.

        :return str:
        """
        raise NotImplemented("You should override ``get_ip`` method in your IP checker class.")


class PublicIPCheckerRegistry(object):
    """
    Registry of public IP checkers.
    """
    def __init__(self):
        self._registry = {}
        self._forced = []

    def register(self, cls):
        """
        Registers the IP checker in the registry.

        :param pif.base.BaseIPChecker cls: Subclass of ``pif.base.BaseIPChecker``.
        :param bool force: If set to True, item stays forced. It's not possible to unregister a forced item.
        :return bool: True if registered and False otherwise.
        """
        if not issubclass(cls, BasePublicIPChecker):
            raise InvalidRegistryItemType("Invalid item type `%s` for registry `%s`" % (cls, self.__class__))

        if not cls.uid in self._registry:
            self._registry[cls.uid] = cls
            return True
        else:
            return False

    def unregister(self, checker):
        """
        Unregisters an item from registry.

        :param mixed checker: May be a subclass of ``pif.base.BasePublicIPChecker`` or string, representing
            the checker name.
        :return bool: True if unregistered and False otherwise.
        """
        if not isinstance(checker, str):
            if not issubclass(cls, BasePublicIPChecker):
                raise InvalidRegistryItemType("Invalid item type `%s` for registry `%s`" % (cls, self.__class__))

            checker = cls.uid

        if checker in self._registry:
            self._registry.pop(checker)
            return True
        else:
            return False

    def get(self, uid):
        return self._registry.get(uid, None)


# Register public IP checkers by calling registry.register()
registry = PublicIPCheckerRegistry()