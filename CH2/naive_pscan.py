#!/usr/bin/env python
"""
Usage:
    naive_pscan -H TARGETHOST -p PORT [-o]
    naive_pscan -H TARGETHOST -p START-END [-o]
    naive_pscan -H TARGETHOST [-o]

Options:
    -h --help               Show this usage.
    -v --version            Show the version.
    -H TARGETHOST           The target host.
    -p (PORT|START-END)     The port to scan.
    -o                      Show open only. [Default: False]
"""
from docopt import docopt
from socket import *
from threading import Thread, Semaphore

screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    """
        A function that will use the socket module in order
        to connect to a certain port in order to check if it
        is open.
    """
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print '[+] %d/tcp open.' % (tgtPort)
        print '[+] %s' % (results)
    except:
        if not arguments['-o']:
            screenLock.acquire()
            print '[+] %d/tcp closed.' % (tgtPort)
    finally:
        screenLock.release()
        connSkt.close()
def portScan(tgtHost, tgtPorts):
    """
        A function that will use the socket module in order
        to scan an iterable of ports, and inform you if they are 
        open or closed.
    """
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unknown host." % (tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan Results for: %s' % (tgtName[0])
    except:
        print '\n[+] Scan Results for: %s' % (tgtIP)
    
    if '-' in tgtPorts:
        tmp = tgtPorts.split('-')
        tgtPorts = [i for i in xrange(int(tmp[0]), int(tmp[1])+1)]
    else:
        tgtPorts = [tgtPorts]
    setdefaulttimeout(1)
    print 'Scanning ports %s.' % (arguments['-p'])
    for tgtPort in tgtPorts:
        thread = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        thread.start()

def main(args):
    """
        The main function that will call all of the exterior
        functions, or it will be the only function.
    """
    portScan(args['-H'], args['-p'])

if __name__ == "__main__":
    arguments = docopt(__doc__, version="Naive Port Scan v1.0.1")
    main(arguments)
