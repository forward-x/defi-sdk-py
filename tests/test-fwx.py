import sys
import os
from dotenv import load_dotenv
load_dotenv()

project_dir = os.path.abspath("")
sys.path.append(project_dir)
from defi_sdk_py.fwx_chain import ADDRESS as FWX_ADDRESS
from defi_sdk_py.fwx_chain import FWXChainClient
PK = os.environ.get("PK")
FWX_RPC_URL = os.environ.get("FWX_RPC_URL")

clientFWX = FWXChainClient(
    rpc_url=FWX_RPC_URL,
    private_key=PK,
    address_const=FWX_ADDRESS,
    maxFeePerGas=3000000,
    maxPriorityFeePerGas=2000000,
)
print("address : ", clientFWX.address)
print("native balance : ",clientFWX.get_balance())

# clientFWX.core.check_staking_amount_sufficient(1, 1000, clientFWX.TOKEN.USDT)

current_pool = clientFWX.current_pool();
nft_id = clientFWX.get_default_membership(clientFWX.address);
get_pool_list = clientFWX.get_pool_lists();
get_previous_pool = clientFWX.get_previous_pool();
get_rank_pool = clientFWX.get_rank_pool(clientFWX.POOLS.USDT, nft_id);
get_rank = clientFWX.get_rank(nft_id=nft_id);
get_refferrer = clientFWX.get_refferrer(nft_id=nft_id);
# mint = clientFWX.mint(nft_id)
# set_default_membership = clientFWX.set_default_membership(nft_id)

pair_USDT_WBNB = clientFWX.pairs(clientFWX.TOKEN.USDT, clientFWX.TOKEN.WBNB)
pair_USDT_WBNB = clientFWX.pairs_by_byte(pair_USDT_WBNB)
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

# deposit = clientFWX.deposit(clientFWX.POOLS.WBNB, nft_id, 1,)

# tx_hash = "0x62461c427c4dcffca2a4881c3de6ac88b19c32522214f622a3a1605b52d2bb4c"
# deposit_event = clientFWX.deposit_event_tx(clientFWX.POOLS.WBNB, tx_hash)
# deposit_event = clientFWX.deposit_event_block(clientFWX.POOLS.WBNB, 6405763, 6405775)


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
# approve_token = clientFWX.approve(clientFWX.TOKEN.FWX, clientFWX.stakepool.address, clientFWX.web3.to_wei(1000000000, 'ether'))

# stake = clientFWX.stake(nft_id, 250000)
# unstake = clientFWX.unstake(nft_id, 250000)
rank_infos = clientFWX.rank_infos(0)
rank_infos = clientFWX.rank_infos(1)
rank_len = clientFWX.rank_len()
pool_start_timestamp = clientFWX.pool_start_timestamp()
settle_interval = clientFWX.settle_interval()
settle_period = clientFWX.settle_period()
get_stake_info = clientFWX.get_stake_info(nft_id)
get_max_ltv = clientFWX.get_max_ltv(nft_id)

get_active_loans = clientFWX.get_active_loans(nft_id, 1, 10)
get_loan_borrow_amount = clientFWX.get_loan_borrow_amount(nft_id,3)
get_loan_collateral_info = clientFWX.get_loan_collateral_info(nft_id,3)
# print(get_active_loans.active_loan_infos[0])
get_settle_borrow_info = clientFWX.get_settle_borrow_info(nft_id, 1)

calculate_ltv_for_borrow = clientFWX.calculate_ltv_for_borrow(
    nft_id,
    1,
    1000,
    clientFWX.TOKEN.USDT,
    100,
    clientFWX.TOKEN.WBNB
    )

calculate_ltv_for_repay = clientFWX.calculate_ltv_for_repay(
    nft_id,
    1,
    5000,
    False
)

calculate_ltv_for_adjust_collateral = clientFWX.calculate_ltv_for_adjust_collateral(
    nft_id,
    1,
    10,
    True
)

calculate_borrow_amount = clientFWX.calculate_borrow_amount(
    nft_id,
    1,
    1000,
    clientFWX.TOKEN.USDT,
    10,
    clientFWX.TOKEN.WBNB,
    30
)

get_stake_pool_next_settle_timestamp = clientFWX.get_stake_pool_next_settle_timestamp(clientFWX.stakepool)
get_nft_list = clientFWX.get_nft_list(clientFWX.address)
get_rank_info_list = clientFWX.get_rank_info_list()
get_stake_info = clientFWX.get_stake_info(5)

