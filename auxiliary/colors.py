# colors.py
# description: used for unified color coding
# author: @httphacker

import sys
import string

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        return False
has_colours = has_colours(sys.stdout)

def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[2;%dm" % (30+colour) + text + "\x1b[0m\n"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)