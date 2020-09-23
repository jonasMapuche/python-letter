#!/usr/bin/env python3

import sys
from scapy.all import sr1,IP,ICMP

alvo = sys.argv[1]

p=sr1(IP(dst=alvo)/ICMP())

if p:
    p.show()
