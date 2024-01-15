from web3 import Web3, types
from .abi.IAPHCore import *
from .abi.IERC20Metadata import IERC20Metadata
from .utils import parseEther, TransactionReceipt
from .address_const import AddressConst
from typing import Union

class Core:
    def __init__(self):
        super(Core, self).__init__()
        self.core:IAPHCore = IAPHCore(self.address_const.get_core_address(), self.web3)

    def __str__(self)->str:
        return self.core.address

    def adjust_collateral_event_tx(self, tx_hash:str)->AdjustCollateralEvent:
        return self.core.event_adjustcollateral_by_tx(tx_hash)
        
    def adjust_collateral_event_block(self, from_block:int=0, to_block:int=0)->List[AdjustCollateralEvent]:
        return [AdjustCollateralEvent(i) for i in self.core.event_adjustcollateral_by_block(from_block, to_block)]

    def open_position_event_tx(self, tx_hash:str)->OpenPositionEvent:
        return self.core.event_openposition_by_tx(tx_hash)
        
    def open_position_event_block(self, from_block:int=0, to_block:int=0)->List[OpenPositionEvent]:
        return [OpenPositionEvent(i) for i in self.core.event_openposition_by_block(from_block, to_block)]

    def close_position_event_tx(self, tx_hash:str)->ClosePositionEvent:
        return self.core.event_closeposition_by_tx(tx_hash)
        
    def close_position_event_block(self, from_block:int=0, to_block:int=0)->List[ClosePositionEvent]:
        return [ClosePositionEvent(i) for i in self.core.event_closeposition_by_block(from_block, to_block)]

    def deposit_collateral_event_tx(self, tx_hash:str)->DepositCollateralEvent:
        return self.core.depositcollateral_by_tx(tx_hash)
        
    def deposit_collateral_event_block(self, from_block:int=0, to_block:int=0)->List[DepositCollateralEvent]:
        return [DepositCollateralEvent(i) for i in self.core.depositcollateral_by_block(from_block, to_block)]

    def liquidate_loan_event_tx(self, tx_hash:str)->LiquidateLoanEvent:
        return self.core.liquidateloan_by_tx(tx_hash)
        
    def liquidate_loan_event_block(self, from_block:int=0, to_block:int=0)->List[LiquidateLoanEvent]:
        return [LiquidateLoanEvent(i) for i in self.core.liquidateloan_by_block(from_block, to_block)]

    def liquidate_position_event_tx(self, tx_hash:str)->LiquidatePositionEvent:
        return self.core.liquidateposition_by_tx(tx_hash)
        
    def liquidate_position_event_block(self, from_block:int=0, to_block:int=0)->List[LiquidatePositionEvent]:
        return [LiquidatePositionEvent(i) for i in self.core.liquidateposition_by_block(from_block, to_block)]

    def repay_event_tx(self, tx_hash:str)->RepayEvent:
        return self.core.event_repay_by_tx(tx_hash)
        
    def repay_event_block(self, from_block:int=0, to_block:int=0)->List[RepayEvent]:
        return [RepayEvent(i) for i in self.core.event_repay_by_block(from_block, to_block)]

    def rollover_event_tx(self, tx_hash:str)->RolloverEvent:
        return self.core.event_rollover_by_tx(tx_hash)
        
    def rollover_event_block(self, from_block:int=0, to_block:int=0)->List[RolloverEvent]:
        return [RolloverEvent(i) for i in self.core.event_rollover_by_block(from_block, to_block)]

    def update_wallet_event_tx(self, tx_hash:str)->UpdateWalletEvent:
        return self.core.event_updatewallet_by_tx(tx_hash)
        
    def update_wallet_event_block(self, from_block:int=0, to_block:int=0)->List[UpdateWalletEvent]:
        return [UpdateWalletEvent(i) for i in self.core.event_updatewallet_by_block(from_block, to_block)]

    def update_loan_event_tx(self, tx_hash:str)->UpdateLoanEvent:
        return self.core.event_updateloan_by_tx(tx_hash)
        
    def update_loan_event_block(self, from_block:int=0, to_block:int=0)->List[UpdateLoanEvent]:
        return [UpdateLoanEvent(i) for i in self.core.event_updateloan_by_block(from_block, to_block)]

    def withdraw_collateral_event_tx(self, tx_hash:str)->WithdrawCollateralEvent:
        return self.core.event_withdrawcollateral_by_tx(tx_hash)
        
    def withdraw_collateral_event_block(self, from_block:int=0, to_block:int=0)->List[WithdrawCollateralEvent]:
        return [WithdrawCollateralEvent(i) for i in self.core.event_withdrawcollateral_by_block(from_block, to_block)]



    # GETTER
    def check_staking_amount_sufficient(self, nft_id: int, new_amount: int, token: IERC20Metadata)->int:
        tokenAddress = token.__str__()
        new_amount = parseEther(self.web3, new_amount, token.decimals().call())
        return self.core.checkStakingAmountSufficient(nft_id, new_amount, tokenAddress).call()

    def wallets(self, nft_id:int, pair_byte:str):
        return self.core.wallets(nft_id, pair_byte).call()

    def trading_collateral_whitelist(self, collateral_token_address: Union[IERC20Metadata, str])->bool:
        collateral_token_address = collateral_token_address.__str__()
        return self.core.tradingCollateralWhitelist(collateral_token_address).call()

    def positions(self, nft_id:int, pair_byte: str)->Position:
        return Position(*self.core.positions(nft_id, pair_byte).call())

    def positions_states(self, nft_id:int, pos_id: int)->PositionState:
        return PositionState(*self.core.positionStates(nft_id, pos_id).call())

    def loans(self, nft_id:int, loan_id: int)->Loan:
        return Loan(*self.core.loans(nft_id, loan_id).call())

    def loanExts(self, nft_id:int, loan_id: int)->LoanExt:
        return LoanExt(*self.core.loanExts(nft_id, loan_id).call())

    def current_loan_index(self, nft_id:int)->int:
        return self.core.currentLoanIndex(nft_id).call()

    def current_position_index(self, nft_id:int)->int:
        return self.core.currentPositionIndex(nft_id).call()
        
    def pairs(self, collateral_token:IERC20Metadata, underlying_token:IERC20Metadata)->Pair:
        return Pair(self.core.pairs(collateral_token.__str__(), underlying_token.__str__()).call())

    # ACTION
    def deposit_collateral(self, nft_id: int, collateral_token_address: IERC20Metadata, underlying_token_address: IERC20Metadata, amount: int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        amount = parseEther(self.web3, amount, collateral_token_address.decimals().call())
        collateral_token_address = collateral_token_address.__str__()
        underlying_token_address = underlying_token_address.__str__()
        contract_func = self.core.depositCollateral(nft_id, collateral_token_address, underlying_token_address, amount)
        is_native = self.native.address == collateral_token_address
        return self.send_transaction(contract_func, value=amount if is_native else 0, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def withdraw_collateral(self, nft_id: int, collateral_token_address: IERC20Metadata, underlying_token_address: IERC20Metadata, amount: int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        amount = parseEther(self.web3, amount, collateral_token_address.decimals().call())
        collateral_token_address = collateral_token_address.__str__()
        underlying_token_address = underlying_token_address.__str__()
        contract_func = self.core.withdrawCollateral(nft_id, collateral_token_address, underlying_token_address, amount)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)
     
    def adjust_collateral(self, nft_id:int, loan_id:int, collateral_adjust_amount:int, is_add:bool, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        loan = self.loans(nft_id, loan_id)
        collateral_token:IERC20Metadata = IERC20Metadata(loan.collateralTokenAddress, self.web3)
        is_native = self.native.address == loan.collateralTokenAddress
        amount = parseEther(self.web3, collateral_adjust_amount, collateral_token.decimals().call())
        contract_func = self.core.adjustCollateral(loan_id, nft_id, amount, is_add)
        return self.send_transaction(contract_func, value=amount if is_native else 0, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)
    
    def rollver(self, nft_id:int, loan_id:int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        contract_func = self.core.rollover(loan_id, nft_id)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def repay(self, nft_id:int, loan_id:int, repay_amount:int, is_only_interest:bool, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        loan = self.loans(nft_id, loan_id)
        borrow_token:IERC20Metadata = IERC20Metadata(loan.borrowTokenAddress, self.web3)
        is_native = self.native.address == loan.borrowTokenAddress
        repay_amount = parseEther(self.web3, repay_amount, borrow_token.decimals().call())
        contract_func = self.core.repay(loan_id, nft_id, repay_amount, is_only_interest)
        return self.send_transaction(contract_func, value=repay_amount if is_native else 0, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)
    
    def close_position(self, nft_id:int, pos_id:int, closing_size:int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
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
        contract_func = self.core.liquidate(loan_id, nft_id)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def liquidate_position(self, nft_id:int ,pair_byte:str, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        contract_func = self.core.liquidatePosition(nft_id, pair_byte)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

