import json
import stuff.baka as b

command_list = {
   "1": "b.DEV_get_facts()",
   "2": "b.DEV_get_interfaces()",
   "3": "b.DEV_get_interfaces_ip()",
   "4": "b.DEV_get_ntp_servers()",
   "5": "b.DEV_get_snmp_information()",
   "6": "b.DEV_get_users()",
   "7": "b.DEV_get_ipv6_neighbors_table()",
   "8": "b.DEV_is_alive()",
   "9": "b.DEV_ping()",
   "10": "b.device.get_lldp_neighbors()",
   "11": "b.DEV_get_lldp_neighbors_detail()",
   "12": "b.device.get_network_instances()",
   "13": "b.device.get_mac_address_table()",
   "14": "b.DEV_get_bgp_neighbors()",
   "15": "b.device.get_bgp_neighbors_detail()",
   "16": "b.DEV_get_arp_table()",
   "17": "b.DEV_get_interfaces_counters()",
   "18": "b.device.get_environment()"
}

while True:
  isc = input("\n[1] Run command\n[2] I'm done.\n\nChoose your act: ")
  if isc == "1":
    with open('stuff/data.json') as mere:
      data = json.load(mere)
    print("\nList of Method")
    for key, value in data.items():
      print (key + " " + " " + value)
    mereID = int(input("\nSelect your command : "))
    printed = False
    for key, value in command_list.items():
      key = int(key)
      if mereID is key:
        to_call = value
        print(eval(to_call))
      elif mereID > 43 and not printed:
        print("There's no command with ID", mereID)
        printed = True
  elif isc == "2":
    b.device.close()
    print("\nDevice disconnected")
    break
  else:
    b.device.close()
    break