from ..abi.IHelperCore import *
from ..abi.IHelperFutureTrade import IHelperFutureTrade, PositionState, PositionData
from ..abi.IERC20Metadata import IERC20Metadata
from ..abi.IAPHCore import Pair
from ..utils import parseEther,Day
from typing import List


class GetPositionStates:
    def __init__(self, position_states: List[PositionState], next_cursor: int) -> None:
        self.position_states = position_states
        self.next_cursor = next_cursor

    def __str__(self):
        return str({
            "position_states": [i.__str__() for i in self.position_states],
            "next_cursor": self.next_cursor
        })

class UnrealizedPNL:
    def __init__(self, pnl: int, roe: int) -> None:
        self.pnl = pnl
        self.roe = roe

    def __str__(self):
        return str({
            "PNL": self.pnl,
            "ROE": self.roe
        })

class EntryPrice:
    def __init__(self, entry_price: int, swap_fee: int, swap_size: int) -> None:
        self.entry_price = entry_price
        self.swap_fee = swap_fee
        self.swap_size = swap_size

    def __str__(self):
        return str({
            "entry_price": self.entry_price,
            "swap_fee": self.swap_fee,
            "swap_size": self.swap_size
        })

class GetBalanceDetails:
    def __init__(self, free_balance: int, used_balance: int, total_balance: int) -> None:
        self.free_balance = free_balance
        self.used_balance = used_balance
        self.total_balance = total_balance

    def __str__(self):
        return str({
            "free_balance": self.free_balance,
            "used_balance": self.used_balance,
            "total_balance": self.total_balance
        })

class OpeningClosingFee:
    def __init__(self, swap_fee: int, trading_fee: int, total_fee: int) -> None:
        self.swap_fee = swap_fee
        self.trading_fee = trading_fee
        self.total_fee = total_fee

    def __str__(self):
        return str({
            "swap_fee": self.swap_fee,
            "trading_fee": self.trading_fee,
            "total_fee": self.total_fee
        })

