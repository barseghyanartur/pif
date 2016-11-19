import logging

from requests import get

from pif.base import BasePublicIPChecker, registry

__title__ = 'pif.checkers.tnx.nl.pif_ip_checker'
__author__ = 'Bruno Santeramo'
__copyright__ = 'Copyright (c) 2016 Bruno Santeramo'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('TnxIPChecker',)

logger = logging.getLogger(__name__)


class TnxIPChecker(BasePublicIPChecker):
    """Check IPs using tnx.nl."""

    uid = 'tnx.nl'

    def get_public_ip(self):
        """Get public IP.

        :return str:
        """
        try:
            data = get('http://tnx.nl/ip', verify=False).text.rstrip()
            return data
        except Exception as err:
            if self.verbose:
                logger.error(err)


registry.register(TnxIPChecker)
