# PiTimekeeperPlus
Raspberry Pi clock and prayer time reminder with SenseHat and logs registered device on the network.

## Getting Started
These instructions will get you a copy of the project up and running on your RaspberryPi for development. See deployment for notes on how to deploy the project on a live system.

### File structure
In this repository, you will find
```
.
|____main.py
|____pixeling.py
|____prayingTime.py
|____LICENSE
|____README.md
```
### Prerequisites
You should have these before getting started
* [RaspberryPi](https://www.raspberrypi.org/products/)
* [SenseHat](https://www.raspberrypi.org/products/sense-hat/)
* [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) (installed)

### Clone / Download
In Raspbian, you may download ZIP file and extract the files or open Terminal and run

```
cd /your-desired-path
git clone https://github.com/azfaralsukor/PiTimekeeperPlus.git
```

### Installing pip packages
Run
```
pip3 install python-nmap --user
```

### Registering MAC Address
To keep tab on which device is online on the network, register the MAC Addresses in [pixeling.py](pixeling.py) starting from line 52. There are two modes that can be alternate between 8 devices at a time.

### Run
```
cd PiTimekeeperPlus
python3 main.py
```

There you have it a clock and prayer time reminder on your Raspberry Pi.

## Deployment
In order to have a command or program run when the Pi boots, you can add it as a service. Once this is done, you can start/stop enable/disable from the linux prompt.

### Creating a service
On your Pi, create a .service file for your service file into `/etc/systemd/system`, for example:

```
[Unit]
Description=Main service
After=network.target

[Service]
ExecStart=sudo /usr/bin/python3 -u /home/pi/PiTimekeeperPlus/main.py
WorkingDirectory=/home/pi/PiTimekeeperPlus
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

Once this has been created, you can attempt to start the service using the following command:

`sudo systemctl start myscript.service`

Stop it using following command:

`sudo systemctl stop myscript.service`

When you are happy that this starts and stops your app, you can have it start automatically on reboot by using this command:

`sudo systemctl enable myscript.service`

The systemctl command can also be used to restart the service or disable it from boot up!
You can get more information from: `man systemctl`

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Thanks to [ThePi.io](https://thepi.io/how-to-create-a-raspberry-pi-digital-clock-using-the-sense-hat/) for the delicious retro Pi Clock code.
