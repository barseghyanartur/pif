__title__ = 'pif.__init__'
__version__ = '0.5'
__build__ = 0x000005
__author__ = 'Artur Barseghyan'
__all__ = ('autodiscover',)

import os

try:
    from importlib import import_module
except ImportError:
    import_module = __import__

from six import print_

from pif.helpers import PROJECT_DIR
from pif.conf import get_setting

def autodiscover():
    """
    Autodiscovers the pif IP checkers in checkers directory.
    """
    IP_CHECKERS_DIR = get_setting('IP_CHECKERS_DIR')
    IP_CHECKER_MODULE_NAME = get_setting('IP_CHECKER_MODULE_NAME')
    DEBUG = get_setting('DEBUG')

    for app_path in os.listdir(PROJECT_DIR(IP_CHECKERS_DIR)):
        full_app_path = [IP_CHECKERS_DIR]
        full_app_path.append(app_path)
        if os.path.isdir(PROJECT_DIR(full_app_path)):
            try:
                import_module(
                    "pif.%s.%s.%s" % (IP_CHECKERS_DIR, app_path, IP_CHECKER_MODULE_NAME)
                    )
            except ImportError as e:
                if DEBUG:
                    print_(e)
            except Exception as e:
                if DEBUG:
                    print_(e)
        else:
            pass
