import sys
import os
import json
project_dir = os.path.abspath("")
sys.path.append(project_dir)
from defi_sdk_py import ChainClient
from defi_sdk_py.fwx_chain import ADDRESS as FWX_ADDRESS
from defi_sdk_py.fwx_chain import FWXChainClient

clientFWX = FWXChainClient(
    rpc_url="https://node.forwardx.space/",
    private_key="0x58acc8bcee8f34690b50880c17c5ea10b2b4c094f6e4f3f44756a817d986e509",
    address_const=FWX_ADDRESS,
    maxFeePerGas=3000000,
    maxPriorityFeePerGas=2000000,
)
print("address : ", clientFWX.address)
print("native balance : ",clientFWX.get_balance())

# clientFWX.core.check_staking_amount_sufficient(1, 1000, clientFWX.TOKEN.USDT)

nft_id = 324
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

token_address = clientFWX.token_address(clientFWX.POOLS.USDT)
lenders = clientFWX.lenders(clientFWX.POOLS.USDT, nft_id)
token_holders = clientFWX.token_holders(clientFWX.POOLS.USDT, nft_id)
current_supply = clientFWX.current_supply(clientFWX.POOLS.USDT)
get_next_borrowing_interest = clientFWX.get_next_borrowing_interest(clientFWX.POOLS.USDT, 10000)

# deposit = clientFWX.deposit(clientFWX.POOLS.WBNB, nft_id, 10)
# deposit = clientFWX.deposit(clientFWX.POOLS.USDT, nft_id, 10)
# withdraw = clientFWX.withdraw(clientFWX.POOLS.USDT, nft_id, 10)
# withdraw = clientFWX.withdraw(clientFWX.POOLS.WBNB, nft_id, 10)
# active_rank = clientFWX.active_rank(clientFWX.POOLS.USDT, nft_id)
# claim_all_interest = clientFWX.claim_all_interest(clientFWX.POOLS.USDT, nft_id)
# claim_token_interest = clientFWX.claim_token_interest(clientFWX.POOLS.USDT, nft_id, 100)
# claim_forw_interest = clientFWX.claim_forw_interest(clientFWX.POOLS.USDT, nft_id, 100)
# borrow = clientFWX.borrow(clientFWX.POOLS.USDT, nft_id, 0, 1000, 10, clientFWX.TOKEN.WBNB)
# open_position = clientFWX.open_position(
#     nft_id=nft_id,
#     is_long=True,
#     collateral_token=clientFWX.TOKEN.USDT,
#     underlying_token=clientFWX.TOKEN.WBNB,
#     entry_price=308,
#     size=5,
#     leverage=5,
#     slip_page=10,
# )

a = clientFWX.approve(clientFWX.TOKEN.BTC, "0xC63dD209434079005E51D34e2b22118d75D1cA0C", 1000)
print(a)

# print(clientFWX.TOKEN.BTC.balanceOf("0xC63dD209434079005E51D34e2b22118d75D1cA0C"))
# event_filter = clientFWX.TOKEN.BTC.eventTransfer(0,0)
# print(event_filter)
