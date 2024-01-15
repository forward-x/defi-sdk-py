from web3 import Web3, types
from .abi.IStakePool import *
from .abi.IERC20Metadata import IERC20Metadata
from .abi.IAPHPool import IAPHPool
from .utils import parseEther, TransactionReceipt
from .address import AddressConst
from typing import Union, List

class StakePool:

    def __init__(self):
        super(StakePool, self).__init__()
        self.stakepool:IStakePool = IStakePool(self.address_const.get_stakepool_address(), self.web3)

    def stake(self, nft_id:int, amount:int, is_estimate:bool=False)->Union[TransactionReceipt, int]:
        amount = parseEther(self.web3, amount, self.TOKEN.FWX.decimals().call())
        contract_func = self.stakepool.stake(nft_id, amount)
        return self.send_transaction(contract_func,is_estimate=is_estimate)

    def unstake(self, nft_id:int, amount:int, is_estimate:bool=False)->Union[TransactionReceipt, int]:
        amount = parseEther(self.web3, amount, self.TOKEN.FWX.decimals().call())
        contract_func = self.stakepool.unstake(nft_id, amount)
        return self.send_transaction(contract_func,is_estimate=is_estimate)
    
    def rank_infos(self, rank_number:int)->RankInfo:
        return RankInfo(*(self.stakepool.rankInfos(rank_number).call()))

    def rank_len(self)->int:
        return self.stakepool.rankLen().call()

    def pool_start_timestamp(self)->int:
        return self.stakepool.poolStartTimestamp().call()

    def settle_interval(self)->int:
        return self.stakepool.settleInterval().call()

    def settle_period(self)->int:
        return self.stakepool.settlePeriod().call()
    
    def get_stake_info(self, nft_id:int)->StakeInfo:
        return StakeInfo(*(self.stakepool.getStakeInfo(nft_id).call()))
    
    def get_max_ltv(self, nft_id:int)->int:
        return self.stakepool.getMaxLTVBonus(nft_id).call()



    # def current_pool(self)->str:
    #     return self.membership.currentPool().call()

    # def get_default_membership(self, address:str)->int:
    #     return self.membership.getDefaultMembership(address).call()
    
    # def get_pool_lists(self)->List[str]:
    #     return self.membership.getPoolLists().call()
    
    # def get_previous_pool(self)->str:
    #     return self.membership.getPreviousPool().call()
    
    # def get_rank(self, nft_id:int)->int:
    #     return self.membership.getRank(pool=self.current_pool(), tokenId=nft_id).call()

    # def get_rank_pool(self, pool:IAPHPool, nft_id:int)->int:
    #     return self.membership.getRank(pool.__str__(), nft_id).call()

    # def get_refferrer(self, nft_id:int)->int:
    #     return self.membership.getReferrer(nft_id).call()

    # def mint(self, referal_id:int=0,is_estimate=False)->Union[TransactionReceipt, int]:
    #     contract_func = self.membership.mint(referal_id)
    #     return self.send_transaction(contract_func, is_estimate=is_estimate)

    # def set_default_membership(self, nft_id:int,is_estimate=False)->Union[TransactionReceipt, int]:
    #     contract_func = self.membership.setDefaultMembership(nft_id)
    #     return self.send_transaction(contract_func, is_estimate=is_estimate)
    