# Raspberry Pi University
![](https://i.imgur.com/eazcSD3.png)


Raspberry Pi usage at full extend.

> Contents below are the work I have been on Raspberry Pi over these 3 years. I can't quantify the afford I put on this tiny little chip, but it'd been very fun for me. Hope you guys like it. Enjoy!

## Table of Contents

- Prerequisites
- General settings
- Camera
- WiFi Dongle
- Remote Access (incl. advanced)
- 4G Internet Connection
- Mesh Network
- Continuous Integration
- RPi Management
- Real Life Example

## Prerequisites

This workthrough is targetted for users using Raspberry Pi 3 or 4 with minumin OS installed (Command Line Interface Mode).

## General Settings

### WiFi Setting
There are two ways you can connect your pi with wifi.

First, via `sudo raspi-config` 
- `sudo raspi-config -> Network Options -> wifi -> {Enter your ssid} -> {enter your passphrase}`

Second, via `/etc/wpa_supplicant/wpa_supplicant.conf` file
1. with your favorite editor go into file with `sudo vim /etc/wpa_supplicant/wpa_supplicant.conf`
2. append your WiFi info below as:
    ```
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=TW


    network={
        ssid="{your wifi ssid}"
        psk="{your wifi passphrase}"
    }
    ```
4. save the file
3. if you are going with this method, make sure you follow this command: `sudo wpa_cli reassociate` to make the new configured wifi works. Otherwise, reboot RPi with `sudo reboot`. Your wifi will be now set. 

### Interface Setting
- To use camera: `sudo raspi-config -> Interface Options -> Camera -> Enable -> OK`
- To use SSH: `sudo raspi-config -> Interface Options -> SSH -> Enable -> OK`

### Camera 
Befote started this make sure you have the settings right, follow the Interface Option for Camera in General Settings to enable camera interface. Which is `sudo raspi-config -> Interface Options -> Camera -> Enable -> OK`.

## Remotely connect to RPi
### Simple SSH

To make RPi accept ssh connections, make sure you enable the settings for ssh in `sudo raspi-config`, as mentioned in General Settings.

#### Over LAN
Fire up `ifconfig`

#### Over WLAN

### Reverse SSH-Tunnel
AutoSSH + systemd to consistantly etablish revse ssh tunnel to server.

**overview:**

![](https://i.imgur.com/Z5WKqBK.png)

**requirements:**
- autossh
- ssh keygen (for password-less ssh)

**setup:**
- remote server
    - username
    - host ip
    - ssh keypem
    - port to reverse

```
[Unit]
Description=AutoSSH tunnel service Remote port {reverse-port} to local 22
After=network.target

[Service]
Environment="AUTOSSH_GATETIME=0"
ExecStart=/usr/bin/autossh -o StrictHostKeyChecking=no -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -i /home/pi/{remote-server}.pem -N -R {reverse-port}:localhost:22 {remote-server-username}@{remote-server-host/ip}

[Install]
WantedBy=multi-user.target

```





### Shellhub
![](https://i.imgur.com/h39sKrD.png)

> ShellHub is a modern SSH server for remotely accessing Linux devices via command line (using any SSH client) or web-based user interface. It is intended to be used instead of sshd.

Server: A server with Static Public IP

Client: Your RPi with internet access


## 4G Internet Connection

> I was luckily enough to ever worked on the 4G connection on RPi. The internet connection for 4G is supported by Waveshare SIM7600-T 4G HAT .

Official Wiki: [SIM7600X 4G & LTE Cat-1 HAT](https://www.waveshare.net/wiki/SIM7600CE_4G_HAT)

The workable way to use this module is by using the Qualcomm QMI-CLI tool to make the 4G connect to the internet. I tested the PPP method but failed multiple times until I found qmicli utils.

Here is how you setup for 4G connection:
1. Plug the 4G HAT in and wire the module as below
2. Install packages
3. Disable WiFi at boot option
4. Search your ISP / Carrier APN
5. Setup and run connection script 

Resources: [here](https://hackmd.io/ILuPyBsHRhmu3DQ2X6yKyw)

## Mesh Network
![](https://i.imgur.com/6wajasT.png)

