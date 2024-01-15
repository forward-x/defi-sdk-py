from ..address import AddressConst
import json
import os
import sys

project_dir = os.path.abspath("")
sys.path.append(project_dir)
with open(project_dir+"/defi_sdk_py/avax_fuji_chain/address.json", 'r') as file:
    json_data = json.load(file)
ADDRESS = AddressConst(json_data)
