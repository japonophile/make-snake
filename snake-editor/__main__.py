#!/usr/bin/env python

# __main__.py
#
# Copyright (C) 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import graphics
import theme
import gameloop
import sys

from kano.utils import is_gui

if __name__ == '__main__' and __package__ is None:
    DIR_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    if not DIR_PATH.startswith('/usr'):
        sys.path.insert(1, DIR_PATH)
        LOCALE_PATH = os.path.join(DIR_PATH, 'locale')
    else:
        LOCALE_PATH = None

import kano_i18n.init
kano_i18n.init.install('make-snake', LOCALE_PATH)


def exit():
    """Attempts to tidy up the graphics.
    Finally it calls sys.exit(), since sys is already imported
    """
    graphics.exit()
    sys.exit()


def run():
    try:
        # Init the editor
        graphics.init()
        theme.init()

        # Start the editor
        gameloop.start()

    except KeyboardInterrupt:
        exit()

if not is_gui():
    sys.exit("make-snake requires an X session")

run()
