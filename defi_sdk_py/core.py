from web3 import Web3
from .abi.IAPHCore import IAPHCore
from .abi.IERC20Metadata import IERC20Metadata
from .utils import parseEther
from .address import AddressConst
class Core:
    def __init__(self, address_const:AddressConst, web3:Web3):
        self.core:IAPHCore = IAPHCore(address_const.get_core_address(), web3)
        self.web3 = web3

    def __str__(self)->str:
        return self.core.address

    # GETTER

    def check_staking_amount_sufficient(self, nftId: int, newAmount: int, token: IERC20Metadata)->int:
        tokenAddress = token.__str__()
        newAmount = parseEther(self.web3, newAmount, token.decimals())
        return self.core.checkStakingAmountSufficient(nftId, newAmount, tokenAddress)
