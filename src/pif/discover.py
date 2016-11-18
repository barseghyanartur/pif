from __future__ import print_function

import os
import logging

from .helpers import PROJECT_DIR
from .conf import get_setting

try:
    from importlib import import_module
except ImportError:
    import_module = __import__

__title__ = 'pif.discover'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('autodiscover',)


logger = logging.getLogger(__name__)


def autodiscover():
    """Autodiscovers the pif IP checkers in checkers directory."""
    IP_CHECKERS_DIR = get_setting('IP_CHECKERS_DIR')
    IP_CHECKER_MODULE_NAME = get_setting('IP_CHECKER_MODULE_NAME')
    DEBUG = get_setting('DEBUG')

    for app_path in os.listdir(PROJECT_DIR(IP_CHECKERS_DIR)):
        full_app_path = [IP_CHECKERS_DIR]
        full_app_path.append(app_path)
        if os.path.isdir(PROJECT_DIR(full_app_path)):
            try:
                import_module(
                    "pif.%s.%s.%s" % (IP_CHECKERS_DIR,
                                      app_path,
                                      IP_CHECKER_MODULE_NAME)
                )
            except ImportError as e:
                if DEBUG:
                    logger.debug(str(e))
            except Exception as e:
                if DEBUG:
                    logger.debug(str(e))
        else:
            pass
