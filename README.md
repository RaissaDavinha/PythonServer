# AgroCam Server #

### What is this repository for? ###
Agrocam Server to connect with AndroidCam

### How do I get set up? ###
Set in pythonServer.service the variable ExecStart to servidorPython.py location

In servidorPython.py, you need to set a log location in line 15, and the default.json, status.json and kml file location 

Copy the service file to /etc/systemd/system and give it permissions:

* sudo cp myservice.service /etc/systemd/system/myservice.service

* sudo chmod 644 /etc/systemd/system/myservice.service
	
Use the enable command to ensure that the service starts whenever the system boots:

* sudo systemctl enable myservice
	
Reboot your system and check the status of the service:

* sudo systemctl status myservice

### Developers ###
Raissa Furlan Davinha (raissa.furlan@sensorvision.com.br)