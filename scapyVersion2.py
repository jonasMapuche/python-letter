from scapy.all import IP

p = sr1(IP(src="192.168.15.9",dst="192.168.15.101")/ICMP()/"Hello World")

print(p.show())

alvo = "192.168.15.101"
ip = IP()
ping = ICMP()
ip.dist = alvo
resp = sr1(ip/ping)
res = sr1(ARP(pdst=alvo))
if resp.tt1 < 65:
    print ("linux")
else:
    print ("windows")
    