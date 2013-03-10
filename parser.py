#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as ET

def usage():
    print("usage: ./parser.py <NETXML-FILE>")

if 2 != len(sys.argv):
    usage()
    sys.exit(1)
