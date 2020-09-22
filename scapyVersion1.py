
#!/usr/bin/env python3
import tkinter 
from tkinter import *
import sys
from scapy.all import *
from os import system

def help():
    print ("""
         ==================
        = Scanner via IP =
        ============================================================
        = Opções:                                                  =
        = [-t] Utilizar  o programa em modo texto                  =
        = EXEMPLO: python marcos.py -t <ip destino>                =
        =                                                          =
        = [-g] Utilizar o programa no modo interface gráfica       =
        = EXEMPLO: python marcos.py -g                             =
        =                                                          =
        = [--help ] ajuda do  programa                             =
        = EXEMPLO python marcos.py --help                          =
        =                                                          =
        = [--verion] exibe a versão do programa                    =
        = EXEMPLO: python marcos.py --version                      =
        ============================================================
    """)

if len(sys.argv) < 2:
    system('clear')
    print("error !")
    print("Anything arg is past !")
    help()
    sys.exit()

elif sys.argv[1].startswith('--'):
    op = sys.argv[1][2:]
    if op == 'help':
        help()
        sys.exit()
    if op == 'version':
        print("version 1.0")
        sys.exit()
    else:
        print("Option invalid !")
        sys.exit()

elif sys.argv[1] == "-t":
    alvo = sys.argv[2]
    res = sr1(IP(src="192.168.15.9",dst=alvo)/ICMP()/"Hello World")
    mac = res.hwsrc
    if res.tt1 <65:
        print("Linux - MAC: %s" %mac)
    else:
        print("Windows - MAC: %s" %mac)
elif sys.argv[1] == '-g':
    class Programa:
        def __init__(self, toplevel):
            self.frame1=Frame(toplevel.title("Scan"))
            self.frame1.pack()
            self.frame2=Frame(toplevel)
            self.frame2.pack()
            self.frame3=Frame(toplevel)
            self.frame3.pack()
            self.frame4=Frame(toplevel)
            self.frame4.pack()
            self.frame5=Frame(toplevel)
            self.frame5.pack()
            self.frame6=Frame(toplevel)
            self.frame6.pack()

else:
    print("Option invalid !")