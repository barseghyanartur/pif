__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2024 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('InvalidRegistryItemType',)


class InvalidRegistryItemType(ValueError):
    """Raised when an attempt is made to register an irrelevant item.

    Raised when an attempt is made to register an item in the registry
    which does not have a proper type.
    """
