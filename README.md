# yang_and_python_challenge

TASK1:
The Yang Model is created with respect to given interfaces.

TASK2:
There can be 2 different solutions for the problem.
    
    SOLUTION1:
        The input data inside "input.py" is feeding the "config.py" script which takes the data and sends it to the jinja file inside the folder "interface.j2". Jinja helps to format the input data in such a way that can be set up flexibly.
    SOLUTION2:
        In this solution, NETCONF is used to connect to a live device (Cisco Yang Suite sandbox IOSXE device) and collected requested interface data. The XML code is derived via the Cisco Yang Suite Desktop program.
