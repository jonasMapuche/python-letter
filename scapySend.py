#!/usr/bin/env python3

from scapy.all import *

alvo = "192.168.15.101"
interface = "wlp6s0"

send(IP(dst=alvo)/ICMP())
sendp(Ether()/IP(dst=alvo,ttl=(1,4)),iface=interface)
