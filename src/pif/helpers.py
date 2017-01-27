import os

__title__ = 'pif.helpers'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'project_dir',
    'PROJECT_DIR',
)


def project_dir(base):
    """Get absolute project directory path."""
    return os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            (os.path.join(*base) if isinstance(base, (list, tuple)) else base)
        ).replace('\\', '/')
    )


PROJECT_DIR = project_dir
