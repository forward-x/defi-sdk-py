from ..abi.IHelperCore import *
from ..abi.IHelperPool import IHelperPool
from ..abi.IStakePool import RankInfo
from ..abi.IAPHPool import IAPHPool
from ..abi.IERC20Metadata import IERC20Metadata
from ..utils import parseEther,Day
from typing import List

class ClaimableInterest:

    def __init__(self, tokenInterest:int, forwInterest:int) -> None:
        self.tokenInterest = tokenInterest
        self.forwInterest = forwInterest

    def __str__(self):
        return str({
            "tokenInterest" : self.tokenInterest,
            "forwInterest" : self.forwInterest
        })

class BorrowingInterest:

    def __init__(self, ltv:int, interest:int) -> None:
        self.ltv = ltv
        self.interest = interest

    def __str__(self):
        return str({
            "ltv" : self.ltv,
            "interest" : self.interest
        })

class PoolInfo:
    def __init__(
        self,
        borrowing_interest: int,
        lending_token_interest: int,
        lending_forw_interest: int,
        utilization_rate: int,
        p_token_total_supply: int,
        current_supply: int
    ) -> None:
        self.borrowing_interest = borrowing_interest
        self.lending_token_interest = lending_token_interest
        self.lending_forw_interest = lending_forw_interest
        self.utilization_rate = utilization_rate
        self.p_token_total_supply = p_token_total_supply
        self.current_supply = current_supply

    def __str__(self):
        return str({
            "borrowing_interest": self.borrowing_interest,
            "lending_token_interest": self.lending_token_interest,
            "lending_forw_interest": self.lending_forw_interest,
            "utilization_rate": self.utilization_rate,
            "p_token_total_supply": self.p_token_total_supply,
            "current_supply": self.current_supply
        })

class LendingInfo:
    def __init__(
        self,
        lending_balance: int,
        interest_token_gained: int,
        interest_forw_gained: int,
        rank: int,
        rank_info: RankInfo
    ) -> None:
        self.lending_balance = lending_balance
        self.interest_token_gained = interest_token_gained
        self.interest_forw_gained = interest_forw_gained
        self.rank = rank
        self.rank_info = rank_info

    def __str__(self):
        return str({
            "lending_balance": self.lending_balance,
            "interest_token_gained": self.interest_token_gained,
            "interest_forw_gained": self.interest_forw_gained,
            "rank": self.rank,
            "rank_info": self.rank_info.__str__()  # Convert the nested RankInfo to string
        })

class HelperPool:

    def __init__(self):
        super(HelperPool, self).__init__()
        self.helper_pool:IHelperPool = IHelperPool(self.address_const.get_helper_pool_address(), self.web3)

    def claimble_interest(self, pool:IAPHPool, nft_id:int)->ClaimableInterest:
        result = self.helper_pool.claimableInterest(pool.address, nft_id).call()
        return ClaimableInterest(result[0], result[1])

    def claimble_interest_membership(self, pool:IAPHPool, nft_id:int)->ClaimableInterest:
        result = self.helper_pool.claimableInterestMembership(pool.address, nft_id).call()
        return ClaimableInterest(result[0], result[1])

    def get_next_lending_forw_interest(self, pool:IAPHPool, new_deposit_amount:int, forw_price_rate:int)->int:
        pool_token = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        forw_token = IERC20Metadata(pool.forwAddress().call(), self.web3)
        new_deposit_amount = parseEther(self.web3, new_deposit_amount, pool_token.decimals().call())
        forw_price_rate = parseEther(self.web3, forw_price_rate, forw_token.decimals().call())
        forw_precision = parseEther(self.web3, 1, forw_token.decimals().call())
        return self.helper_pool.getNextLendingForwInterest(pool.address, new_deposit_amount, forw_price_rate, forw_precision).call()

    def get_next_lending_interest(self, pool:IAPHPool, new_deposit_amount:int)->int:
        pool_token = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        new_deposit_amount = parseEther(self.web3, new_deposit_amount, pool_token.decimals().call())
        return self.helper_pool.getNextLendingInterest(pool.address, new_deposit_amount).call()

    def get_interest_amount_by_deposit_amount(self, pool:IAPHPool, deposit_amount:int, day_second:int=Day())->int:
        pool_token = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        deposit_amount = parseEther(self.web3, deposit_amount, pool_token.decimals().call())
        return self.helper_pool.getInterestAmountByDepositAmount(pool.address, deposit_amount, day_second).call()
    
    def get_deposit_amount_by_interest_amount(self, pool:IAPHPool, interest_amount:int, day_second:int=Day())->int:
        pool_token = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        interest_amount = parseEther(self.web3, interest_amount, pool_token.decimals().call())
        return self.helper_pool.getDepositAmountByInterestAmount(pool.address, interest_amount, day_second).call()
    
    def calculate_borrowing_interest(
        self,
        pool:IAPHPool,
        borrow_amount:int,
        collateral_amount:int,
        collateral_token:IERC20Metadata,
        day_second:int=Day())->BorrowingInterest:

        borrow_token = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        borrow_amount = parseEther(self.web3, borrow_amount, borrow_token.decimals().call())
        collateral_amount = parseEther(self.web3, collateral_amount, collateral_token.decimals().call())
        
        result = self.helper_pool.calculateBorrowingInterest(
            pool.address,
            day_second,
            borrow_amount,
            collateral_amount,
            collateral_token.address
        ).call()
        return BorrowingInterest(*result)
    
    def get_pool_info(self, pool:IAPHPool, forw_price_rate:int)->PoolInfo:
        forw_token = IERC20Metadata(pool.forwAddress().call(), self.web3)
        forw_price_rate = parseEther(self.web3, forw_price_rate, forw_token.decimals().call())
        forw_precision = parseEther(self.web3, 1, forw_token.decimals().call())
        result = self.helper_pool.getPoolInfo(pool.address, forw_price_rate, forw_precision).call()
        return PoolInfo(*result)

    def get_lending_info(self, pool:IAPHPool, nft_id:int)->LendingInfo:
        result = self.helper_pool.getLendingInfo(pool.address, nft_id).call()
        return LendingInfo(*result[:4], rank_info=RankInfo(*result[4]))
    
    

