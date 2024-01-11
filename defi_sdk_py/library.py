from web3 import Web3
from .abi.APHLibrary import APHLibrary
from .abi.IERC20Metadata import IERC20Metadata
from .address import AddressConst
class Library:
    def __init__(self, address_const:AddressConst, web3:Web3):
        self.library:APHLibrary = APHLibrary(address_const.get_library_address(), web3)
        self.web3 = web3

    def __str__(self)->str:
        return self.library.address
    
    def hashPair(self, collateral_token_address:IERC20Metadata, underlytinc_token_address:IERC20Metadata)->str:
        collateral_token_address = collateral_token_address.__str__()
        underlytinc_token_address = underlytinc_token_address.__str__()
        return "0x"+self.library.hashPair(collateral_token_address, underlytinc_token_address).hex()