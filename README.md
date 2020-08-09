HIMU-Server
===========

HIMU Server (HyperIMU Server) is a python library covering all server-side stream protocols supported by [HyperIMU](https://ianovir.com/works/mobile/hyperimu/). It performs basic operations such as input stream reading and csv sequence chunking.

Read the [HyperIMU Documentation](https://ianovir.com/works/mobile/hyperimu/hyperimu-help/) for more details.

# Overview #

## Network configurations ##

In order to connect the HIMUServer application and the HyperIMU app, you need the following:

* Be sure the Android device (HyperIMU client) and you server (HIMUServer) are connected to the **same network**
* Configure the HyperIMU app with the server **IP address** and **server port**
* Be sure the **firewall** in the server machine doesn't limit the server application 

## Protocols and Data Format ##

HyperIMU streams the sensors' data by using the protocols UDP and TCP,
or by storing them into a file for an offline processing.
The order of the sensors is the same as specified in the HyperIMU's settings.

Data are formatted as CSV (Comma Separated Value).
At a time, all sensors' values are gathered into a single string and all values are separated by commas. 
HyperIMU samples always three values per sensor.

E.g. considering a case with three sensors,
the packet will be:

	`0.123,0.586,0.2637,0.259,-0.5963,9.815,5.36,0.00,0.00 <CR><LF>`

where the values can be grouped as follows:
      
		  
| Sensor1                     | Sensor2                |Sensor3             | end of line|
|:---------------------------:|:----------------------:|:------------------:|:-----:|
| 0.123 **,**  0.586 **,**  0.2637      | 0.259 **,**  -0.5963 **,** 9.815 | 5.36  **,** 0.00  **,** 0.00 |   **[CR][LF]**   |  
	      
At the end of the CSV line it is inserted the symbols [CR][LF] or the char "#" (configurable option).

**Timestamp** and **MAC address** will be added at the very beginning of the packet, while **GPS** data (Latitude, Longitude, Altitude) and **GPS NMEA** sentences will be added at the very end.

# Installation
Get `HIMUServer` source from Github and install it.

## Linux
Execute the following commands:
```sh
git clone git://github.com/ianovir/HIMUServer.git
cd HIMUServer/
sudo python HIMUServer/setup.py install
sudo rm -rf HIMUServer
```   
## Windows
Download the repository or execute the following git command:
```sh
git clone git://github.com/ianovir/HIMUServer.git
```
Via Windows cmd (or Powershell) navigate to the downloaded folder `HIMUServer/` and execute the follwing command:
```sh
python HIMUServer/setup.py install
```   
Finally, delete the folder `HIMUServer/`

# How to use HIMUServer #

## Server configuration ##

HIMU-Server offers code snippets for data acquisition via UDP, TCP and FILE protocols.
It is possible to read the signals directly from the stream by using an instance of the class **HIMUServer**:

```python
from HIMUServer import HIMUServer
myHIMUServer = HIMUServer()
```
Configurations such as input buffer size, timeout and terminator symbol can be specified directly in the server constructor:

```python
from HIMUServer import HIMUServer
myHIMUServer = HIMUServer(bufferSize = 1024, timeout = 30, separatorIndex = 0)
```
The parameter `separatorIndex` can assume the value 0 to use the symbol **[CR][LF]** for csv packet separator, value 1 to use the **#** symbol.

## Custom listeners ##

HIMU Server supports listeners. A listener is an object having the public method `notify(sensorData)` which is called by the server when a packet is received.

You can define your custom listener:

```python
class SimplePrintListener:
    def __init__(self, serverInstance):
        self.__server = serverInstance
        ...
        
    def notify (self, sensorData):
        #simply printing all data strings
        HIMUServer.printSensorsData(sensorData)
```

Then add an instance of the listener to the server:

```python
myListener = SimplePrintListener(myHIMUServer)
myHIMUServer.addListener(myListener)
```

## Accessing Sensors' data ##

You can access the sensors' data by iterating the `sensorData` parameter in the `notify()` method of your custom listener:

```python
class MyCustomListener:
    def __init__(self):
        pass
    ...    
    def notify (self, sensorData): 
        for sensors in sensorData:
          sensor_1 = HIMUServer.strings2Floats(sensors[0])
          sensor_2 = HIMUServer.strings2Floats(sensors[1])
          ...
          s1_x = sensor_1[0]
          s1_y = sensor_1[1]
          s1_z = sensor_1[2]
```
Please, note the method `HIMUServer.strings2Floats()` which can be used to convert a list of strings (from csv) to a list of floats very easily.

## Launching the server ##

Launch the server with TCP protocol:
```python
	myHIMUServer.start("TCP", 2055)
```

UDP protocol:
```python
	myHIMUServer.start("UDP", 2055)
```

File:
```python
	myHIMUServer.start("FILE", "HIMU-file-path.csv")
```

Take a look to the `demo.py` file for more info.


# Copyright
Copyright(c) 2019 Sebastiano Campisi - [ianovir.com](https://ianovir.com). 
Read the LICENSE file for more details.


