from neutronclient.v2_0 import client
from credentials import get_credentials
from utils import print_values
import os

credentials = get_credentials()
neutron = client.Client(**credentials)
subnets = neutron.list_subnets()
print subnets
