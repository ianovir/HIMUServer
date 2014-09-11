#!/usr/bin/env python

#import socket


#TCP_IP = '127.0.0.1'
#TCP_PORT = 2500
#BUFFER_SIZE = 1024
 
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((TCP_IP, TCP_PORT))

#while True:
#   data = s.recv(BUFFER_SIZE)
#    print ("received data: ", data)

#s.close()


import socket
import sys
import  HIMU


def goTCP(port):
	bufferSize= 1024
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverAddress = ('', port)

	print ('starting up on ', serverAddress )
	sock.bind(serverAddress)
	sock.listen(1)
	print ('waiting for a connection')
	[connection, clientAddress] = sock.accept()

	try:
		print ('connection from', clientAddress)
		while HIMU.go:
		    data = connection.recv(bufferSize)	
		    HIMU.plotSensorsData(data.decode("utf-8"))
	finally:
		connection.close()