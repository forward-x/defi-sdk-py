from ..address import ExtendedAddressConst,AddressConst
import json
import os
import sys

project_dir = os.path.abspath("")
sys.path.append(project_dir)
with open(project_dir+"/defi_sdk_py/fwx_chain/address.json", 'r') as file:
    json_data = json.load(file)
ADDRESS = ExtendedAddressConst(json_data)
