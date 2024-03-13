from ..abi.IHelperCore import *
from ..abi.IHelperFutureTrade import IHelperFutureTrade, PositionState, PositionData
from ..abi.IERC20Metadata import IERC20Metadata
from ..abi.IAPHCore import Pair
from ..utils import parseEther,Day
from typing import List


class GetPositionStates:
    """
    Represents the state of positions along with pagination information.

    :param position_states: A list of PositionState objects
    :param next_cursor: The cursor for the next page of results
    """
    def __init__(self, position_states: List[PositionState], next_cursor: int) -> None:
        self.position_states = position_states
        self.next_cursor = next_cursor

    def __str__(self):
        return str({
            "position_states": [i.__str__() for i in self.position_states],
            "next_cursor": self.next_cursor
        })

class UnrealizedPNL:
    """
    Represents the unrealized profit or loss (PNL) and return on equity (ROE).

    :param pnl: The unrealized profit or loss
    :param roe: The return on equity
    """
    def __init__(self, pnl: int, roe: int) -> None:
        self.pnl = pnl
        self.roe = roe

    def __str__(self):
        return str({
            "PNL": self.pnl,
            "ROE": self.roe
        })

class EntryPrice:
    """
    Represents the entry price details of a position.

    :param entry_price: The entry price of the position
    :param swap_fee: The swap fee incurred
    :param swap_size: The size of the swap
    """
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
    """
    Represents the balance details of an account.

    :param free_balance: The free balance that is not used as margin
    :param used_balance: The balance used as margin
    :param total_balance: The total balance of the account
    """
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
    """
    Represents the fees associated with opening or closing a position.

    :param swap_fee: The fee for swapping
    :param trading_fee: The fee for trading
    :param total_fee: The total fee incurred
    """
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
    """
    HelperFutureTrade provides utility functions to assist with future trade calculations.
    """

    def __init__(self):
        """
        Initializes the HelperFutureTrade by setting up the helper future trade contract interface.
        """
        super(HelperFutureTrade, self).__init__()
        self.helper_future_trade:IHelperFutureTrade = IHelperFutureTrade(self.address_const.get_helper_future_trade_address(), self.web3)

    def get_unrealized_pnl(self, nft_id:int, pair_byte:str)->UnrealizedPNL:
        """
        Retrieves the unrealized profit or loss (PNL) and return on equity (ROE) for a given position.
        
        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :return: An UnrealizedPNL object containing the PNL and ROE
        """
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
        """
        Calculates the entry price for a new position.
        
        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :param is_long: A boolean indicating if the position is long (True) or short (False)
        :param contract_size: The size of the contract
        :param expected_rate: The expected rate for the position
        :param slip_page: The slippage percentage
        :return: An EntryPrice object containing the entry price, swap fee, and swap size
        """
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
        """
        Retrieves the balance details for a given NFT ID and pair.
        
        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :return: A GetBalanceDetails object containing the free, used, and total balance details
        """
        return GetBalanceDetails(*(self.helper_future_trade.getBalanceDetails(nft_id, pair_byte).call()))
    
    def get_position_margin(self, nft_id:int, pair_byte:str)->int:
        """
        Retrieves the margin requirement for a given position.
        
        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :return: The margin requirement for the position
        """
        return self.helper_future_trade.getPositionMargin(nft_id, pair_byte).call()

    def get_max_withdrawal(self, nft_id:int, pair_byte:str)->int:
        """
        Calculates the maximum amount that can be withdrawn from the margin of a given position.
        
        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :return: The maximum withdrawal amount
        """

        return self.helper_future_trade.getMaxWithdrawal(nft_id, pair_byte).call()

    def get_liquidation_price(self, nft_id:int, pair_byte:str)->int:
        """
        Calculates the liquidation price for a given position.
        
        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :return: The liquidation price
        """

        return self.helper_future_trade.getLiquidationPrice(nft_id, pair_byte).call()

    def get_margin_after_adjust_collateral(self,
        nft_id:int,
        pair_byte:str,
        is_add:bool,
        amount:int
    )->int:
        """
        Calculates the margin after adjusting the collateral for a given position.
        
        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :param is_add: A boolean indicating if collateral is being added (True) or removed (False)
        :param amount: The amount of collateral to adjust
        :return: The margin after collateral adjustment
        """
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
        """
        Calculates the opening fee for initiating a new position.

        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :param is_long: A boolean indicating if the position is long (True) or short (False)
        :param contract_size: The size of the contract
        :param expected_rate: The expected rate for the position
        :param slip_page: The slippage percentage
        :return: An OpeningClosingFee object containing the swap fee, trading fee, and total fee for opening the position
        """
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
        """
        Calculates the closing fee for terminating an existing position.

        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :param contract_size: The size of the contract being closed
        :return: An OpeningClosingFee object containing the swap fee, trading fee, and total fee for closing the position
        """
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
        """
        Calculates the required collateral for opening a position with specified leverage.

        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :param is_long: A boolean indicating if the position is long (True) or short (False)
        :param contract_size: The size of the contract
        :param leverage: The leverage being used for the position
        :param expected_rate: The expected rate for the position
        :param slip_page: The slippage percentage
        :return: The required collateral amount
        """

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
        """
        Calculates the average entry price for a position after considering the expected rate and slippage.

        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :param is_long: A boolean indicating if the position is long (True) or short (False)
        :param contract_size: The size of the contract
        :param expected_rate: The expected rate for the position
        :param slip_page: The slippage percentage
        :return: The average entry price
        """

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
        """
        Calculates the profit or loss (PNL) after closing a position.

        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :param contract_size: The size of the contract being closed
        :return: An UnrealizedPNL object containing the PNL and ROE after closing the position
        """
        pair:Pair = self.pairs_by_byte(pair_byte)
        underlying_token:IERC20Metadata = IERC20Metadata(pair.pair1, self.web3)
        contract_size = parseEther(self.web3, contract_size, underlying_token.decimals().call())
        return UnrealizedPNL(*self.helper_future_trade.getPNLAfterClosePosition(nft_id, pair_byte, contract_size).call())
    
    def get_margin_after_close_position(self, nft_id:int, pair_byte:str, contract_size:int)->int:
        """
        Calculates the remaining margin after closing a position.

        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :param contract_size: The size of the contract being closed
        :return: The remaining margin after closing the position
        """
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
        """
        Calculates the account balance after opening a new position.

        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :param is_long: A boolean indicating if the position is long (True) or short (False)
        :param contract_size: The size of the contract
        :param expected_rate: The expected rate for the position
        :param slip_page: The slippage percentage
        :return: The account balance after opening the position
        """

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
        """
        Calculates the liquidation price for a position immediately after it is opened.

        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :param is_long: A boolean indicating if the position is long (True) or short (False)
        :param contract_size: The size of the contract
        :param expected_rate: The expected rate for the position
        :param slip_page: The slippage percentage
        :return: The liquidation price immediately after opening the position
        """
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
        """
        Calculates the margin requirement after opening a new position.

        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :param is_long: A boolean indicating if the position is long (True) or short (False)
        :param contract_size: The size of the contract
        :param expected_rate: The expected rate for the position
        :param slip_page: The slippage percentage
        :return: The margin requirement after the position has been opened
        """
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
        """
        Calculates the maximum contract size that can be opened based on the available margin and leverage.

        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :param is_long: A boolean indicating if the position is long (True) or short (False)
        :param leverage: The leverage being used for the position
        :param expected_rate: The expected rate for the position
        :param slip_page: The slippage percentage
        :return: The maximum contract size that can be opened
        """
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
        """
        Retrieves the states of positions for a given NFT ID, along with pagination information.

        :param nft_id: The NFT ID associated with the positions
        :param cursor: The cursor position for pagination
        :param result_per_page: The number of results per page
        :return: A GetPositionStates object containing a list of position states and the next cursor position
        """
        pos_state = self.helper_future_trade.getPositionStates(nftId=nft_id, cursor=cursor, resultsPerPage=result_per_page).call()
        result = GetPositionStates(
            position_states= [PositionState(*i) for i in pos_state[0]],
            next_cursor=pos_state[1]
        )
        return result

    def get_all_active_positions(self, nft_id:int)->List[PositionData]:
        """
        Retrieves all active positions for a given NFT ID.

        :param nft_id: The NFT ID associated with the positions
        :return: A list of PositionData objects representing all active positions
        """
        return [PositionData(*i) for i in (self.helper_future_trade.getAllActivePositions(nftId=nft_id).call())]

    
    
    


    





