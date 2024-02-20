from web3 import Web3, types
from ..abi.IMembership import *
from ..abi.IERC20Metadata import IERC20Metadata
from ..abi.IAPHPool import IAPHPool
from ..utils import parseEther, TransactionReceipt
from ..address_const import AddressConst
from typing import Union, List

class Membership:
    """
    Membership provides functionality to interact with the membership smart contracts.
    """
    def __init__(self):
        """
        Initializes the Membership by setting up the membership contract interface.
        """
        super(Membership, self).__init__()
        self.membership:IMembership = IMembership(self.address_const.get_membership_address(), self.web3)

    def current_pool(self)->str:
        """
        Retrieves the address of the current pool.

        :return: The address of the current pool as a string
        """
        return self.membership.currentPool().call()

    def get_default_membership(self, address:str)->int:
        """
        Retrieves the default membership level for a given address.

        :param address: The address to query the default membership level
        :return: The default membership level as an integer
        """
        return self.membership.getDefaultMembership(address).call()
    
    def get_pool_lists(self)->List[str]:
        """
        Retrieves a list of pool addresses that are part of the membership program.

        :return: A list of pool addresses as strings
        """
        return self.membership.getPoolLists().call()
    
    def get_previous_pool(self)->str:
        """
        Retrieves the address of the previous pool.

        :return: The address of the previous pool as a string
        """
        return self.membership.getPreviousPool().call()
    
    def get_rank(self, nft_id:int)->int:
        """
        Retrieves the rank associated with a given NFT ID in the current pool.

        :param nft_id: The NFT ID to query the rank
        :return: The rank as an integer
        """
        return self.membership.getRank(pool=self.current_pool(), tokenId=nft_id).call()

    def get_rank_pool(self, pool:IAPHPool, nft_id:int)->int:
        """
        Retrieves the rank associated with a given NFT ID in a specified pool.

        :param pool: The pool contract interface
        :param nft_id: The NFT ID to query the rank
        :return: The rank as an integer
        """
        return self.membership.getRank(pool.__str__(), nft_id).call()

    def get_refferrer(self, nft_id:int)->int:
        """
        Retrieves the referrer associated with a given NFT ID.

        :param nft_id: The NFT ID to query the referrer
        :return: The referrer as an integer
        """
        return self.membership.getReferrer(nft_id).call()

    def mint(self, referal_id:int=0,is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Mints a new membership NFT with an optional referral ID.

        :param referal_id: The referral ID to associate with the minting (default is 0)
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        contract_func = self.membership.mint(referal_id)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def set_default_membership(self, nft_id:int,is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Sets the default membership level for the caller using a given NFT ID.

        :param nft_id: The NFT ID to set as the default membership
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        contract_func = self.membership.setDefaultMembership(nft_id)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)
    
    def owner_of(self, nft_id:int)->str:
        """
        Retrieves the owner address of a specific NFT ID.

        :param nft_id: The NFT ID to query the owner
        :return: The address of the owner as a string
        """
        return self.membership.ownerOf(nft_id).call()
    