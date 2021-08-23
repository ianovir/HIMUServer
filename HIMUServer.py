#===============================================================================
#
# MIT License
#
# HyperIMU Server (HIMU Server)
# Copyright (c) [2020] [Sebastiano Campisi - ianovir]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#===============================================================================

import socket
import math
import traceback

valuesPerSensor = 3

class HIMUServer:

	def __init__(self, bufferSize = 2048, timeout = 10, separatorIndex = 0):
		self.__listeners = []
		self.__packSeparators = ["\r\n" , "#"]
		self.__commentSymbol = '@'
		self.timeout = timeout  #timeout in seconds
		self.bufferSize=bufferSize #bytes
		self.go = True		
		if(separatorIndex == 0  ):
			self.packSeparator = self.__packSeparators[0]
		else:
			self.packSeparator = self.__packSeparators[separatorIndex]
		
	def addListener(self , newListener):
		self.__listeners.append(newListener)

	def __notifyListeners(self, recPacket):
		for listener in self.__listeners:
			listener.notify(recPacket)

	def executeUDP(self , port, raw = False):
		'''
		Performs data acquisition via UDP protocol.
		If raw is False (default) sensors' data will be extracted from the input string,
		otherwise the latter will be presented as it is.
		'''
		UDPSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)	
		UDPSocket.settimeout(self.timeout)
		serverAddress = ('', port)
		print('Listening on port ' + str(port))
		UDPSocket.bind(serverAddress)
		while self.go:
			[data,attr] = UDPSocket.recvfrom(self.bufferSize)
			if not data: break
			if raw :
				self.__notifyListeners(data.decode("utf-8"))
			else:
				self.__notifyListeners(self.__extractSensorData(data.decode("utf-8")))
		UDPSocket.close()

	def executeTCP(self , port, raw = False):
		'''
		Performs data acquisition via TCP protocol.
		If raw is False (default) sensors' data will be extracted from the input string,
		otherwise the latter will be presented as it is.
		'''
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(self.timeout)
		serverAddress = ('', port)
		sock.bind(serverAddress)
		sock.listen(1)
		print ('waiting for connection...')
		[connection, clientAddress] = sock.accept()
		connection.setblocking(1)
		print ('connection from ' + str(clientAddress))
		while self.go:
			data = connection.recv(self.bufferSize)
			if not data: break
			if raw :
				self.__notifyListeners(data.decode("utf-8"))
			else:
				self.__notifyListeners(self.__extractSensorData(data.decode("utf-8")))
		connection.close()		

	def executeFile(self , fileName, raw = False):
		'''
		Performs data acquisition from local file
		'''
		print("Reading file " + fileName + " ...")
		f = open(fileName,'r')
		sline=f.readline()
		while sline!='':
			if sline[0]!= self.__commentSymbol:	
				if raw :
					self.__notifyListeners(sline)
				else:			
					self.__notifyListeners(self.__extractSensorData(sline))
			sline=f.readline()
		print('reached EOF.')
			
	
	@staticmethod
	def strings2Floats(listString):
		'''
		Converts a list of Strings to a list of floats; returns the converted list
		'''
		out=[]		
		for j in range(0, len(listString)):
			if(listString[j]!=''):
				out.append( float(listString[j]))
		return out
		
	@staticmethod
	def printSensorsData (sensorData):		
		'''
		Prints to console the acquired sensors'data
		'''
		try:	
			for acquisition in sensorData:
				i = 1;
				for sensorAcq in acquisition :
					print('Sensor' + str(i) +  ": " + str(sensorAcq))
					i+=1
		except Exception as ex:
			print(str(ex))
				
	def __extractSensorData (self, dataString):		
		'''
		Extracts sensors'data from the input raw data string.
		The return object is an array of arrays [i][j], where i corresponds to sampled acquisitions and j corresponds to sensors' value.
		All sensors' values are represented as strings.
		'''
		packages = dataString.split(self.packSeparator)
		retVal = []
		for pack in packages:
			if pack!='' :
				try:
					packVal = []
					packSplit = pack.replace('\n', '').replace('\r', '').split(",")
					numSensors = int(math.floor( len(packSplit)  / valuesPerSensor))
					for i in range(0 , numSensors):
						p = packSplit[i*valuesPerSensor : (i+1)*(valuesPerSensor)]
						packVal.append(p)
					if(len(packVal)>0):
						retVal.append(packVal)
				except Exception as ex:
					print(str(ex))
		return retVal

	def start(self , protocol, arg, raw = False):
		'''
		Executes the data acquisition;
		<protocol> 	the supported protocol: 'UDP' , 'TCP' , 'FILE'
		<arg> 		the port number in case of UDP or TCP protocols, input file path in case of 'FILE' protocol		
		<raw> 		False (default) to extract sensors' data from input string, True to present the latter as it is
		'''
		
		print('protocol: ' + protocol)
		print('RAW: ' + ('yes' if raw else 'no'))
		try:
			if protocol == 'RAW':
				print("RAW deprecated, use the <raw> parameter instead.")
			elif protocol == 'UDP':
				self.executeUDP(int(arg), raw)
			elif protocol == 'TCP':
				self.executeTCP(int(arg), raw)
			elif protocol == 'FILE':
				self.executeFile(arg, raw)
		except Exception as ex:
			print(str(ex))
			
	def stop(self ):
		self.go = False
		
