# Filename:                     cisco-automation-tutorial.py
# Command to run the program:   python cisco-automation-tutorial.py

# Import the required dependencies
from ncclient import manager
import sys
from argparse import ArgumentParser
import xml.dom.minidom


# Establish our NETCONF Session
m = manager.connect(host= input("Enter Hostname/IP: "), port=830, username = input("Enter Username: "), password = input("Enter Password: "), device_params={'name': 'csr'})

# Collect requested data from device
interface_filter = '''
                        <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                                <interface>
                                    <GigabitEthernet>
                                        <name/>
                                        <description/>
                                        <mtu/>
                                        <encapsulation>
                                        <dot1Q>
                                            <vlan-id/>
                                        </dot1Q>
                                        </encapsulation>
                                        <service-policy xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-policy">
                                            <input/>
                                            <output/>
                                        </service-policy>
                                    </GigabitEthernet>
                                </interface>
                            </native>
                        </filter>
                '''



# Execute the get-config RPC
result = m.get_config('running', interface_filter)
xmlDom = xml.dom.minidom.parseString( str( m.get_config('running', interface_filter)))
print(xmlDom.toprettyxml( indent = "  " ))
