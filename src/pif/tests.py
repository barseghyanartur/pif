from __future__ import print_function

__title__ = 'pif.tests'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('log_info', 'PifTest',)

import unittest
import logging

from pif.discover import autodiscover
from pif.utils import get_public_ip, list_checkers
from pif.base import registry, BasePublicIPChecker

LOG_INFO = True
TRACK_TIME = False

logger = logging.getLogger(__name__)

def log_info(func):
    """
    Prints some useful info.
    """
    if not LOG_INFO:
        return func

    def inner(self, *args, **kwargs):
        if TRACK_TIME:
            import simple_timer
            timer = simple_timer.Timer() # Start timer

        result = func(self, *args, **kwargs)

        if TRACK_TIME:
            timer.stop() # Stop timer

        logger.info('\n{0}'.format(func.__name__))
        logger.info('============================')
        logger.info('""" {0} """'.format(func.__doc__.strip()))
        logger.info('----------------------------')
        if result is not None:
            logger.info(result)
        if TRACK_TIME:
            logger.info('done in {0} seconds'.format(timer.duration))

        return result
    return inner


class PifTest(unittest.TestCase):
    """
    Tests
    """
    def setUp(self):
        pass

    @log_info
    def test_01_autodiscover(self):
        """
        Test ``autodiscover``.
        """
        autodiscover()
        self.assertTrue(len(registry._registry) > 0)

    @log_info
    def test_02_get_public_ip(self):
        """
        Test get IP.
        """
        res = get_public_ip(verbose=True)
        assert res
        return res

    @log_info
    def test_03_get_public_ip_using_preferred_checker_whatismyip(self):
        """
        Test get IP using preferred checker `whatismyip.com`.
        """
        res = get_public_ip('whatismyip.com', verbose=True)
        assert res
        return res

    @log_info
    def test_04_get_public_ip_using_preferred_checker_ident(self):
        """
        Test get IP using preferred checker `ident.me`.
        """
        res = get_public_ip('ident.me', verbose=True)
        assert res
        return res

    @log_info
    def test_05_get_public_ip_using_preferred_checker_dyndns(self):
        """
        Test get IP using preferred checker `dyndns.com`.
        """
        res = get_public_ip('dyndns.com', verbose=True)
        assert res
        return res

    @log_info
    def test_06_list_checkers(self):
        """
        Lists all registered checkers.
        """
        res = list_checkers()
        self.assertTrue(len(res) > 0)
        return res

    @log_info
    def test_07_unregister_checker(self):
        """
        Test unregister checker `dyndns.com`.
        """
        self.assertTrue('dyndns.com' in registry._registry.keys())
        registry.unregister('dyndns.com')
        self.assertTrue('dyndns.com' not in registry._registry.keys())

    @log_info
    def test_08_register_custom_checker(self):
        """
        Test unregister checker `dyndns`.
        """
        class MyPublicIPChecker(BasePublicIPChecker):
            uid = 'mypublicipchecker'

            def get_public_ip(self):
                return '8.8.8.8'

        registry.register(MyPublicIPChecker)
        self.assertTrue('mypublicipchecker' in registry._registry.keys())


if __name__ == '__main__':
    unittest.main()
