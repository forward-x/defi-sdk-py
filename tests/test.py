import sys
import os
import json
project_dir = os.path.abspath("")
sys.path.append(project_dir)
from defi_sdk_py import ChainClient, FWX_ADDRESS


FWXChain = ChainClient(
    rpc_url="http://65.109.93.162:9650/ext/bc/C/rpc",
    private_key="0x7e7077fb5c507cfe1d0b1743430e5370fa1caca11f0eb39db203f4c0903601eb",
    address_const=FWX_ADDRESS
)
# with open(project_dir+"/defi_sdk_py/address/fwx_address.json", 'r') as file:
#     json_data = json.load(file)

# a = AddressConst(json_data)
