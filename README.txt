Hyper IMU & HIMU-Server Help
version 1.0

------------------------------------------------------------------------------------------------------------
Network & Connection configurations

In this paragraph it is described one of the several solutions to set up a Network between your Android device and the Server (PC).

Set up a portable Hotspot from your Android Device
	- Go in “Settings” from your Android Device
	- Under the section “Wireless & Networks”, tap on “More”, then on “Thetering & portable hotspot”.
	- In the “Thetering & portable hotspot” screen, tap on “Set up Wi-Fi hotspot”, then a box will appear.
	- Choose the “Network SSID” (Service Set Identifier) as you prefer; it is pratically the name of the the new Network
	- Specify a Security protocol as you want.
	- Choose a network “Password” as you prefer.

Connect your Computer to the portable Network
	Go in the Settings of your Computer and connect to the Network created above, specifying the Network SSID, 
	the Security protocol and the Password defined in the previous steps.

Retrieving the  IP address of your Computer
	The IP address of your Computer is necessary in order to allow the Android device to connect to your PC.
	It is composed up to 12 ciphers (example: 192.168.xxx.xxx).
	You can retrieve it after your Computer is connected to the Network.

Windows OS
- In the command prompt, enter the command “ ipconfig /all ” and check for the IPv4 Address.
Linux OS
- In the terminal enter the command “ ip addr show ” and check for the IPv4 Address.
MAC OS
- After your Computer connected to the Network, in the terminal enter the command “ ifconfig ” and check for the IPv4 Address.

Please note that IP address may change, so it is better to check its value at every connection.


Configure HyperIMU for the connection
	- Go to the settings screen in HyperIMU
	- From the “Stream Protocol” select an Internet protocol (UDP or TCP)
	- In the field “IP address” put the IP address of your PC
	- in the field “Port Number” put a value of your choice.

Be sure that the corresponding port is not being used by the Operative System.



------------------------------------------------------------------------------------------------------------
Protocols and Data Format

HyperIMU sends the data of the signals of the sensors by using the standard internet protocols UDP and TCP,
or it stores all data inside a text File for an offline processing.
The order of the sensors is the same as specified in the Settings of HyperIMU.
The text file is saved in the device memory, and its name is composed by a  prefix “HIMU-” followed by the time stamp.
The first lines of the text file represent the header, which cointains some informations 
about acquisition (sampling time, sensors, timestamp...).

Data sent through the Stream are formatted as CSV (Comma Separated Value).
At a time, all sensors’ values are gathered into a single string and all values are separated by commas. 
HyperIMU samples three values per sensor, so for example, considering the case of three sensors,
the string passed through the stream will be:

“0.123,0.586,0.2637,0.259,-0.5963,9.815,5.36,0.00,0.00,#”

where the values can be subdivided as follows:

    0.123   0.586   0.2637           0.259   -0.5963  9.815            5.36   0.00   0.00         #
	      Sensor1                               Sensor2                               Sensor3                end of line
	      
	      
At the end of the CSV line it is inserted the special symbol “#”.
In the case of GPS data, besides the values of latitude and longitude, a zero value is added in order to match the same length of values of other sensors.



------------------------------------------------------------------------------------------------------------
Receiving and plotting Data in Python 3.3.3

HIMU-Server offers code snippets regarding the stream reads for the internet protocols UDP, TCP and FILE protocol.
It is possible to read the signals direclty from the stream by calling the script “main.py”:

“ python main.py PROTOCOL PARAM ”

where PROTOCOL indicates the chosen stream protocol (TCP | UDP | FILE), and PARAM is the parameter depending on the used protocol.

TCP
	Enter the command: “ python main.py TCP PORT ”
	where the PORT parameter is the port where the server is going to listen.
		Example: “ python main.py TCP 2055”

UDP
	Enter the command: “ python main.py UDP PORT ”
	where the PORT parameter is the port where the server is going to listen.
		Example: “ python main.py UDP 2055”

FILE
	Enter the command: “ python main.py FILE FILENAME ”
	where the FILENAME.txt is the name of the file .txt to read
	“ python main.py FILE HIMU-test01.txt ”


Remember that the code provided with HIMU-Server consists only on code snippets, 
whose work is only to print on screen the values by subdividing them per sensor, 
so HIMU-Server is not optimized code. HIMU-Server offers a reusable source code
to be integrated into your developing process. 



_____________________
HyperIMU and HIMUServer by Sebastiano Campisi - ianovir - 2014


