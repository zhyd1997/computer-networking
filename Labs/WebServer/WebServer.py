#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
# Fill in start
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
# Fill in end
while True:
  # Establish the connection
  print('Ready to serve...')
  connectionSocket, addr = serverSocket.accept() # Fill in
  try:
    message = connectionSocket.recv(2048).decode() # Fill in
    filename = message.split()[1]
    print('et')
    f = open(filename[1:])
    outputData = f.read() # Fill in
    # Send one HTTP header line into socket
    # Fill in start
    connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
    # Fill in end
    # Send the content of the requested file to the client
    for i in range(0, len(outputData)):
      connectionSocket.send(outputData[i].encode())
    connectionSocket.send('\r\n'.encode())

    connectionSocket.close()
  except IOError:
    # Send response message for file not found
    # Fill in start
    connectionSocket.send('404 Not Found')
    # Fill in end
    # Close client socket
    # Fill in start
    connectionSocket.close()
    # Fill in end
  serverSocket.close()
  sys.exit() #Terminate the program after sending the corresponding data
