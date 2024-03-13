from ..abi.IHelperCore import *
from ..abi.IStakePool import IStakePool
from ..abi.IHelperMembershipAndStakePool import IHelperMembershipAndStakePool, RankInfo, StakeInfo
from typing import List
class NFTList:
    """
    Represents a list of NFTs owned by an address along with the count.

    :param count: The total number of NFTs
    :param nft_list: A list of NFT IDs
    """
    def __init__(self, count:int, nft_list:List[int]) -> None:

        self.count = count
        self.nft_list = nft_list

    def __str__(self):

        return str({
            "count" : self.count,
            "nft_list" : [i for i in self.nft_list]
        })

class HelperMembershipAndStakePool:
    """
    HelperMembershipAndStakePool provides utility functions to assist with membership and stake pool operations.
    """

    def __init__(self):
        """
        Initializes the HelperMembershipAndStakePool by setting up the helper membership and stake pool contract interface.
        """
        super(HelperMembershipAndStakePool, self).__init__()
        self.helper_membership_and_stake_pool:IHelperMembershipAndStakePool = IHelperMembershipAndStakePool(self.address_const.get_helper_membership_and_stake_pool_address(), self.web3)

    def get_stake_pool_next_settle_timestamp(self, stake_pool:IStakePool)->int:
        """
        Retrieves the next settlement timestamp for a stake pool.

        :param stake_pool: The stake pool contract interface
        :return: The next settlement timestamp as an integer
        """

        stake_pool = stake_pool.__str__()
        return self.helper_membership_and_stake_pool.getStakePoolNextSettleTimeStamp(stake_pool).call()

    def get_nft_list(self, address:str)->NFTList:
        """
        Retrieves a list of NFT IDs owned by a given address.

        :param address: The address to query for owned NFTs
        :return: An NFTList object containing the count and list of NFT IDs
        """

        data = self.helper_membership_and_stake_pool.getNFTList(address).call()
        return NFTList(data[0], data[1])

    def get_rank_info_list(self)->List[RankInfo]:
        """
        Retrieves a list of rank information for membership.

        :return: A list of RankInfo objects containing rank details
        """

        data = self.helper_membership_and_stake_pool.getRankInfoList().call()
        result:List[RankInfo] = [RankInfo(*i) for i in data]
        return result
    
    def get_stake_info(self, nft_id:int)->StakeInfo:
        """
        Retrieves the stake information for a given NFT ID.

        :param nft_id: The NFT ID to query for stake information
        :return: A StakeInfo object containing the stake details
        """
        return StakeInfo(*(self.helper_membership_and_stake_pool.getStakeInfo(nft_id).call()))


