# yang_and_python_challenge

**TASK1:**
The Yang Model is created with respect to given interfaces.

**TASK2:**
There can be 2 different solutions for the problem:
    
    SOLUTION1:
        Run "input.py" to see the output. The input data inside "input.py" is feeding the "config.py" script which takes the data and sends it to the jinja file (interface.j2) inside the "jinja" folder. Jinja helps to format the input data in such a way that can be set up reusable and modular way.
    SOLUTION2:
        In this solution, NETCONF is used to connect to a live device (Cisco Yang Suite sandbox IOSXE device is used as an example) and collected requested interface data. The XML code is derived via the Cisco Yang Suite Desktop program.
