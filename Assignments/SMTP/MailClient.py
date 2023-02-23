#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *

msg = '\r\n I love computer networks!'
endMsg = '\r\n.\r\n'

# Choose a mail server (e.g. Google mail server) and call it mailserver

gmailServerName = 'smtp.gmail.com'
gmailServerPort = 257
mailServer = (gmailServerName, gmailServerPort) # Fill in

# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailServer)
# Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
  print('220 reply not received from the server.')

# Send HELO command and print server response.
helloCmd = 'HELO Alice\r\n'
clientSocket.send(helloCmd.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
  print('250 reply not received from server.')

# Send MAIL FROM command and print server response
# Fill in start
mailFromCmd = 'MAIL FROM: test\r\n'
clientSocket.send(mailFromCmd.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
  print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response
# Fill in start
recpToCmd = 'RCPT TO: zhyd007@gmail.com\r\n'
clientSocket.send(recpToCmd.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
  print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response
# Fill in start
dataCmd = 'DATA\r\n'
clientSocket.send(msg.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
  print('354 reply not received from server.')
# Fill in end

# Send message data
# Fill in start
clientSocket.send(msg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
  print('250 reply not received from server.')
# Fill in end

# Message ends with a single period
# Fill in start
clientSocket.send(endMsg.encode())
# Fill in end

# Send QUIT command and get server response
# Fill in start
quitCmd = 'QUIT\r\n'
clientSocket.send(quitCmd.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '221':
  print('221 reply not received from server.')

clientSocket.close()
# Fill in end
