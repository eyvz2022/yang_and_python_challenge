#Import Config class from config.py
from config import Config

#Interface List: Input is taken here
interfaces = [{
    "intf-type": "GigabitEthernet",
    "intf-id": "0/0",
    "subint": 900,
    "encap": 900,
    "description": "interface 1",
    "mtu": 9216,
    "service-policy": [
        {"direction": "input", "name": "POLICY1"},
        {"direction": "input", "name": "POLICY2"},
        {"direction": "output", "name": "POLICY3"}
    ]
},
    {
        "intf-type": "GigabitEthernet",
        "intf-id": "0/0",
        "subint": 901,
        "encap": "default",
        "description": "interface 2",
        "mtu": 1500,
        "service-policy": [
            {"direction": "output", "name": "POLICY4"}
        ]
    }
]

#Call config.py script
cfg = Config()
output = ''

#This for loop sends all interface data to jinja over config.py and have the proper results
for interface in interfaces:
    output += cfg.create_interface_config(interface_info_dict=interface)
print(output)
