#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
import sys

if len(sys.argv) <= 1:
  print('Usage: "python3 ProxyServer.py server_ip"\n[server_ip]: It is the IP Address of Proxy Server')
  sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSocket = socket(AF_INET, SOCK_STREAM)
# Fill in start
tcpSocket.bind(('localhost', 8888))
tcpSocket.listen(1)
# Fill in end
while 1:
  # Start receiving data from the client
  print('Ready to serve...')
  tcpCliSock, addr = tcpSocket.accept()
  print('Received a connection from:', addr)
  message = tcpSocket.recv(1024).decode() # Fill in
  print(message)
  # Extract the filename from the given message
  print(message.split()[1])
  filename = message.split()[1].partition('/')[2]
  print(filename)
  fileExist = 'false'
  fileToUse = '/' + filename
  print(fileToUse)
  try:
    # Check whether the file exist in the cache
    f = open(fileToUse[1:], 'r')
    outputData = f.readlines()
    fileExist = 'true'
    # ProxyServer finds a cache hit and generates a response message
    tcpCliSock.send('HTTP/1.0 200 OK\r\n')
    tcpCliSock.send('Content-Type:text/html\r\n')
    # Fill in start
    tcpCliSock.send(outputData)
    # Fill in end
    print('Read from cache')
  # Error handling for file not found in cache
  except IOError:
    if fileExist == 'false':
      # Create a socket on the proxyserver
      c = socket(AF_INET, SOCK_STREAM) # Fill in
      hostName = filename.replace('www.', '', 1)
      print(hostName)
      try:
        # Connect to the socket to port 80
        # Fill in start
        c.connect((hostName, 80))
        # Fill in end
        # Create a temporary file on this socket and ask port 80 for the file requested by the client
        fileObj = c.makefile('r', 0)
        fileObj.write('GET  ' + 'http://' + filename + 'HTTP/1.0\r\n')
        # Read the response into buffer
        # Fill in start
        fileObj.readlines()
        # Fill in end
        # Create a new file in the cache for the requested file.
        # Also send the response in the buffer to client socket and the corresponding file in the cache
        tmpFile = open('./' + filename, 'wb')
        # Fill in start
        c.send(fileObj)
        c.close()
        # Fill in end
      except:
        print('Illegal request')
    else:
      # HTTP response message for file not found
      # Fill in start
      tcpCliSock.send('404 Not found')
      # Fill in end
  # Close the client and the server sockets
  tcpCliSock.close()
# Fill in start
tcpSocket.close()
sys.exit()
# Fill in end
