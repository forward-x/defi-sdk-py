import json
import os
import sys

project_dir = os.path.abspath("")
sys.path.append(project_dir)

from defi_sdk_py import AddressConst

with open(project_dir+"/defi_sdk_py/address/fwx_address.json", 'r') as file:
    json_data = json.load(file)

a = AddressConst(json_data)
