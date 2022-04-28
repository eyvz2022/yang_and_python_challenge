from config import Config

#Interface List: Input is taken from here
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

cfg = Config()
output = ''
for interface in interfaces:
    output += cfg.create_interface_config(interface_info_dict=interface)
print(output)
