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


subnet_id = raw_input("Please enter the id of the subnet you want to delete:")
id = neutron.delete_subnet(subnet_id)
