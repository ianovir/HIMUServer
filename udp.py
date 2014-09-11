import socket
import HIMU

def goUDP(port):
	bufferSize=1024
	UDPSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	serverAddress = ('', port)
	print('Listening on port ', port)
	UDPSocket.bind(serverAddress)

	try:
		while HIMU.go:
			[data,attr] = UDPSocket.recvfrom(bufferSize)
			HIMU.plotSensorsData(data.decode("utf-8"))
	finally:
		UDPSocket.close()
