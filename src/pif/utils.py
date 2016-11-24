import logging

from pif.base import registry
from pif.discover import autodiscover

__title__ = 'pif.utils'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'ensure_autodiscover',
    'list_checkers',
    'get_public_ip',
)

logger = logging.getLogger(__name__)


def ensure_autodiscover():
    """Ensure the IP checkers are auto-discovered."""
    if not registry.registry:
        autodiscover()


def list_checkers():
    """List available checkers.

    :return list:
    """
    ensure_autodiscover()
    return registry.registry.keys()


def get_public_ip(preferred_checker=None, verbose=False):
    """Get IP using one of the services.

    :param str preferred_checker: Checker UID. If given, the preferred
        checker is used.
    :param bool verbose: If set to True, debug info is printed.
    :return str:
    """
    ensure_autodiscover()

    # If use preferred checker.
    if preferred_checker:
        ip_checker_cls = registry.get(preferred_checker)

        if not ip_checker_cls:
            return False

        ip_checker = ip_checker_cls(verbose=verbose)
        ip = ip_checker.get_public_ip()

        if verbose:
            logger.info(
                'provider: {}'.format(ip_checker_cls.__name__)
            )
        return ip

    # Using all checkers.

    for ip_checker_name, ip_checker_cls in registry.registry.items():
        ip_checker = ip_checker_cls(verbose=verbose)
        try:
            ip = ip_checker.get_public_ip()
            if ip:
                if verbose:
                    logger.info(
                        'provider: {}'.format(ip_checker_cls.__name__)
                    )
                return ip

        except Exception as err:
            if verbose:
                logger.error(err)

    return False
