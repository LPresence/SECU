#!/usr/local/bin/ipython3
from scapy.all import *
#####
#Vars
#####
sport = random.randint(1024,65535)
dport = 80
#####
# SYN
#####
ip=IP(src='192.168.10.9',dst='192.168.10.20')
SYN=TCP(sport=sport,dport=dport,flags='S',seq=100)
SYNACK=sr1(ip/SYN)
#########
# SYN-ACK
#########
ACK=TCP(sport=sport, dport=dport, flags='A', seq=SYNACK.ack + 1, ack=SYNACK.seq + 1)
send(ip/ACK)
