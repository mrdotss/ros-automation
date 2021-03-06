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
	print("\nList server of NTP client:")
	ct = 1
	for key, value in device.get_ntp_servers().items():
		print(f"{ct}. {key}")
		ct += 1

def DEV_get_snmp_information():
	print("\nSNMP info:")
	for key, value in device.get_snmp_information().items():
		if key == "community":
			for key_com, value_com in key['community'].items():
				print(f"{key_com}: {value_com}")
		print(f"{key}: {value}")

def DEV_get_users():
	print("\nUsers info:")
	for key, value in device.get_users().items():
		print(f"\nUsername = {key}")
		for user, info in value.items():
			print(f"  {user}: {info}")

def DEV_get_ipv6_neighbors_table():
	print("\nIPv6 neighbors info:")
	pprint(device.get_ipv6_neighbors_table())
	for info in device.get_ipv6_neighbors_table():
		for key, value in info.items():
			print(f"   {key}: {value}")
			if key['interface']:
				print(key['interface'])
				continue

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

def DEV_get_lldp_neighbors_detail():
for key, value in device.get_lldp_neighbors_detail().items():
	for info in value:
		print()
		for key_info, value_info in info.items():
			if key_info == "remote_chassis_id":
				key_info = "Chassis ID"
			elif key_info == "remote_port":
				key_info = "Port"
			elif key_info == "remote_port_description":
				key_info = "Port description"
			elif key_info == "remote_system_capab":
				key_info = "System capability"
			elif key_info == "remote_system_description":
				key_info = "System description"
			elif key_info == "remote_system_enable_capab":
				key_info = "System enable capability"
			elif key_info == "remote_system_name":
				key_info = "System name"
			if key_info == "parent_interface":
				key_info = "Parent Interface"
				print(f"{key_info}: {value_info}")
				print("[Remote]")
				continue
			print(f"  {key_info}: {value_info}")

def DEV_get_bgp_neighbors():
	print("\nBGP neighbors info:")
	for key, value in device.get_bgp_neighbors().items():
		print(f"{key}")
		for bgp_info, bgp_value in value.items():
			print(f"  {bgp_info}: {bgp_value}")

def DEV_get_arp_table():
	print("\nARP table:")
	for info in device.get_arp_table():
		print()
		for key, value in info.items():
			if key == "interface":
				key = "Interface"
				print(f"{key}: {value}")
				continue
			print(f"  {key}: {value}")

def DEV_get_interfaces_counters():

	def all_iface_counters():
		all_ct = 1
		all_iface_list = {}
		print("\nInterface status:")
		for iface_key_temp, value in device.get_interfaces_counters().items():
			print(f"[{all_ct}] Interface: {iface_key_temp}")
			all_iface_list[all_ct] = iface_key_temp
			all_ct += 1
			for ct_key, ct_value in value.items():
				print(f"  {ct_key}: {ct_value}")
			print()

	#Database and Count ID for interface list	
	ct = 1
	iface_list = {}
	for iface_ct, value in device.get_interfaces_counters().items():
		iface_list[ct] = iface_ct
		ct += 1

	#Loop for asking interface counters
	# while True:

	#Print interface list
	ctr = 1
	print("\nInterface list:")
	for key_ex, value_temp in iface_list.items():
		print(f"{key_ex}. {value_temp}")
		ctr += 1
	print(f"{ctr}. All interface")
	# print(f"{ctr+1}. Back to home")

	ask = int(input("\nSelect interface: "))
	Pout = False

	#ID from api
	for iface_key, iface_value in device.get_interfaces_counters().items():
		#ID from iface_list data
		for key_temp, value_temp in iface_list.items():
			#Finding interface as selected KEY
			if ask == ct and not Pout:
				all_iface_counters()
				Pout = True
				break		
			elif value_temp == iface_key and iface_list[ask] == iface_key and ask == key_temp:
				print(f"\nInterface: {iface_key}")
				for ct_key, ct_value in iface_value.items():
					print(f"  {ct_key} {ct_value}")
			elif ask+1 == ct + 1:
				break