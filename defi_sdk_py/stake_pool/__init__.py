from web3 import Web3, types
from ..abi.IStakePool import *
from ..abi.IERC20Metadata import IERC20Metadata
from ..abi.IAPHPool import IAPHPool
from ..utils import parseEther, TransactionReceipt
from ..address_const import AddressConst
from typing import Union, List

class StakePool:
    """
    StakePool provides functionality to interact with the stake pool smart contracts.
    """
    def __init__(self):
        """
        Initializes the StakePool by setting up the stake pool contract interface.
        """
        super(StakePool, self).__init__()
        self.stakepool:IStakePool = IStakePool(self.address_const.get_stakepool_address(), self.web3)

    def stake(self, nft_id:int, amount:int, is_estimate:bool=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Stakes an amount for a given NFT ID in the stake pool.

        :param nft_id: The NFT ID to stake for
        :param amount: The amount to stake
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """

        amount = parseEther(self.web3, amount, self.TOKEN.FWX.decimals().call())
        contract_func = self.stakepool.stake(nft_id, amount)
        return self.send_transaction(contract_func,is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def unstake(self, nft_id:int, amount:int, is_estimate:bool=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Unstakes an amount for a given NFT ID from the stake pool.

        :param nft_id: The NFT ID to unstake from
        :param amount: The amount to unstake
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        amount = parseEther(self.web3, amount, self.TOKEN.FWX.decimals().call())
        contract_func = self.stakepool.unstake(nft_id, amount)
        return self.send_transaction(contract_func,is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)
    
    def rank_infos(self, rank_number:int)->RankInfo:
        """
        Retrieves the rank information for a given rank number in the stake pool.

        :param rank_number: The rank number to query for information
        :return: A RankInfo object containing the rank details
        """
        return RankInfo(*(self.stakepool.rankInfos(rank_number).call()))

    def rank_len(self)->int:
        """
        Retrieves the total number of ranks available in the stake pool.

        :return: The total number of ranks as an integer
        """
        return self.stakepool.rankLen().call()

    def pool_start_timestamp(self)->int:
        """
        Retrieves the start timestamp of the stake pool.

        :return: The start timestamp of the pool as an integer
        """

        return self.stakepool.poolStartTimestamp().call()

    def settle_interval(self)->int:
        """
        Retrieves the settlement interval for the stake pool.

        :return: The settlement interval as an integer
        """

        return self.stakepool.settleInterval().call()

    def settle_period(self)->int:
        """
        Retrieves the settlement period for the stake pool.

        :return: The settlement period as an integer
        """
        return self.stakepool.settlePeriod().call()
    
    def get_stake_info(self, nft_id:int)->StakeInfo:
        """
        Retrieves the stake information for a given NFT ID in the stake pool.

        :param nft_id: The NFT ID to query for stake information
        :return: A StakeInfo object containing the stake details
        """
        return StakeInfo(*(self.stakepool.getStakeInfo(nft_id).call()))
    
    def get_max_ltv(self, nft_id:int)->int:
        """
        Retrieves the maximum loan-to-value (LTV) bonus for a given NFT ID in the stake pool.

        :param nft_id: The NFT ID to query for the maximum LTV bonus
        :return: The maximum LTV bonus as an integer
        """
        return self.stakepool.getMaxLTVBonus(nft_id).call()