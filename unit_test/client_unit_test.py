#main.py
# -*- coding: utf-8 -*-

import sys, os
import logging
sys.path.append("../core")
from packet import *
from encrypt import *
#from reactor import *
import  socket
from clienthandler import *
from tcpclient import *
from core.reactor import *
import server_unit_test

class ObjA:
    def __init__(self):
        self.tt = 0

    def __del__(self):
        pass


def unitTest():
    parser = CPacketParser()
    server = server_unit_test.GameServer()
    reactor = CReactor.Instance()
    reactor.SetPacketParser(parser)

    client = CTcpClient(reactor, server)

    if (platform.system() == "Windows"):
        client.InitConnect("127.0.0.1", 4800)
    else:
        client.InitConnect("192.168.96.152", 4800)

    #linux test
    #client.InitConnect("192.168.96.152", 4800)



    reactor.RunEventLoop()
    str = raw_input("please input:")
    print ("content: ", str)


def main():
    args = sys.argv
    unitTest()


if __name__ == '__main__':
    print 'sys.argv= ' + __name__
    print   sys.argv
    logging.warning('call main  FFF')
    main()


