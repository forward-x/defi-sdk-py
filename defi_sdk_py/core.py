from web3 import Web3, types
from .abi.IAPHCore import *
from .abi.IERC20Metadata import IERC20Metadata
from .utils import parseEther
from .address import AddressConst
from typing import Union

class Core:
    def __init__(self):
        super(Core, self).__init__()
        self.core:IAPHCore = IAPHCore(self.address_const.get_core_address(), self.web3)

    def __str__(self)->str:
        return self.core.address

    # GETTER
    def check_staking_amount_sufficient(self, nft_id: int, new_amount: int, token: IERC20Metadata)->int:
        tokenAddress = token.__str__()
        new_amount = parseEther(self.web3, new_amount, token.decimals())
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

    # ACTION
    def deposit_collateral(self, nft_id: int, collateral_token_address: IERC20Metadata, underlying_token_address: IERC20Metadata, amount: int)->types.TxReceipt:
        amount = parseEther(self.web3, amount, collateral_token_address.decimals().call())
        collateral_token_address = collateral_token_address.__str__()
        underlying_token_address = underlying_token_address.__str__()
        contract_func = self.core.depositCollateral(nft_id, collateral_token_address, underlying_token_address, amount)
        return self.send_transaction(contract_func)

    def withdraw_collateral(self, nft_id: int, collateral_token_address: IERC20Metadata, underlying_token_address: IERC20Metadata, amount: int)->types.TxReceipt:
        amount = parseEther(self.web3, amount, collateral_token_address.decimals().call())
        collateral_token_address = collateral_token_address.__str__()
        underlying_token_address = underlying_token_address.__str__()
        contract_func = self.core.withdrawCollateral(nft_id, collateral_token_address, underlying_token_address, amount)
        return self.send_transaction(contract_func)
     
    def adjust_collateral(self, nft_id:int, loan_id:int, collateral_adjust_amount:int, is_add:bool):
        loan = self.loans(nft_id, loan_id)
        collateral_token:IERC20Metadata = IERC20Metadata(loan.collateralTokenAddress, self.web3)
        is_native = self.native.address == loan.collateralTokenAddress
        amount = parseEther(self.web3, collateral_adjust_amount, collateral_token.decimals().call())
        contract_func = self.core.adjustCollateral(loan_id, nft_id, amount, is_add)
        return self.send_transaction(contract_func, amount) if is_native else self.send_transaction(contract_func)
    
    def rollver(self, nft_id:int, loan_id:int):
        contract_func = self.core.rollover(loan_id, nft_id)
        return self.send_transaction(contract_func)
        


