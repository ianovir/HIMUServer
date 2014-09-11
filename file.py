import HIMU

def goFile(fileName):
	f = open(fileName,'r')
	sline=f.readline()
	while sline!='':
		if sline[0]!='@':
			HIMU.plotSensorsData(sline)
		sline=f.readline()
	
	print('reached EOF')
	
	