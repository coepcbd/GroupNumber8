from neutronclient.v2_0 import client
from credentials import get_credentials
from utils import print_values
import os
import getpass

#n_Name = raw_input("please enter Network name:")

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
#credentials = get_credentials()
#neutron = client.Client(**credentials)
sub_id = raw_input("Please enter subnet id:")
#x='7ec920d9-0ff7-4938-991d-dd0b0b5af416'
z = neutron.show_subnet(sub_id)

print z

