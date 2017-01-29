import socket
import math

timeout = 10  #timeout in seconds
bufferSize=1024 #bytes
packSeparator="#"
go=True;

def executeUDP(port):
	'''
	Performs data acquisition via UDP protocol
	'''
	UDPSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)	
	UDPSocket.settimeout(timeout)
	serverAddress = ('', port)
	print('Listening on port ' + str(port))
	UDPSocket.bind(serverAddress)
	while go:
		[data,attr] = UDPSocket.recvfrom(bufferSize)
		if not data: break
		printSensorsData(data.decode("utf-8"))
	UDPSocket.close()

def executeTCP(port):
	'''
	Performs data acquisition via TCP protocol
	'''
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(timeout)
	serverAddress = ('', port)
	sock.bind(serverAddress)
	sock.listen(1)
	print ('waiting for connection')
	[connection, clientAddress] = sock.accept()
	connection.setblocking(1)
	print ('connection from ' + str(clientAddress))
	while go:
		data = connection.recv(bufferSize)	
		if not data: break
		printSensorsData(data.decode("utf-8"))
	connection.close()		

def executeFile(fileName):
	'''
	Performs data acquisition from local file
	'''
	print("Reading file " + fileName + " ...")
	f = open(fileName,'r')
	sline=f.readline()
	while sline!='':
		if sline[0]!='@':
			printSensorsData(sline)
		sline=f.readline()	
	print('reached EOF.')
		
def strings2Floats(listString):
	'''
	Converts a list of Strings to a list of floats; returns the converted list
	'''
	out=[]
	for j in range(0, len(listString)-1):
		out.append( float(listString[j]))
	return out

def printSensorsData (dataString):	
	'''
	Prints to console the acquired data string, separing it by sensor
	'''
	packages = dataString.split(packSeparator)
	for pack in packages:
		try:
			pack = pack+","
			lFloat =strings2Floats(pack.split(","))
			numSensors = int(math.floor(len(lFloat)/3))
			for i in range(0,numSensors):
				p=lFloat[i*3:3*(i + 1)]
				print('Sensor' + str(i+1) +  ": " + str(p))
		except:
			pass

def execute(protocol, arg):
	'''
	Executes the data acquisition;
	<protocol> 	is the supported protocol: 'UDP' , 'TCP' or 'FILE'
	<arg> 		is the port number in case of UDP or TCP protocols, input file path in case of 'FILE' protocol
	'''
	print('protocol: ' + protocol)
	try:
		if protocol == 'UDP':
			executeUDP(int(arg))
		elif protocol == 'TCP':
			executeTCP(int(arg))
		elif protocol == 'FILE':
			executeFile(arg)
		print("The End")
	except Exception as ex:
		print(str(ex))
	