# This library is a fork of the original dhcp_server library by @miketeo
# GitHub: https://github.com/niccokunzmann/python_dhcp_server/

from .dhcp import DHCPServer, DHCPServerConfiguration

configuration = DHCPServerConfiguration()
configuration.debug = print
configuration.adjust_if_this_computer_is_a_router()
configuration.router #+= ['192.168.0.1']
configuration.ip_address_lease_time = 60
server = DHCPServer(configuration)
for ip in server.configuration.all_ip_addresses():
    assert ip == server.configuration.network_filter()

server.run()
