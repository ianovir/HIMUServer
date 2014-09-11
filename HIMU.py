from math import floor

go=True;

def Strings2Floats(listString):
	out=[]
	for j in range(0,len(listString)-1):
		out.append( float(listString[j]))
	return out

def plotSensorsData (inputString):
	lFloat =Strings2Floats(inputString.split(','))
	numSensors = floor(len(lFloat)/3)
	for i in range(0,numSensors):
		p=lFloat[i*3:3*(i + 1)]
		print('Sensor',(i+1), ": ",p,sep='')
	print('\n')


	