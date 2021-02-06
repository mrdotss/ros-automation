[![Supported python versions](https://img.shields.io/pypi/pyversions/napalm-ros.svg)](https://pypi.python.org/pypi/napalm-ros/)
# ros-automation
Automation for RouterOS<br>
What is dis? this project help you to use napalm-ros package without too much coding, 
so you can just run the file and ready to command your MikroTik. Since this project used napalm-ros package, you can learn how to use the package.<br>

Note: You need to replace Node info with your own in `stuff/baka` module

### Getting started
first you need to install napalm-ros packages

python 3.x</br>
`$ pip3 install napalm`<br>
`$ pip3 install napalm-ros`

Enable api in your mikrotik<br>
![MikroTik API](https://i.imgur.com/77luieJ.png)<br>
`IP - Services` mark sure to enable `api` section, also you can use api-ssl for secure connection.

### How to use
run the python file and you'll see list of method.<br>
`$ python3 base.py`

### Implemented getters works in this project
* get_facts
* get_interfaces
* get_interfaces_ip
* is_alive
* ping
* get_ipv6_neighbors_table
* get_snmp_information
* get_ntp_servers

update soon for more feature.<br>
Read more about
[napalm-ros repository](https://github.com/napalm-automation-community/napalm-ros) and [napalm-ros site](https://napalm.readthedocs.io/en/yang_doc/support/index.html)
