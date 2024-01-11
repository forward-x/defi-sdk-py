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
    # private_key="0x7e7077fb5c507cfe1d0b1743430e5370fa1caca11f0eb39db203f4c0903601eb",
    private_key="0xe90c257fd5f0761fdf915e7b4edfbf1b8724dd3455368f1a8d10939abaf0bc39",
    address_const=FWX_ADDRESS,
    maxFeePerGas=3000000,
    maxPriorityFeePerGas=2000000,
)
print("address : ", clientFWX.address)
print("native balance : ",clientFWX.get_balance())

# clientFWX.core.check_staking_amount_sufficient(1, 1000, clientFWX.TOKEN.USDT)

pair_USDT_WBNB = clientFWX.hashPair(clientFWX.TOKEN.USDT, clientFWX.TOKEN.WBNB)
clientFWX.wallets(13, pair_USDT_WBNB)

# print(clientFWX.TOKEN.BTC.balanceOf("0xC63dD209434079005E51D34e2b22118d75D1cA0C"))
# event_filter = clientFWX.TOKEN.BTC.eventTransfer(0,0)
# print(event_filter)
