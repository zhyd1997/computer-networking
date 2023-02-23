#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Packet Loss
# import timeit
import datetime
from socket import *
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = 'Success'
sequenceNumber = 1

while sequenceNumber <= 10:
  socket.settimeout(clientSocket, 1)
  # startTime = timeit.default_timer()
  startTime = datetime.timedelta()
  print('Ping ' + str(sequenceNumber) + ' ' + str(startTime))
  try:
    clientSocket.sendto(message.encode(), ('', 12000))
    serverMessage, addr = clientSocket.recvfrom(1024)
    if serverMessage:
      # endTime = timeit.default_timer()
      endTime = datetime.timedelta()
      RTT = endTime - startTime
      print(serverMessage.decode() + ' ' + str(RTT.microseconds) + 'ms')
  except timeout:
    print('Request timed out')
  sequenceNumber += 1

clientSocket.close()
