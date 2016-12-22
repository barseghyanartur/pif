from __future__ import print_function

import logging
import unittest

from .base import BasePublicIPChecker, registry
from .utils import get_public_ip, list_checkers, ensure_autodiscover
from .discover import autodiscover

__title__ = 'pif.tests'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'log_info',
    'PifTest',
)

LOG_INFO = True

LOGGER = logging.getLogger(__name__)


def log_info(func):
    """Prints some useful info."""
    if not LOG_INFO:
        return func

    def inner(self, *args, **kwargs):
        result = func(self, *args, **kwargs)

        LOGGER.info('\n%s', func.__name__)
        LOGGER.info('============================')
        LOGGER.info('""" %s """', func.__doc__.strip())
        LOGGER.info('----------------------------')
        if result is not None:
            LOGGER.info(result)

        return result
    return inner


class PifTest(unittest.TestCase):
    """Tests."""

    def setUp(self):
        """Set up."""
        pass

    @log_info
    def test_01_autodiscover(self):
        """Test ``autodiscover``."""
        autodiscover()
        self.assertTrue(len(registry.registry) > 0)

    @log_info
    def test_02_get_public_ip(self):
        """Test get IP."""
        res = get_public_ip(verbose=True)
        self.assertIsNotNone(res)
        return res

    @log_info
    def _test_get_public_ip_using_preferred_checker(self, checker):
        """Test get_public_ip using preferred checker."""
        res = get_public_ip(checker, verbose=True)
        return res

    @log_info
    def test_03_get_public_ip_using_preferred_checker(self):
        """Test get IP using preferred checker `ident.me`."""
        checkers = list_checkers()
        res = {}
        failed = []
        for checker in checkers:
            _res = self._test_get_public_ip_using_preferred_checker(checker)
            if _res is None:
                failed.append(checker)
            res.update({checker: _res})
        self.assertTrue(
            len(failed) == 0,
            "Failed for {}".format(','.join(failed))
        )
        return res

    @log_info
    def test_04_list_checkers(self):
        """Lists all registered checkers."""
        res = list_checkers()
        self.assertTrue(len(res) > 0)
        return res

    @log_info
    def test_05_unregister_checker(self):
        """Test un-register checker `dyndns.com`."""
        self.assertTrue('dyndns.com' in registry.registry.keys())
        registry.unregister('dyndns.com')
        self.assertTrue('dyndns.com' not in registry.registry.keys())

    @log_info
    def test_06_register_custom_checker(self):
        """Test un-register checker `dyndns`."""
        class MyPublicIPChecker(BasePublicIPChecker):
            """MyPublicIPChecker."""

            uid = 'mypublicipchecker'

            def get_public_ip(self):
                """Get public IP."""
                return '8.8.8.8'

        registry.register(MyPublicIPChecker)
        self.assertTrue('mypublicipchecker' in registry.registry.keys())

    @log_info
    def test_07_get_local_ip(self):
        """Test get local IP."""
        ensure_autodiscover()
        ip_checker_cls = list(registry.registry.values())[0]

        ip_checker = ip_checker_cls(verbose=False)
        local_ip = ip_checker.get_local_ip()
        self.assertIsNotNone(local_ip)


if __name__ == '__main__':
    unittest.main()
