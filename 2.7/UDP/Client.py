#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
serverName = '0.0.0.0' # hostname after run 'Server.py'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
