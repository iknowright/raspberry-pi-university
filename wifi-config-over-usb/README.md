# Update WiFi config over USB (wpa_supplicant)
Overwrite `wpa_supplicant.conf` on host system, when specific wifi configuration file is mount to the host via USB device.

## Features
* Add new wifi password on boot

## Getting Started

### Prerequisites
* Raspberry Pi 4 (or linux)
* Python 3.7.3
* apt-get

### Setup environment

1. install dependencies
```
apt-get install usbmount
```

2. For rpi4, the automount is disabled by default
Edit file in `/lib/systemd/system/systemd-udevd.service` and change
```
PrivateMounts=yes
```
to 
```
PrivateMounts=no
```

### Setup for USB
For usb device, put your wifi ssid and password inside a file called `wifi.config`.

File format: a pair of `<ssid>,<password>`
Example:
```
ssid1,password1
ssid2,password2
```

### Setup for host device
Edit or create `/etc/rc.local` if not exist
Add `python3 <path>/<to>/<file>.py` before `exit 0`

### Future works
* Auto find `wifi.config` in usb devices
* Auto restart wireless service to apply newest config

### Contributors
* Chai-Shi, Chang
* Darkborderman
