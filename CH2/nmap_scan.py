#!/usr/bin/env python
"""
Usage:
    nmap_scan -H TARGETHOST -p PORT [-o]
    nmap_scan -H TARGETHOST [-o]

Options:
    -h --help       Show this usage.
    -v --version    Show the version.
    -H TARGETHOST   The target host.
    -p PORT         The port to scan.
    -o              Show only open ports. [Default: False]
"""
from docopt import docopt
import nmap

def nmapScan(tgtHost, tgtPort):
    """
        The actual scanning of the host occurs here.
    """
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    if state == 'open' or not arguments["-o"]:
        print ' [*] %s tcp/ %s %s' % (tgtHost, tgtPort, state)

def main(args):
    """
        This is a python port scanner that uses the nmap
        library to do the majority of the work.
    """
    if '-' in args['-p']:
        tmp = args['-p'].split('-')
        tgtPorts = [str(i) for i in xrange(int(tmp[0]), int(tmp[1])+1)]
    else:
        tgtPorts = [args['-p']]
    tgtHost = args['-H']
    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)

if __name__ == "__main__":
    arguments = docopt(__doc__, version="Nmap scan v1.0.0")
    main(arguments)
