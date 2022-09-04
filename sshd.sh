#!/usr/bin/bash
if [ "$EUID" -ne 0 ]; then
    echo "Script not running as root."
    exit 1
fi

echo "Enter Port Number"
read port


if ! [[ "$port" =~ ^[0-9]+$ ]];
    echo "Port Number is not an integer number"
else
    if (( ("$port" > 1024) && ("$port" < 65535) )); then
        echo "Port $port" >> /etc/ssh/sshd_config
        echo "Port new value is: $port"
    else
        echo "Incorrect Port value"
fi

sed -i "s/#PermitRootLogin/PermitRootLogin/"/etc/ssh/sshd_config
sed -i "s/PermitRootLogin yes/PermitRootLogin no/"/etc/ssh/sshd_config
systemctl restart sshd


     




