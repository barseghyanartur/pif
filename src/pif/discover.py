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
    ip_checkers_dir = get_setting('IP_CHECKERS_DIR')
    ip_checker_module_name = get_setting('IP_CHECKER_MODULE_NAME')
    debug = get_setting('DEBUG')

    for app_path in os.listdir(PROJECT_DIR(ip_checkers_dir)):
        full_app_path = [ip_checkers_dir]
        full_app_path.append(app_path)
        if os.path.isdir(PROJECT_DIR(full_app_path)):
            try:
                import_module(
                    "pif.%s.%s.%s" % (ip_checkers_dir,
                                      app_path,
                                      ip_checker_module_name)
                )
            except ImportError as err:
                if debug:
                    logger.debug(str(err))
            except Exception as err:
                if debug:
                    logger.debug(str(err))
        else:
            pass