class HelperFutureTrade:

    def __init__(self):
        super(HelperFutureTrade, self).__init__()
        self.helper_future_trade:IHelperFutureTrade = IHelperFutureTrade(self.address_const.get_helper_future_trade_address(), self.web3)

    def get_unrealized_pnl(self, nft_id:int, pair_byte:str)->UnrealizedPNL:
        return UnrealizedPNL(*self.helper_future_trade.getUnrealizedPNL(nft_id, pair_byte).call())

    def get_entry_price(
        self,
        nft_id:int,
        pair_byte:str,
        is_long:bool,
        contract_size:int,
        expected_rate:int,
        slip_page:int
    )->EntryPrice:
        pair:Pair = self.pairs_by_byte(pair_byte)
        collateral_token:IERC20Metadata = IERC20Metadata(pair.pair0, self.web3)
        underlying_token:IERC20Metadata = IERC20Metadata(pair.pair1, self.web3)
        contract_size = parseEther(self.web3, contract_size, underlying_token.decimals().call())
        expected_rate = parseEther(self.web3, expected_rate, collateral_token.decimals().call())
        slip_page = parseEther(self.web3, slip_page)
        return EntryPrice(*self.helper_future_trade.getEntryPrice(
            nft_id,
            pair_byte,
            is_long,
            contract_size,
            expected_rate,
            slip_page
        ).call())
    
    def get_balance_details(self, nft_id:int, pair_byte:str)->GetBalanceDetails:
        return GetBalanceDetails(*(self.helper_future_trade.getBalanceDetails(nft_id, pair_byte).call()))
    
    def get_position_margin(self, nft_id:int, pair_byte:str)->int:
        return self.helper_future_trade.getPositionMargin(nft_id, pair_byte).call()

    def get_max_withdrawal(self, nft_id:int, pair_byte:str)->int:
        return self.helper_future_trade.getMaxWithdrawal(nft_id, pair_byte).call()

    def get_liquidation_price(self, nft_id:int, pair_byte:str)->int:
        return self.helper_future_trade.getLiquidationPrice(nft_id, pair_byte).call()

    def get_margin_after_adjust_collateral(self,
        nft_id:int,
        pair_byte:str,
        is_add:bool,
        amount:int
    )->int:
        pair:Pair = self.pairs_by_byte(pair_byte)
        collateral_token:IERC20Metadata = IERC20Metadata(pair.pair0, self.web3)
        amount = parseEther(self.web3, amount, collateral_token.decimals().call())
        return self.helper_future_trade.getMarginAfterAdjustCollateral(
            nft_id,
            pair_byte,
            is_add,
            amount
        ).call()

    def get_opening_fee(self,
        nft_id:int,
        pair_byte:str,
        is_long:bool,
        contract_size:int,
        expected_rate:int,
        slip_page:int
    )->OpeningClosingFee:
        pair:Pair = self.pairs_by_byte(pair_byte)
        collateral_token:IERC20Metadata = IERC20Metadata(pair.pair0, self.web3)
        underlying_token:IERC20Metadata = IERC20Metadata(pair.pair1, self.web3)
        contract_size = parseEther(self.web3, contract_size, underlying_token.decimals().call())
        expected_rate = parseEther(self.web3, expected_rate, collateral_token.decimals().call())
        slip_page = parseEther(self.web3, slip_page)
        return OpeningClosingFee(*self.helper_future_trade.getOpeningFee(
            nft_id,
            pair_byte,
            is_long,
            contract_size,
            expected_rate,
            slip_page
        ).call())

    def get_closing_fee(self,
        nft_id:int,
        pair_byte:str,
        contract_size:int
    )->OpeningClosingFee:
        pair:Pair = self.pairs_by_byte(pair_byte)
        underlying_token:IERC20Metadata = IERC20Metadata(pair.pair1, self.web3)
        contract_size = parseEther(self.web3, contract_size, underlying_token.decimals().call())
        return OpeningClosingFee(*self.helper_future_trade.getClosingFee(
            nft_id,
            pair_byte,
            contract_size
        ).call())
    
    def get_required_collateral(self,
        nft_id:int,
        pair_byte:str,
        is_long:bool,
        contract_size:int,
        leverage:int,
        expected_rate:int,
        slip_page:int
    )->int:
        pair:Pair = self.pairs_by_byte(pair_byte)
        collateral_token:IERC20Metadata = IERC20Metadata(pair.pair0, self.web3)
        underlying_token:IERC20Metadata = IERC20Metadata(pair.pair1, self.web3)
        contract_size = parseEther(self.web3, contract_size, underlying_token.decimals().call())
        expected_rate = parseEther(self.web3, expected_rate, collateral_token.decimals().call())
        slip_page = parseEther(self.web3, slip_page)
        leverage = parseEther(self.web3, leverage)
        return self.helper_future_trade.getRequiredCollateral(
            nft_id,
            pair_byte,
            is_long,
            contract_size,
            leverage,
            expected_rate,
            slip_page
        ).call()

    def get_average_price(self,
        nft_id:int,
        pair_byte:str,
        is_long:bool,
        contract_size:int,
        expected_rate:int,
        slip_page:int
    )->int:
        pair:Pair = self.pairs_by_byte(pair_byte)
        collateral_token:IERC20Metadata = IERC20Metadata(pair.pair0, self.web3)
        underlying_token:IERC20Metadata = IERC20Metadata(pair.pair1, self.web3)
        contract_size = parseEther(self.web3, contract_size, underlying_token.decimals().call())
        expected_rate = parseEther(self.web3, expected_rate, collateral_token.decimals().call())
        slip_page = parseEther(self.web3, slip_page)
        return self.helper_future_trade.getAveragePrice(
            nft_id,
            pair_byte,
            is_long,
            contract_size,
            expected_rate,
            slip_page
        ).call()

    def get_pnl_after_close_position(self, nft_id:int, pair_byte:str, contract_size:int)->UnrealizedPNL:
        pair:Pair = self.pairs_by_byte(pair_byte)
        underlying_token:IERC20Metadata = IERC20Metadata(pair.pair1, self.web3)
        contract_size = parseEther(self.web3, contract_size, underlying_token.decimals().call())
        return UnrealizedPNL(*self.helper_future_trade.getPNLAfterClosePosition(nft_id, pair_byte, contract_size).call())
    
    def get_margin_after_close_position(self, nft_id:int, pair_byte:str, contract_size:int)->int:
        pair:Pair = self.pairs_by_byte(pair_byte)
        underlying_token:IERC20Metadata = IERC20Metadata(pair.pair1, self.web3)
        contract_size = parseEther(self.web3, contract_size, underlying_token.decimals().call())
        return self.helper_future_trade.getMarginAfterClosePosition(nft_id, pair_byte, contract_size).call()
    
    def get_balance_after_open_position(self,
        nft_id:int,
        pair_byte:str,
        is_long:bool,
        contract_size:int,
        expected_rate:int,
        slip_page:int
    )->int:
        pair:Pair = self.pairs_by_byte(pair_byte)
        collateral_token:IERC20Metadata = IERC20Metadata(pair.pair0, self.web3)
        underlying_token:IERC20Metadata = IERC20Metadata(pair.pair1, self.web3)
        contract_size = parseEther(self.web3, contract_size, underlying_token.decimals().call())
        expected_rate = parseEther(self.web3, expected_rate, collateral_token.decimals().call())
        slip_page = parseEther(self.web3, slip_page)
        return self.helper_future_trade.getBalanceAfterOpenPosition(
            nft_id,
            pair_byte,
            is_long,
            contract_size,
            expected_rate,
            slip_page
        ).call()

    def get_liquidate_price_after_open_position(self,
        nft_id:int,
        pair_byte:str,
        is_long:bool,
        contract_size:int,
        expected_rate:int,
        slip_page:int
    )->int:
        pair:Pair = self.pairs_by_byte(pair_byte)
        collateral_token:IERC20Metadata = IERC20Metadata(pair.pair0, self.web3)
        underlying_token:IERC20Metadata = IERC20Metadata(pair.pair1, self.web3)
        contract_size = parseEther(self.web3, contract_size, underlying_token.decimals().call())
        expected_rate = parseEther(self.web3, expected_rate, collateral_token.decimals().call())
        slip_page = parseEther(self.web3, slip_page)
        return self.helper_future_trade.getLiqPriceAfterOpenPosition(
            nft_id,
            pair_byte,
            is_long,
            contract_size,
            expected_rate,
            slip_page
        ).call()

    def get_margin_after_open_position(self,
        nft_id:int,
        pair_byte:str,
        is_long:bool,
        contract_size:int,
        expected_rate:int,
        slip_page:int
    )->int:
        pair:Pair = self.pairs_by_byte(pair_byte)
        collateral_token:IERC20Metadata = IERC20Metadata(pair.pair0, self.web3)
        underlying_token:IERC20Metadata = IERC20Metadata(pair.pair1, self.web3)
        contract_size = parseEther(self.web3, contract_size, underlying_token.decimals().call())
        expected_rate = parseEther(self.web3, expected_rate, collateral_token.decimals().call())
        slip_page = parseEther(self.web3, slip_page)
        return self.helper_future_trade.getMarginAfterOpenPosition(
            nft_id,
            pair_byte,
            is_long,
            contract_size,
            expected_rate,
            slip_page
        ).call()

    def get_max_contract_size(
        self,
        nft_id:int,
        pair_byte:str,
        is_long:bool,
        leverage:int,
        expected_rate:int,
        slip_page:int
    )->int:
        pair:Pair = self.pairs_by_byte(pair_byte)
        collateral_token:IERC20Metadata = IERC20Metadata(pair.pair0, self.web3)
        expected_rate = parseEther(self.web3, expected_rate, collateral_token.decimals().call())
        slip_page = parseEther(self.web3, slip_page)
        leverage = parseEther(self.web3, leverage)
        return self.helper_future_trade.getMaxContractSize(
            nft_id,
            pair_byte,
            is_long,
            leverage,
            expected_rate,
            slip_page
        ).call()
    
    def get_position_states(self, nft_id:int, cursor:int=1, result_per_page:int=1)->GetPositionStates:
        pos_state = self.helper_future_trade.getPositionStates(nftId=nft_id, cursor=cursor, resultsPerPage=result_per_page).call()
        result = GetPositionStates(
            position_states= [PositionState(*i) for i in pos_state[0]],
            next_cursor=pos_state[1]
        )
        return result

    def get_all_active_positions(self, nft_id:int)->List[PositionData]:
        return [PositionData(*i) for i in (self.helper_future_trade.getAllActivePositions(nftId=nft_id).call())]

    
    
    


    





