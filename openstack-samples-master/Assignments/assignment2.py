from neutronclient.v2_0 import client
from credentials import get_credentials
from utils import print_values
import os
import getpass

n_Name = raw_input("please enter Network name:")

#credentials = get_credentials()

uname = raw_input("Please enter username:")
tname = raw_input("Please enter tenant name:")
passw = getpass.getpass()

d = {}
d['username'] = uname
d['password'] = passw
d['auth_url'] = os.environ['OS_AUTH_URL']
d['tenant_name'] = tname

credentials = d
neutron = client.Client(**credentials)

n_Net = {
    "network":
     {
        "name": n_Name,
        "admin_state_up": True
     }
}

netw = neutron.create_network(body=n_Net)
net_dic = netw['network']
net_id = net_dic['id']
print "Network create Id is " + net_id

i = input("Please enter how many subnets you want to add:")

for j in range(0, i):
    cidr = raw_input("Please enter Network address and CIDR:")
    ip_v = raw_input("Please Enter IP version:")

    body_create_subnet = {
        "subnets":  [
                {
                    "cidr": cidr,
                    "ip_version": ip_v,
                    "network_id": net_id
                }
                   ]
        }
    subnet = neutron.create_subnet(body=body_create_subnet)
    print "Created a subnet:%s" % subnet




