#/usr/bin/env python3

from scapy.all import *

alvo = "192.168.15.101"
message = "Hello World!"

ans,unans=sr(IP(dst=alvo,ttl=5)/ICMP())

ans.nsummary()
unans.nsummary()

p=sr1(IP(dst=alvo)/ICMP()/message)
p.show()