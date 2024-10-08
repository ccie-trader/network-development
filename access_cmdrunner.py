#!/user/bin/python3
#GETPASS USING IMPORT COMMAND

import banner
import netmiko
import json
import netmiko.ssh_auth
import myaccess
import sys

if len(sys.argv) < 3:
    print("Usage: access_cmdrunner.py commands.txt devices.json")
    print(len(sys.argv), (sys.argv))
    exit()

##USING A JSON FILE FOR DEVICES

netmiko_exceptions = (netmiko.NetMikoTimeoutException,
                      netmiko.NetMikoAuthenticationException,
                      netmiko.NetmikoBaseException)

username, password = myaccess.get_credentials()

with open('tacacs_devices.json') as dev_file:
    devices = json.load(dev_file)


for device in devices:
    try:
        print('~'*79)
        print("Connecting to device", device['ip'])
        connection = netmiko.ConnectHandler(**device)
        print(connection.send_command('show ip int brief'))

        connection.disconnect()
    except netmiko_exceptions as e:
        print("Failed to ", device['ip'], e)

