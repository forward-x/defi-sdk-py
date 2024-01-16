from ..abi.IHelperCore import *
from ..abi.IStakePool import IStakePool
from ..abi.IHelperMembershipAndStakePool import IHelperMembershipAndStakePool, RankInfo, StakeInfo
from typing import List
class NFTList:

    def __init__(self, count:int, nft_list:List[int]) -> None:

        self.count = count
        self.nft_list = nft_list

    def __str__(self):

        return str({
            "count" : self.count,
            "nft_list" : [i for i in self.nft_list]
        })

class HelperMembershipAndStakePool:

    def __init__(self):
        super(HelperMembershipAndStakePool, self).__init__()
        self.helper_membership_and_stake_pool:IHelperMembershipAndStakePool = IHelperMembershipAndStakePool(self.address_const.get_helper_membership_and_stake_pool_address(), self.web3)

    def get_stake_pool_next_settle_timestamp(self, stake_pool:IStakePool)->int:
        stake_pool = stake_pool.__str__()
        return self.helper_membership_and_stake_pool.getStakePoolNextSettleTimeStamp(stake_pool).call()

    def get_nft_list(self, address:str)->NFTList:
        data = self.helper_membership_and_stake_pool.getNFTList(address).call()
        return NFTList(data[0], data[1])

    def get_rank_info_list(self)->List[RankInfo]:
        data = self.helper_membership_and_stake_pool.getRankInfoList().call()
        result:List[RankInfo] = [RankInfo(*i) for i in data]
        return result
    
    def get_stake_info(self, nft_id:int)->StakeInfo:
        return StakeInfo(*(self.helper_membership_and_stake_pool.getStakeInfo(nft_id).call()))


