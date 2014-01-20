from __future__ import print_function

__title__ = 'pif.__init__'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('autodiscover',)

import os
import logging

try:
    from importlib import import_module
except ImportError:
    import_module = __import__

from pif.helpers import PROJECT_DIR
from pif.conf import get_setting

logger = logging.getLogger(__name__)

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
                    logger.debug(str(e))
            except Exception as e:
                if DEBUG:
                    logger.debug(str(e))
        else:
            pass
