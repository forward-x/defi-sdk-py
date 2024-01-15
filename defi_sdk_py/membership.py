from web3 import Web3, types
from .abi.IMembership import *
from .abi.IERC20Metadata import IERC20Metadata
from .abi.IAPHPool import IAPHPool
from .utils import parseEther, TransactionReceipt
from .address_const import AddressConst
from typing import Union, List

class Membership:

    def __init__(self):
        super(Membership, self).__init__()
        self.membership:IMembership = IMembership(self.address_const.get_membership_address(), self.web3)

    def current_pool(self)->str:
        return self.membership.currentPool().call()

    def get_default_membership(self, address:str)->int:
        return self.membership.getDefaultMembership(address).call()
    
    def get_pool_lists(self)->List[str]:
        return self.membership.getPoolLists().call()
    
    def get_previous_pool(self)->str:
        return self.membership.getPreviousPool().call()
    
    def get_rank(self, nft_id:int)->int:
        return self.membership.getRank(pool=self.current_pool(), tokenId=nft_id).call()

    def get_rank_pool(self, pool:IAPHPool, nft_id:int)->int:
        return self.membership.getRank(pool.__str__(), nft_id).call()

    def get_refferrer(self, nft_id:int)->int:
        return self.membership.getReferrer(nft_id).call()

    def mint(self, referal_id:int=0,is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        contract_func = self.membership.mint(referal_id)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def set_default_membership(self, nft_id:int,is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        contract_func = self.membership.setDefaultMembership(nft_id)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)
    
    def owner_of(self, nft_id:int)->str:
        return self.membership.ownerOf(nft_id).call()
    