claimble_interest = clientFWX.claimble_interest(clientFWX.POOLS.USDT, 5)
claimble_interest_membership = clientFWX.claimble_interest_membership(clientFWX.POOLS.USDT, 5)

get_next_lending_forw_interest = clientFWX.get_next_lending_forw_interest(clientFWX.POOLS.USDT, 100, 0.00015)
get_next_lending_interest = clientFWX.get_next_lending_interest(clientFWX.POOLS.USDT, 10000)

get_interest_amount_by_deposit_amount = clientFWX.get_interest_amount_by_deposit_amount(clientFWX.POOLS.USDT, 10000, 86400)
get_deposit_amount_by_interest_amount = clientFWX.get_deposit_amount_by_interest_amount(clientFWX.POOLS.USDT, 10000, 86400)

calculate_borrowing_interest = clientFWX.calculate_borrowing_interest(
    clientFWX.POOLS.USDT,
    1000,
    10,
    clientFWX.TOKEN.WBNB,
    86400
)

get_pool_info = clientFWX.get_pool_info(clientFWX.POOLS.USDT, 0.00015)
get_lending_info = clientFWX.get_lending_info(clientFWX.POOLS.USDT, 5)
get_unrealized_pnl = clientFWX.get_unrealized_pnl(5, pair_USDT_WBNB)
get_entry_price = clientFWX.get_entry_price(
    nft_id=nft_id,
    pair_byte=pair_USDT_WBNB,
    is_long=True,
    contract_size=5,
    expected_rate=315,
    slip_page=5
)
get_balance_details = clientFWX.get_balance_details(nft_id, pair_USDT_WBNB)
get_position_margin = clientFWX.get_margin_after_adjust_collateral(
    nft_id,
    pair_USDT_WBNB,
    True,
    100
)

get_max_withdrawal = clientFWX.get_max_withdrawal(nft_id, pair_USDT_WBNB)

get_liquidation_price = clientFWX.get_liquidation_price(nft_id, pair_USDT_WBNB)

get_opening_fee = clientFWX.get_opening_fee(
    nft_id=nft_id,
    pair_byte=pair_USDT_WBNB,
    is_long=True,
    contract_size=5,
    expected_rate=315,
    slip_page=5
)

get_closing_fee = clientFWX.get_closing_fee(
    nft_id=nft_id,
    pair_byte=pair_USDT_WBNB,
    contract_size=5,
)

get_required_collateral = clientFWX.get_required_collateral(
    nft_id=nft_id,
    pair_byte=pair_USDT_WBNB,
    is_long=True,
    contract_size=5,
    leverage=5,
    expected_rate=315,
    slip_page=5
)

get_average_price = clientFWX.get_average_price(
    nft_id=nft_id,
    pair_byte=pair_USDT_WBNB,
    is_long=True,
    contract_size=5,
    expected_rate=315,
    slip_page=5
)

get_pnl_after_close_position = clientFWX.get_pnl_after_close_position(
    nft_id=nft_id,
    pair_byte=pair_USDT_WBNB,
    contract_size=5,
)

get_margin_after_close_position = clientFWX.get_margin_after_close_position(
    nft_id=nft_id,
    pair_byte=pair_USDT_WBNB,
    contract_size=5,
)

get_balance_after_open_position = clientFWX.get_balance_after_open_position(
    nft_id=nft_id,
    pair_byte=pair_USDT_WBNB,
    is_long=True,
    contract_size=5,
    expected_rate=315,
    slip_page=5
)

get_liquidate_price_after_open_position = clientFWX.get_liquidate_price_after_open_position(
    nft_id=nft_id,
    pair_byte=pair_USDT_WBNB,
    is_long=True,
    contract_size=5,
    expected_rate=315,
    slip_page=5
)

get_margin_after_open_position = clientFWX.get_margin_after_open_position(
    nft_id=nft_id,
    pair_byte=pair_USDT_WBNB,
    is_long=True,
    contract_size=5,
    expected_rate=315,
    slip_page=5
)

get_max_contract_size = clientFWX.get_max_contract_size(
    nft_id=nft_id,
    pair_byte=pair_USDT_WBNB,
    is_long=True,
    leverage=5,
    expected_rate=315,
    slip_page=5
)

get_position_states = clientFWX.get_position_states(nft_id, 1, 10)

get_all_active_positions = clientFWX.get_all_active_positions(nft_id)
print(get_all_active_positions[0])
