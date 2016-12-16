import logging
import socket

# from .conf import get_setting
from .exceptions import InvalidRegistryItemType

__title__ = 'pif.base'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BasePublicIPChecker',
    'PublicIPCheckerRegistry',
    'registry'
)


class BasePublicIPChecker(object):
    """Base public IP checker."""

    uid = None
    verbose = False

    def __init__(self, verbose=False):
        """Constructor.

        :param bool verbose:
        """
        assert self.uid
        self.verbose = verbose
        self.logger = logging.getLogger(__name__)

    def get_local_ip(self):
        """Get local IP.

        :return str:
        """
        return socket.gethostbyname(socket.gethostname())

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        raise NotImplementedError(
            "You should override ``get_ip`` method in your IP checker class."
        )


class PublicIPCheckerRegistry(object):
    """Registry of public IP checkers."""

    def __init__(self):
        self._registry = {}
        self._forced = []

    @property
    def registry(self):
        """Registry."""
        return self._registry

    def register(self, cls):
        """Register the IP checker in the registry.

        :param pif.base.BaseIPChecker cls: Subclass of
            ``pif.base.BaseIPChecker``.
        :param bool force: If set to True, item stays forced. It's not
            possible to un-register a forced item.
        :return bool: True if registered and False otherwise.
        """
        if not issubclass(cls, BasePublicIPChecker):
            raise InvalidRegistryItemType(
                "Invalid item type `%s` for registry "
                "`%s`" % (cls, self.__class__)
            )

        if cls.uid not in self._registry:
            self._registry[cls.uid] = cls
            return True
        else:
            return False

    def unregister(self, checker):
        """Un-registers an item from registry.

        :param mixed checker: May be a subclass of
            ``pif.base.BasePublicIPChecker`` or string, representing the
            checker name.
        :return bool: True if unregistered and False otherwise.
        """
        # If not string, then we check it it's of a right class.
        if not isinstance(checker, str):
            if not issubclass(checker, BasePublicIPChecker):
                raise InvalidRegistryItemType(
                    "Invalid item type `%s` for registry "
                    "`%s`" % (checker, self.__class__)
                )
            # So, it's the right class.

            checker = checker.uid

        if checker in self._registry:
            self._registry.pop(checker)
            return True
        else:
            return False

    def get(self, uid):
        """Get item from registry.

        :param str uid:
        :return BasePublicIPChecker: Subclass of `BasePublicIPChecker`.
        """
        return self._registry.get(uid, None)


# Register public IP checkers by calling registry.register()
registry = PublicIPCheckerRegistry()
