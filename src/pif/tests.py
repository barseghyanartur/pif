__title__ = 'pif.tests'
__version__ = '0.4'
__build__ = 0x000004
__author__ = 'Artur Barseghyan'
__all__ = ('PifTest',)

import unittest

from pif.discover import autodiscover
#from pif.conf import set_setting, get_setting, reset_to_defaults_settings
#from pif import defaults
from pif.utils import get_public_ip, list_checkers
from pif.base import registry, BasePublicIPChecker

PRINT_INFO = True
TRACK_TIME = False

def print_info(func):
    """
    Prints some useful info.
    """
    if not PRINT_INFO:
        return func

    def inner(self, *args, **kwargs):
        if TRACK_TIME:
            import simple_timer
            timer = simple_timer.Timer() # Start timer

        result = func(self, *args, **kwargs)

        if TRACK_TIME:
            timer.stop() # Stop timer

        print '\n%s' % func.__name__
        print '============================'
        print '""" %s """' % func.__doc__.strip()
        print '----------------------------'
        if result is not None: print result
        if TRACK_TIME:
            print 'done in %s seconds' % timer.duration

        return result
    return inner


class PifTest(unittest.TestCase):
    """
    Tests
    """
    def setUp(self):
        pass

    @print_info
    def test_01_autodiscover(self):
        """
        Test ``autodiscover``.
        """
        autodiscover()
        self.assertTrue(len(registry._registry) > 0)

    @print_info
    def test_02_get_public_ip(self):
        """
        Test get IP.
        """
        res = get_public_ip(print_info=True)
        assert res
        return res

    @print_info
    def test_03_get_public_ip_using_preferred_checker_whatismyip(self):
        """
        Test get IP using preferred checker `whatismyip.com`.
        """
        res = get_public_ip('whatismyip.com', print_info=True)
        assert res
        return res

    @print_info
    def test_04_get_public_ip_using_preferred_checker_ident(self):
        """
        Test get IP using preferred checker `ident.me`.
        """
        res = get_public_ip('ident.me', print_info=True)
        assert res
        return res

    @print_info
    def test_05_get_public_ip_using_preferred_checker_dyndns(self):
        """
        Test get IP using preferred checker `dyndns.com`.
        """
        res = get_public_ip('dyndns.com', print_info=True)
        assert res
        return res

    @print_info
    def test_06_list_checkers(self):
        """
        Lists all registered checkers.
        """
        res = list_checkers()
        self.assertTrue(len(res) > 0)
        return res

    @print_info
    def test_07_unregister_checker(self):
        """
        Test unregister checker `dyndns.com`.
        """
        self.assertTrue('dyndns.com' in registry._registry.keys())
        registry.unregister('dyndns.com')
        self.assertTrue('dyndns.com' not in registry._registry.keys())

    @print_info
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
