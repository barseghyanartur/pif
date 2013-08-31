__title__ = 'pif.exceptions'
__version__ = '0.4'
__build__ = 0x000004
__author__ = 'Artur Barseghyan'
__all__ = ('InvalidRegistryItemType',)

class InvalidRegistryItemType(ValueError):
    """
    Raised when an attempt is made to register an item in the registry which does not have a proper type.
    """