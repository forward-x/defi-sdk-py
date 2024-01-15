from ..abi.IAPHCore import *
from ..abi.IERC20Metadata import IERC20Metadata
from ..utils import parseEther, TransactionReceipt
from typing import Union

class Core:
    """
    Core class provides the functionality to interact with the core of FWX-Protocol smart contracts.
    """
    def __init__(self):
        """
        Initializes the Core class by setting up the core contract interface.
        """
        super(Core, self).__init__()
        self.core:IAPHCore = IAPHCore(self.address_const.get_core_address(), self.web3)

    def __str__(self)->str:
        """
        Returns the string representation of the core contract's address.

        :return: Core contract address as a string
        """
        return self.core.address

    def adjust_collateral_event_tx(self, tx_hash:str)->AdjustCollateralEvent:
        """
        Retrieves the AdjustCollateralEvent by transaction hash.

        :param tx_hash: The hash of the transaction to query
        :return: An instance of AdjustCollateralEvent
        """
        return self.core.event_adjustcollateral_by_tx(tx_hash)
        
    def adjust_collateral_event_block(self, from_block:int=0, to_block:int=0)->List[AdjustCollateralEvent]:
        """
        Retrieves a list of AdjustCollateralEvent within a block range.
        
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of AdjustCollateralEvent instances
        """
        return [AdjustCollateralEvent(i) for i in self.core.event_adjustcollateral_by_block(from_block, to_block)]

    def open_position_event_tx(self, tx_hash:str)->OpenPositionEvent:
        """
        Retrieves the OpenPositionEvent by transaction hash.
        
        :param tx_hash: The hash of the transaction to query
        :return: An instance of OpenPositionEvent
        """
        return self.core.event_openposition_by_tx(tx_hash)
        
    def open_position_event_block(self, from_block:int=0, to_block:int=0)->List[OpenPositionEvent]:
        """
        Retrieves a list of OpenPositionEvent within a block range.
        
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of OpenPositionEvent instances
        """
        return [OpenPositionEvent(i) for i in self.core.event_openposition_by_block(from_block, to_block)]

    def close_position_event_tx(self, tx_hash:str)->ClosePositionEvent:
        """
        Retrieves the ClosePositionEvent by transaction hash.
        
        :param tx_hash: The hash of the transaction to query
        :return: An instance of ClosePositionEvent
        """
        return self.core.event_closeposition_by_tx(tx_hash)
        
    def close_position_event_block(self, from_block:int=0, to_block:int=0)->List[ClosePositionEvent]:
        """
        Retrieves a list of ClosePositionEvent within a block range.
        
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of ClosePositionEvent instances
        """
        return [ClosePositionEvent(i) for i in self.core.event_closeposition_by_block(from_block, to_block)]

    def deposit_collateral_event_tx(self, tx_hash:str)->DepositCollateralEvent:
        """
        Retrieves the DepositCollateralEvent by transaction hash.
        
        :param tx_hash: The hash of the transaction to query
        :return: An instance of DepositCollateralEvent
        """
        return self.core.depositcollateral_by_tx(tx_hash)
        
    def deposit_collateral_event_block(self, from_block:int=0, to_block:int=0)->List[DepositCollateralEvent]:
        """
        Retrieves a list of DepositCollateralEvent within a block range.
        
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of DepositCollateralEvent instances
        """
        return [DepositCollateralEvent(i) for i in self.core.depositcollateral_by_block(from_block, to_block)]

    def liquidate_loan_event_tx(self, tx_hash:str)->LiquidateLoanEvent:
        """
        Retrieves the LiquidateLoanEvent by transaction hash.
        
        :param tx_hash: The hash of the transaction to query
        :return: An instance of LiquidateLoanEvent
        """
        return self.core.liquidateloan_by_tx(tx_hash)
        
    def liquidate_loan_event_block(self, from_block:int=0, to_block:int=0)->List[LiquidateLoanEvent]:
        """
        Retrieves a list of LiquidateLoanEvent within a block range.
        
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of LiquidateLoanEvent instances
        """
        return [LiquidateLoanEvent(i) for i in self.core.liquidateloan_by_block(from_block, to_block)]

    def liquidate_position_event_tx(self, tx_hash:str)->LiquidatePositionEvent:
        """
        Retrieves the LiquidatePositionEvent by transaction hash.
        
        :param tx_hash: The hash of the transaction to query
        :return: An instance of LiquidatePositionEvent
        """
        return self.core.liquidateposition_by_tx(tx_hash)
        
    def liquidate_position_event_block(self, from_block:int=0, to_block:int=0)->List[LiquidatePositionEvent]:
        """
        Retrieves a list of LiquidatePositionEvent within a block range.
        
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of LiquidatePositionEvent instances
        """
        return [LiquidatePositionEvent(i) for i in self.core.liquidateposition_by_block(from_block, to_block)]

    def repay_event_tx(self, tx_hash:str)->RepayEvent:
        """
        Retrieves the RepayEvent by transaction hash.
        
        :param tx_hash: The hash of the transaction to query
        :return: An instance of RepayEvent
        """
        return self.core.event_repay_by_tx(tx_hash)
        
    def repay_event_block(self, from_block:int=0, to_block:int=0)->List[RepayEvent]:
        """
        Retrieves a list of RepayEvent within a block range.
        
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of RepayEvent instances
        """
        return [RepayEvent(i) for i in self.core.event_repay_by_block(from_block, to_block)]

    def rollover_event_tx(self, tx_hash:str)->RolloverEvent:
        """
        Retrieves the RolloverEvent by transaction hash.
        
        :param tx_hash: The hash of the transaction to query
        :return: An instance of RolloverEvent
        """
        return self.core.event_rollover_by_tx(tx_hash)
        
    def rollover_event_block(self, from_block:int=0, to_block:int=0)->List[RolloverEvent]:
        """
        Retrieves a list of RolloverEvent within a block range.
        
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of RolloverEvent instances
        """
        return [RolloverEvent(i) for i in self.core.event_rollover_by_block(from_block, to_block)]

    def update_wallet_event_tx(self, tx_hash:str)->UpdateWalletEvent:
        """
        Retrieves the UpdateWalletEvent by transaction hash.
        
        :param tx_hash: The hash of the transaction to query
        :return: An instance of UpdateWalletEvent
        """
        return self.core.event_updatewallet_by_tx(tx_hash)
        
    def update_wallet_event_block(self, from_block:int=0, to_block:int=0)->List[UpdateWalletEvent]:
        """
        Retrieves a list of UpdateWalletEvent within a block range.
        
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of UpdateWalletEvent instances
        """
        return [UpdateWalletEvent(i) for i in self.core.event_updatewallet_by_block(from_block, to_block)]

    def update_loan_event_tx(self, tx_hash:str)->UpdateLoanEvent:
        """
        Retrieves the UpdateLoanEvent by transaction hash.
        
        :param tx_hash: The hash of the transaction to query
        :return: An instance of UpdateLoanEvent
        """
        return self.core.event_updateloan_by_tx(tx_hash)
        
    def update_loan_event_block(self, from_block:int=0, to_block:int=0)->List[UpdateLoanEvent]:
        """
        Retrieves a list of UpdateLoanEvent within a block range.
        
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of UpdateLoanEvent instances
        """
        return [UpdateLoanEvent(i) for i in self.core.event_updateloan_by_block(from_block, to_block)]

    def withdraw_collateral_event_tx(self, tx_hash:str)->WithdrawCollateralEvent:
        """
        Retrieves the WithdrawCollateralEvent by transaction hash.
        
        :param tx_hash: The hash of the transaction to query
        :return: An instance of WithdrawCollateralEvent
        """
        return self.core.event_withdrawcollateral_by_tx(tx_hash)
        
    def withdraw_collateral_event_block(self, from_block:int=0, to_block:int=0)->List[WithdrawCollateralEvent]:
        """
        Retrieves a list of WithdrawCollateralEvent within a block range.
        
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of WithdrawCollateralEvent instances
        """
        return [WithdrawCollateralEvent(i) for i in self.core.event_withdrawcollateral_by_block(from_block, to_block)]

    def check_staking_amount_sufficient(self, nft_id: int, new_amount: int, token: IERC20Metadata)->int:
        """
        Checks if the staking amount is sufficient for a given NFT ID and new amount.
        
        :param nft_id: The NFT ID to check
        :param new_amount: The new amount to check sufficiency against
        :param token: The token for which to check the staking amount
        :return: The result of the sufficiency check
        """
        tokenAddress = token.__str__()
        new_amount = parseEther(self.web3, new_amount, token.decimals().call())
        return self.core.checkStakingAmountSufficient(nft_id, new_amount, tokenAddress).call()

    def wallets(self, nft_id:int, pair_byte:str):
        """
        Retrieves the wallet information for a given NFT ID and pair byte.
        
        :param nft_id: The NFT ID associated with the wallet
        :param pair_byte: The pair byte representing the token pair
        :return: The wallet information
        """
        return self.core.wallets(nft_id, pair_byte).call()

    def trading_collateral_whitelist(self, collateral_token_address: Union[IERC20Metadata, str])->bool:
        """
        Checks if a collateral token address is whitelisted for trading.
        
        :param collateral_token_address: The address of the collateral token to check
        :return: True if the token is whitelisted, False otherwise
        """
        collateral_token_address = collateral_token_address.__str__()
        return self.core.tradingCollateralWhitelist(collateral_token_address).call()

    def positions(self, nft_id:int, pair_byte: str)->Position:
        """
        Retrieves the position information for a given NFT ID and pair byte.
        
        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The pair byte representing the token pair
        :return: The position information as a Position object
        """
        return Position(*self.core.positions(nft_id, pair_byte).call())

    def positions_states(self, nft_id:int, pos_id: int)->PositionState:
        """
        Retrieves the position state for a given NFT ID and position ID.
        
        :param nft_id: The NFT ID associated with the position
        :param pos_id: The position ID
        :return: The state of the position as a PositionState object
        """
        return PositionState(*self.core.positionStates(nft_id, pos_id).call())

    def loans(self, nft_id:int, loan_id: int)->Loan:
        """
        Retrieves the loan information for a given NFT ID and loan ID.
        
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :return: The loan information as a Loan object
        """
        return Loan(*self.core.loans(nft_id, loan_id).call())

    def loanExts(self, nft_id:int, loan_id: int)->LoanExt:
        """
        Retrieves exists loan information for a given NFT ID and loan ID.
        
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :return: The extended loan information as a LoanExt object
        """
        return LoanExt(*self.core.loanExts(nft_id, loan_id).call())

    def current_loan_index(self, nft_id:int)->int:
        """
        Retrieves the current loan index for a given NFT ID.
        
        :param nft_id: The NFT ID to retrieve the loan index for
        :return: The current loan index
        """
        return self.core.currentLoanIndex(nft_id).call()

    def current_position_index(self, nft_id:int)->int:
        """
        Retrieves the current position index for a given NFT ID.
        
        :param nft_id: The NFT ID to retrieve the position index for
        :return: The current position index
        """
        return self.core.currentPositionIndex(nft_id).call()
        
    def pairs(self, collateral_token:IERC20Metadata, underlying_token:IERC20Metadata)->Pair:
        """
        Retrieves the pair information for given collateral and underlying tokens. (ChainClient built-in TOKEN.<TOKEN_SYMBOL>)
        
        :param collateral_token: The collateral token's metadata
        :param underlying_token: The underlying token's metadata
        :return: The pair information as a Pair object
        """
        return Pair(self.core.pairs(collateral_token.__str__(), underlying_token.__str__()).call())

    # ACTION
    def deposit_collateral(self, nft_id: int, collateral_token_address: IERC20Metadata, underlying_token_address: IERC20Metadata, amount: int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Deposits collateral into a position.
        
        :param nft_id: The NFT ID associated with the position
        :param collateral_token_address: The address of the collateral token
        :param underlying_token_address: The address of the underlying token
        :param amount: The amount of collateral to deposit
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        amount = parseEther(self.web3, amount, collateral_token_address.decimals().call())
        collateral_token_address = collateral_token_address.__str__()
        underlying_token_address = underlying_token_address.__str__()
        contract_func = self.core.depositCollateral(nft_id, collateral_token_address, underlying_token_address, amount)
        is_native = self.native.address == collateral_token_address
        return self.send_transaction(contract_func, value=amount if is_native else 0, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def withdraw_collateral(self, nft_id: int, collateral_token_address: IERC20Metadata, underlying_token_address: IERC20Metadata, amount: int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Withdraws collateral from a position.
        
        :param nft_id: The NFT ID associated with the position
        :param collateral_token_address: The address of the collateral token
        :param underlying_token_address: The address of the underlying token
        :param amount: The amount of collateral to withdraw
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        amount = parseEther(self.web3, amount, collateral_token_address.decimals().call())
        collateral_token_address = collateral_token_address.__str__()
        underlying_token_address = underlying_token_address.__str__()
        contract_func = self.core.withdrawCollateral(nft_id, collateral_token_address, underlying_token_address, amount)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)
     
    def adjust_collateral(self, nft_id:int, loan_id:int, collateral_adjust_amount:int, is_add:bool, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Adjusts the collateral for a loan.
        
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :param collateral_adjust_amount: The amount by which to adjust the collateral
        :param is_add: True to add collateral, False to remove
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """

        loan = self.loans(nft_id, loan_id)
        collateral_token:IERC20Metadata = IERC20Metadata(loan.collateralTokenAddress, self.web3)
        is_native = self.native.address == loan.collateralTokenAddress
        amount = parseEther(self.web3, collateral_adjust_amount, collateral_token.decimals().call())
        contract_func = self.core.adjustCollateral(loan_id, nft_id, amount, is_add)
        return self.send_transaction(contract_func, value=amount if is_native else 0, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)
    
    def rollver(self, nft_id:int, loan_id:int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Rolls over a loan to a new period.
        
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        contract_func = self.core.rollover(loan_id, nft_id)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def repay(self, nft_id:int, loan_id:int, repay_amount:int, is_only_interest:bool, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Repays a loan or its interest.
        
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :param repay_amount: The amount to repay
        :param is_only_interest: True to repay only interest, False to repay principal and interest
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        loan = self.loans(nft_id, loan_id)
        borrow_token:IERC20Metadata = IERC20Metadata(loan.borrowTokenAddress, self.web3)
        is_native = self.native.address == loan.borrowTokenAddress
        repay_amount = parseEther(self.web3, repay_amount, borrow_token.decimals().call())
        contract_func = self.core.repay(loan_id, nft_id, repay_amount, is_only_interest)
        return self.send_transaction(contract_func, value=repay_amount if is_native else 0, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)
    
    def close_position(self, nft_id:int, pos_id:int, closing_size:int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Closes an open trading position.
        
        :param nft_id: The NFT ID associated with the position
        :param pos_id: The position ID
        :param closing_size: The size of the position to close
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        pos_state = self.positions_states(nft_id, pos_id)
        if pos_state.active:
            pair = Pair(*self.core.pairs(pos_state.pairByte).call())
            underlying_token:IERC20Metadata = IERC20Metadata(pair.pair1, self.web3)
            closing_size = parseEther(self.web3, closing_size, underlying_token.decimals().call())
            contract_func = self.core.closePosition(nft_id, pos_id, closing_size)
            return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)
        else:
            raise Exception("position-not-active")

    def liquidate(self, nft_id:int ,loan_id:int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Liquidates a loan that is undercollateralized or in default.
        
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        contract_func = self.core.liquidate(loan_id, nft_id)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def liquidate_position(self, nft_id:int ,pair_byte:str, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Liquidates an open trading position that is undercollateralized or in default.
        
        :param nft_id: The NFT ID associated with the position
        :param pair_byte: The byte representation of the pair associated with the position
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        contract_func = self.core.liquidatePosition(nft_id, pair_byte)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

