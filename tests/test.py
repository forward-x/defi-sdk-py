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

nft_id = 13
pair_USDT_WBNB = clientFWX.hash_pair(clientFWX.TOKEN.USDT, clientFWX.TOKEN.WBNB)
wallets = clientFWX.wallets(nft_id, pair_USDT_WBNB)
trading_collateral_whitelist = clientFWX.trading_collateral_whitelist(clientFWX.TOKEN.USDT)
positions = clientFWX.positions(nft_id, pair_USDT_WBNB)
positions_state = clientFWX.positions_states(nft_id, positions.id)
current_loan_index = clientFWX.current_loan_index(nft_id)
loans = clientFWX.loans(nft_id, current_loan_index)
loanExts = clientFWX.loanExts(nft_id, current_loan_index)
# adjust_collateral_to_loan = clientFWX.adjust_collateral(nft_id, current_loan_index, 1, True)
# deposit_collateral = clientFWX.deposit_collateral(nft_id, clientFWX.TOKEN.USDT, 100)
# deposit_collateral = clientFWX.deposit_collateral(nft_id, clientFWX.TOKEN.USDT, 100)
# rollover = clientFWX.rollver(nft_id, current_loan_index)
# rollover = clientFWX.repay(nft_id, current_loan_index, 1, True)
# rollover = clientFWX.repay(nft_id, current_loan_index, 1, False)
# close_position = clientFWX.close_position(nft_id, positions.id, 0.5)
# liquidate_loan = clientFWX.liquidate(nft_id, current_loan_index)
# liquidate_position = clientFWX.liquidate_position(nft_id, positions_state.pairByte)


# print(clientFWX.TOKEN.BTC.balanceOf("0xC63dD209434079005E51D34e2b22118d75D1cA0C"))
# event_filter = clientFWX.TOKEN.BTC.eventTransfer(0,0)
# print(event_filter)
