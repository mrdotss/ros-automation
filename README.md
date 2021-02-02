[![Supported python versions](https://img.shields.io/pypi/pyversions/napalm-ros.svg)](https://pypi.python.org/pypi/napalm-ros/)
# ros-automation
Automation for RouterOS based by napalm-ros

You need to replace Node info with your own in `stuff/baka` module

### Getting started
firs you need to install napalm-ros packages

python 3.x</br>
`$ pip3 install napalm`<br>
`$ pip3 install napalm-ros`

Enable api in mikrotik<br>
![MikroTik API](https://i.imgur.com/77luieJ.png)<br>
`IP - Services` mark sure to enable `api` section.

### How to use
run the python file and you'll see list of method.<br>
`$ python3 base.py`

### Implemented getters works in this project
* get_facts
* get_interfaces
* get_interfaces_ip
* is_alive
* ping

update soon for more feature.<br>
also you can read more about napalm-ros packages [napalm-ros](https://github.com/napalm-automation-community/napalm-ros)
