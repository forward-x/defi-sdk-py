import sys
import os
import json
from dotenv import load_dotenv
load_dotenv()
project_dir = os.path.abspath("")
sys.path.append(project_dir)
from defi_sdk_py import ChainClient
from defi_sdk_py.avax_fuji_chain import ADDRESS as FUJI_ADDRESS
from defi_sdk_py.avax_fuji_chain import AVAXFUJIChainClient

PK = os.environ.get("PK")
FUJI_RPC_URL = os.environ.get("FUJI_RPC_URL")
clientFUJI = AVAXFUJIChainClient(
    rpc_url=FUJI_RPC_URL,
    private_key=PK,
    address_const=FUJI_ADDRESS,
    maxFeePerGas=3000000,
    maxPriorityFeePerGas=2000000,
)
print("address : ", clientFUJI.address)
print("native balance : ",clientFUJI.get_balance())

current_pool = clientFUJI.current_pool();
nft_id = clientFUJI.get_default_membership(clientFUJI.address);
get_pool_list = clientFUJI.get_pool_lists();
get_previous_pool = clientFUJI.get_previous_pool();
get_rank_pool = clientFUJI.get_rank_pool(clientFUJI.POOLS.USDC, nft_id);
get_rank = clientFUJI.get_rank(nft_id=nft_id);
get_refferrer = clientFUJI.get_refferrer(nft_id=nft_id);
if nft_id == 0:
    mint = clientFUJI.mint(nft_id)
nft_id = clientFUJI.get_default_membership(clientFUJI.address);

pair_USDC_WAVAX = clientFUJI.hash_pair(clientFUJI.TOKEN.USDC, clientFUJI.TOKEN.WAVAX)
wallets = clientFUJI.wallets(nft_id, pair_USDC_WAVAX)
trading_collateral_whitelist = clientFUJI.trading_collateral_whitelist(clientFUJI.TOKEN.USDC)
positions = clientFUJI.positions(nft_id, pair_USDC_WAVAX)
positions_state = clientFUJI.positions_states(nft_id, positions.id)
current_loan_index = clientFUJI.current_loan_index(nft_id)

# loans = clientFUJI.loans(nft_id, current_loan_index)
# loanExts = clientFUJI.loanExts(nft_id, current_loan_index)
exit(1)
# adjust_collateral_to_loan = clientFUJI.adjust_collateral(nft_id, current_loan_index, 1, True)
# deposit_collateral = clientFUJI.deposit_collateral(nft_id, clientFUJI.TOKEN.USDC, 100)
# deposit_collateral = clientFUJI.deposit_collateral(nft_id, clientFUJI.TOKEN.USDC, 100)
# rollover = clientFUJI.rollver(nft_id, current_loan_index)
# rollover = clientFUJI.repay(nft_id, current_loan_index, 1, True)
# rollover = clientFUJI.repay(nft_id, current_loan_index, 1, False)
# close_position = clientFUJI.close_position(nft_id, positions.id, 0.5)
# liquidate_loan = clientFUJI.liquidate(nft_id, current_loan_index)
# liquidate_position = clientFUJI.liquidate_position(nft_id, positions_state.pairByte)

token_address = clientFUJI.token_address(clientFUJI.POOLS.USDC)
lenders = clientFUJI.lenders(clientFUJI.POOLS.USDC, nft_id)
token_holders = clientFUJI.token_holders(clientFUJI.POOLS.USDC, nft_id)
current_supply = clientFUJI.current_supply(clientFUJI.POOLS.USDC)
get_next_borrowing_interest = clientFUJI.get_next_borrowing_interest(clientFUJI.POOLS.USDC, 10000)

# deposit = clientFUJI.deposit(clientFUJI.POOLS.WBNB, nft_id, 1,)

# tx_hash = "0x62461c427c4dcffca2a4881c3de6ac88b19c32522214f622a3a1605b52d2bb4c"
# deposit_event = clientFUJI.deposit_event_tx(clientFUJI.POOLS.WBNB, tx_hash)
# deposit_event = clientFUJI.deposit_event_block(clientFUJI.POOLS.WBNB, 6405763, 6405775)


# deposit = clientFUJI.deposit(clientFUJI.POOLS.USDC, nft_id, 10)
# withdraw = clientFUJI.withdraw(clientFUJI.POOLS.USDC, nft_id, 10)
# withdraw = clientFUJI.withdraw(clientFUJI.POOLS.WBNB, nft_id, 10)
# active_rank = clientFUJI.active_rank(clientFUJI.POOLS.USDC, nft_id)
# claim_all_interest = clientFUJI.claim_all_interest(clientFUJI.POOLS.USDC, nft_id)
# claim_token_interest = clientFUJI.claim_token_interest(clientFUJI.POOLS.USDC, nft_id, 100)
# claim_forw_interest = clientFUJI.claim_forw_interest(clientFUJI.POOLS.USDC, nft_id, 100)
# borrow = clientFUJI.borrow(clientFUJI.POOLS.USDC, nft_id, 0, 1000, 10, clientFUJI.TOKEN.WBNB)
# open_position = clientFUJI.open_position(
#     nft_id=nft_id,
#     is_long=True,
#     collateral_token=clientFUJI.TOKEN.USDC,
#     underlying_token=clientFUJI.TOKEN.WBNB,
#     entry_price=308,
#     size=5,
#     leverage=5,
#     slip_page=10,
# )
# approve_token = clientFUJI.approve(clientFUJI.TOKEN.FWX, clientFUJI.stakepool.address, clientFUJI.web3.to_wei(1000000000, 'ether'))

# stake = clientFUJI.stake(nft_id, 250000)
# unstake = clientFUJI.unstake(nft_id, 250000)
rank_infos = clientFUJI.rank_infos(0)
rank_infos = clientFUJI.rank_infos(1)
rank_len = clientFUJI.rank_len()
pool_start_timestamp = clientFUJI.pool_start_timestamp()
settle_interval = clientFUJI.settle_interval()
settle_period = clientFUJI.settle_period()
get_stake_info = clientFUJI.get_stake_info(17)
get_max_ltv = clientFUJI.get_max_ltv(17)

get_active_loans = clientFUJI.get_active_loans(17, 1, 10)
get_loan_borrow_amount = clientFUJI.get_loan_borrow_amount(17,3)
get_loan_collateral_info = clientFUJI.get_loan_collateral_info(17,3)

# print(clientFUJI.TOKEN.BTC.balanceOf("0xC63dD209434079005E51D34e2b22118d75D1cA0C"))
# event_filter = clientFUJI.TOKEN.BTC.eventTransfer(0,0)
# print(event_filter)
