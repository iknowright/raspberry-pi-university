import os
from time import sleep

if __name__ == "__main__":
    for retry in range(int(os.environ.get("AUTO_UPDATE_RETRY", "5")))
        sleep(int(os.environ.get("AUTO_UPDATE_INTERVAL", "10")))
        try:
            print(f"Start updating wifi config, retry {retry}")
            # TODO: Auto find `wifi.config` in usb devices
            # Curruntly define the first usb storage device
            source = open("/media/usb0/wifi.config", "r+")
            target = open("/etc/wpa_supplicant/wpa_supplicant.conf", "a+")
            for wifi_pair in source.readlines():
                account, passowrd = wifi_pair.strip().split(",")
                target.write(
                    f'network={{'
                    f'    ssid="{account}"'
                    f'    psk="{password}"'
                    f'}}'
                )
            print("Done writing config to wpa_applicant.conf")
            # TODO: Auto restart wireless service to apply newest config
            exit(0)
        except Exception as error:
            print(erorr)
