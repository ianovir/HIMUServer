Hyper IMU & HIMU-Server Help
version 2.0

# Network and Connection configurations #

In this paragraph it is described one of the several solutions to set up a Network between your Android device and the Server (PC).

## Set up a portable Hotspot from your Android Device ##

1. Go in **Settings** from your Android Device
2. Under the section **Wireless & Networks**, tap on **More**, then on **Thetering & portable hotspot**.
3. In the **Thetering & portable hotspot** screen, tap on **Set up Wi-Fi hotspot**, then a box will appear.
4. Choose the **Network SSID** (Service Set Identifier) as you prefer; it is pratically the name of the the new Network
5. Specify a Security protocol as you want.
6. Choose a network **Password** as you prefer.

## Connect your Computer to the portable Network ##
Go in the Settings of your Computer and connect to the Network created above, specifying the Network SSID, 
the Security protocol and the Password defined in the previous steps.

## Retrieving the  IP address of your Computer ##
The IP address of your Computer is necessary in order to allow the Android device to connect to your PC.
It is composed up to 12 ciphers (example: *192.168.xxx.xxx*).
You can retrieve it after your Computer is connected to the Network.

### Windows OS ###
In the command prompt, enter the command **ipconfig /all** and check for the IPv4 Address.
### Linux OS ###
In the terminal enter the command **ip addr show** and check for the IPv4 Address.
### MAC OS ###
After your Computer connected to the Network, in the terminal enter the command **ifconfig** and check for the IPv4 Address.

## HyperIMU configuration ##
1. Go to the settings screen in HyperIMU
2. From the **Stream Protocol** select an Internet protocol (UDP or TCP)
3. In the field **IP address** put the IP address of your PC
4. in the field **Port Number** put a value of your choice.

Be sure that the corresponding port is not being used by the Operating System.

# Protocols and Data Format #

HyperIMU sends the data of the signals of the sensors by using the standard internet protocols UDP and TCP,
or it stores all data inside a text File for an offline processing.
The order of the sensors is the same as specified in the Settings of HyperIMU.
The text file is saved in the device memory, and its name is composed by a  prefix **HIMU-** followed by the time stamp.
The first lines of the text file represent the header, which cointains some informations 
about acquisition (sampling time, sensors, timestamp...).

Data sent through the Stream are formatted as CSV (Comma Separated Value).
At a time, all sensors' values are gathered into a single string and all values are separated by commas. 
HyperIMU samples three values per sensor, so for example, considering the case of three sensors,
the string passed through the stream will be:

	`0.123,0.586,0.2637,0.259,-0.5963,9.815,5.36,0.00,0.00 <CR><LF>`

where the values can be grouped as follows:
      
		  
| Sensor1                     | Sensor2                |Sensor3             | end of line|
|:---------------------------:|:----------------------:|:------------------:|:-----:|
| 0.123 **,**  0.586 **,**  0.2637      | 0.259 **,**  -0.5963 **,** 9.815 | 5.36  **,** 0.00  **,** 0.00 |   **[CR][LF]**   |  
	      
At the end of the CSV line it is inserted the symbols [CR][LF]  or the char "#" (configurable option).

**Timestamp** and **MAC address** will be added at the very beginning of the packet, while **GPS** data (Latitude, Longitude, Altitude) and **GPS NMEA** sentences will be added at the end.

# HIMUServer: usage #

HIMU-Server offers code snippets for data acquisition via UDP, TCP and FILE protocols.
It is possible to read the signals directly from the stream by using an instance of the class **HIMUServer.py**:

```python
	myHIMUServer = HIMUServer()
```
Configurations such as input buffer size, timeout and terminator symbol can be specified directly in the server constructor.

The last version of HIMU Server supports custom listeners, then you can define your custom one:

```python
	class SimplePrintListener:
		def __init__(self, serverInstance):
			self.__server = serverInstance
			pass
			
		def notify (self, sensorData):
			#simply printing all data strings
			HIMUServer.printSensorsData(sensorData)
			pass
```

Then, add an instance of the listener to the HIMUServer object:

```python
	myListener = SimplePrintListener(myHIMUServer)
	myHIMUServer.addListener(myListener)
```

For launching TCP protocol, use
```python
	myHIMUServer.start("TCP", 2055)
```

For launching UDP protocol, use
```python
	myHIMUServer.start("UDP", 2055)
```

For File importing, use 
```python
	myHIMUServer.start("FILE", "HIMU-file-path.csv")
```


# About #

HIMUServer is released under the MIT license.

HyperIMU and HIMUServer by Sebastiano Campisi - ianovir - Copyright &copy; 2017


