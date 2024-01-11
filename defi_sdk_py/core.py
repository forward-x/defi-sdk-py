from web3 import Web3, types
from .abi.IAPHCore import IAPHCore
from .abi.IERC20Metadata import IERC20Metadata
from .utils import parseEther
from .address import AddressConst
import json
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
        return self.core.checkStakingAmountSufficient(nft_id, new_amount, tokenAddress)

    def wallets(self, nft_id:int, pair_byte:str):
        return self.core.wallets(nft_id, pair_byte)

    # ACTION
    def depositCollateral(self, nft_id: int, collateral_token_address: IERC20Metadata, underlying_token_address: IERC20Metadata, amount: int)->types.TxReceipt:
        amount = parseEther(self.web3, amount, collateral_token_address.decimals())
        collateral_token_address = collateral_token_address.__str__()
        underlying_token_address = underlying_token_address.__str__()
        contract_func = self.core.depositCollateral(nft_id, collateral_token_address, underlying_token_address, amount)
        return self.send_transaction(contract_func)

    def withdrawCollateral(self, nft_id: int, collateral_token_address: IERC20Metadata, underlying_token_address: IERC20Metadata, amount: int)->types.TxReceipt:
        amount = parseEther(self.web3, amount, collateral_token_address.decimals())
        collateral_token_address = collateral_token_address.__str__()
        underlying_token_address = underlying_token_address.__str__()
        contract_func = self.core.withdrawCollateral(nft_id, collateral_token_address, underlying_token_address, amount)
        return self.send_transaction(contract_func)


