import sys
import os
import json
project_dir = os.path.abspath("")
sys.path.append(project_dir)
from defi_sdk_py import ChainClient
from defi_sdk_py.fwx_chain import ADDRESS as FWX_ADDRESS
from defi_sdk_py.fwx_chain import FWXChainClient


# FWXChain = ChainClient(
#     rpc_url="https://node.forwardx.space/",
#     private_key="0x7e7077fb5c507cfe1d0b1743430e5370fa1caca11f0eb39db203f4c0903601eb",
#     address_const=FWX_ADDRESS
# )
clientFWX = FWXChainClient(
    rpc_url="https://node.forwardx.space/",
    private_key="0x7e7077fb5c507cfe1d0b1743430e5370fa1caca11f0eb39db203f4c0903601eb",
    address_const=FWX_ADDRESS
)
print("address : ", clientFWX.address)
print("native balance : ",clientFWX.getBalance())
print(clientFWX.TOKEN.BTC.address)
print(clientFWX.TOKEN.BTC)
# print(clientFWX.TOKEN.BTC.balanceOf("0xC63dD209434079005E51D34e2b22118d75D1cA0C"))
# event_filter = clientFWX.TOKEN.BTC.eventTransfer(0,0)
# print(event_filter)
