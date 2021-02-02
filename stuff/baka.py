import napalm
# from pprint import pprint
from napalm_ros import ros

#Node info
router_ip = 'your_ip_or_hostname'
router_port = 8728 # Use 8729 for api-ssl
router_user = 'your_username'
router_pass = 'your_password'


# Use the RouterOS (ros) network driver to connect to the device:
driver = napalm.get_network_driver('ros')
print('\nConnecting to', router_ip, "with port", router_port)

device = driver(hostname=router_ip, username=router_user,
                    password=router_pass, optional_args={'port': router_port, 'use_ssl': True})

device.open()
print('\nOpening..' + '\nStarting session..\n' + router_ip, 'is connected')

def DEV_get_facts():
	print("\nInfo about router", device.get_facts()['hostname'])
	for key, value in device.get_facts().items():
		print(f"{key}: {value}")

def DEV_get_interfaces():
	print("\nInfo about interfaces:")
	for key_interface, value_interface in device.get_interfaces().items():
		print(f"\nInterface {key_interface}")
		for info_interface, int_info in value_interface.items():
			print(f"   {info_interface}: {int_info}")

def DEV_get_interfaces_ip():
	print("\nInfo about IP interfaces:")
	for key_interface, value_interface in device.get_interfaces_ip().items():
		print(f"\nInterface {key_interface}")
		for ipv, ip_info in value_interface.items():
			for ip, subnet in ip_info.items():
				print(f" {ipv} - {ip}/{subnet['prefix_length']}")

def DEV_get_ntp_servers():
	print("")

def DEV_get_snmp_information():
	print("")

def DEV_get_users():
	print("")

def DEV_get_ipv6_neighbors_table():
	print("")

def DEV_is_alive():
	print("\nDevice Status:")
	for key, value in device.is_alive().items():
		print("Status connection with", router_ip + " is", value)
		print("True: connected\nFalse: disconnected")

def DEV_ping():
	print("\nYou can input Hostname or IP address \nExample: 'google.com' or '10.x.x.x' (without quote)")
	dst = input("\nEnter your destination IP: ")
	# pprint(device.ping(dst))
	print(f"\nPinging [{dst}] with 56 bytes of data:")
	for success, success_info in device.ping(dst).items():
		for key in success_info['results']:
			print(f"Send to {key['ip_address']} rtt={key['rtt']}ms")
			rec_probes = int(success_info['probes_sent'])
			rec_loss = int(success_info['packet_loss'] / 20)
			recv = abs(rec_loss - rec_probes)
		print(f"\nInfo packets send:\n   Sent: {success_info['probes_sent']}, Received: {recv}, Lost: {success_info['packet_loss']}%")
		print(f"RTT (round-trip delay) info:\n   Max: {success_info['rtt_max']}ms, Min: {success_info['rtt_min']}ms, Avg: {success_info['rtt_avg']}ms, StdDev: {success_info['rtt_stddev']}ms")

def DEV_get_lldp_neighbors():
	print("")

def DEV_get_lldp_neighbors_detail():
	print("")

def DEV_get_network_instances():
	print("")

def DEV_get_mac_address_table():
	print("")

def DEV_get_bgp_neighbors():
	print("")

def DEV_get_bgp_neighbors_detail():
	print("")

def DEV_get_interfaces_counters():
	print("")

def DEV_get_environment():
	print("")