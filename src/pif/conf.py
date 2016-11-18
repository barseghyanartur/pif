from . import defaults

__title__ = 'pif.conf'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'get_setting',
    'set_setting',
    'settings',
    'reset_to_defaults_settings',
)


class Settings(object):
    """Settings registry."""

    def __init__(self):
        self._settings = {}

    def set(self, name, value):
        """Override default settings.

        :param str name:
        :param mixed value:
        """
        self._settings[name] = value

    def get(self, name, default=None):
        """Get a variable from local settings.

        :param str name:
        :param mixed default: Default value.
        :return mixed:
        """
        if name in self._settings:
            return self._settings.get(name, default)
        elif hasattr(defaults, name):
            return getattr(defaults, name, default)
        else:
            return default

    def reset_to_defaults(self):
        """Resets settings to defaults."""
        self._settings = {}


settings = Settings()

get_setting = settings.get

set_setting = settings.set

reset_to_defaults_settings = settings.reset_to_defaults
