# Check if 4G module is connected with USB
if ls /dev | grep cdc-wdm0 > /dev/null
then
    echo "4G module mounted"
else
    echo "4G module not mounted"
    exit 1
fi

# Establishing internet via 4G module
while :
do
    # Set 4G module mode to "online"
    qmicli -d /dev/cdc-wdm0 --dms-set-operating-mode="online"

    # It takes few seconds to 4G status to show "online", check status for 20 seconds
    count=0
    while [ $count -lt 10 ]
    do
        if qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode | grep "online" > /dev/null
        then
            echo "4G mode is set online"
            break
        fi
        sleep 2
        count=`expr $count + 1`
    done

    # Command that shows 4G status
    qmicli -d /dev/cdc-wdm0 --nas-get-signal-strength
    qmicli -d /dev/cdc-wdm0 --nas-get-home-network
    qmicli -d /dev/cdc-wdm0 -w

    # Setup for internet access
    ip link set wwan0 down
    echo "Y" | tee /sys/class/net/wwan0/qmi/raw_ip
    ip link set wwan0 up

    # Setup connection configuration and internet APN
    qmicli -p -d /dev/cdc-wdm0 --device-open-net="net-raw-ip|net-no-qos-header" --wds-start-network="ip-type=4,apn=internet" --client-no-release-cid

    # Command that brings up the internet connection
    timeout 20 udhcpc -i wwan0
    ip a s wwan0
    ip r s

    # Check internet access by below command
    if nc -zw1 google.com 443; then
        echo "Connected to internet"
        break
    else
        echo "Internet not connected, Retrying"
    fi
done
