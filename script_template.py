#!/usr/bin/env python
"""
Usage:
    naive_pscan -H TARGETHOST -p PORT
    naive_pscan -H TARGETHOST

Options:
    -h --help       Show this usage.
    -v --version    Show the version.
    -H TARGETHOST   The target host.
    -p PORT         The port to scan.
"""
from docopt import docopt

def main(args):
    """
        The main function that will call all of the exterior
        functions, or it will be the only function.
    """
    print args

if __name__ == "__main__":
    arguments = docopt(__doc__, version="1.0.0")
    main(arguments)
