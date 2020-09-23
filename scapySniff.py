#!/usr/bin/env python3

from scapy.all import *

a = sniff(count=10)
a.summary()