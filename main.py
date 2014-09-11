import sys
import tcp
import udp
import HIMU
import file

HIMU.go=True

#synthax main(Protocol, port/file)
arg= sys.argv[1:]
protocol=arg[0]
print('protocol: ',protocol)


if protocol == 'UDP':
	udp.goUDP(int(arg[1]))
elif protocol == 'TCP':
	tcp.goTCP(int(arg[1]))
elif protocol == 'FILE':
	file.goFile(arg[1])
