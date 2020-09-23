#!/usr/bin/env python3

from scapy.all import *

def arp_monitor(pkt):
    if ARP in pkt and pkt[ARP].op in (1,2):
        return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")

sniff(prn=arp_monitor,filter="arp",store=0)