import HIMU

#Use the <go> variable to control the acquisition loop
HIMU.go=True

#Change the timeout (in seconds) :
HIMU.timeout = 2

#Launch acquisition via TCP on port 2250:
HIMU.execute("TCP", 2250)

#Launch acquisition via UDP on port 3478:
HIMU.execute("UDP", 3478)

#Launch acquisition from local file:
HIMU.execute("FILE", "HIMU-filetest.txt")