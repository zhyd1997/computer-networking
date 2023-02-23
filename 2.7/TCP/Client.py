#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('', serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedMessage = clientSocket.recv(2048)
print('From Server: ', modifiedMessage.decode())
clientSocket.close()
