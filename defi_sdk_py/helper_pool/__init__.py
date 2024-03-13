from ..abi.IHelperCore import *
from ..abi.IHelperPool import IHelperPool
from ..abi.IStakePool import RankInfo
from ..abi.IAPHPool import IAPHPool
from ..abi.IERC20Metadata import IERC20Metadata
from ..utils import parseEther,Day
from typing import List

class ClaimableInterest:
    """
    Represents the claimable interest for a stake in a pool.

    :param tokenInterest: The claimable token interest amount
    :param forwInterest: The claimable forward interest amount
    """

    def __init__(self, tokenInterest:int, forwInterest:int) -> None:
        self.tokenInterest = tokenInterest
        self.forwInterest = forwInterest

    def __str__(self):
        return str({
            "tokenInterest" : self.tokenInterest,
            "forwInterest" : self.forwInterest
        })

class BorrowingInterest:
    """
    Represents the borrowing interest details for a loan.

    :param ltv: The loan-to-value ratio
    :param interest: The interest amount
    """

    def __init__(self, ltv:int, interest:int) -> None:
        self.ltv = ltv
        self.interest = interest

    def __str__(self):
        return str({
            "ltv" : self.ltv,
            "interest" : self.interest
        })

class PoolInfo:
    """
    Represents the information about a pool.

    :param borrowing_interest: The interest rate for borrowing
    :param lending_token_interest: The interest rate for token lending
    :param lending_forw_interest: The interest rate for forward lending
    :param utilization_rate: The utilization rate of the pool
    :param p_token_total_supply: The total supply of the pool's P tokens
    :param current_supply: The current supply of the pool
    """
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
    """
    Represents the lending information for a stake in a pool.

    :param lending_balance: The lending balance
    :param interest_token_gained: The interest gained in tokens
    :param interest_forw_gained: The interest gained in forwards
    :param rank: The rank of the lender
    :param rank_info: The rank information
    """
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
    """
    HelperPool provides utility functions to assist with pool-related calculations.
    """

    def __init__(self):
        """
        Initializes the HelperPool by setting up the helper pool contract interface.
        """
        super(HelperPool, self).__init__()
        self.helper_pool:IHelperPool = IHelperPool(self.address_const.get_helper_pool_address(), self.web3)

    def claimble_interest(self, pool:IAPHPool, nft_id:int)->ClaimableInterest:
        """
        Retrieves the claimable interest for a given NFT ID in a pool.

        :param pool: The pool contract interface
        :param nft_id: The NFT ID to query for claimable interest
        :return: A ClaimableInterest object containing the token and forward interest amounts
        """
        result = self.helper_pool.claimableInterest(pool.address, nft_id).call()
        return ClaimableInterest(result[0], result[1])

    def claimble_interest_membership(self, pool:IAPHPool, nft_id:int)->ClaimableInterest:
        """
        Retrieves the claimable interest for a given NFT ID in a pool, accounting for membership.

        :param pool: The pool contract interface
        :param nft_id: The NFT ID to query for claimable interest with membership considered
        :return: A ClaimableInterest object containing the token and forward interest amounts
        """

        result = self.helper_pool.claimableInterestMembership(pool.address, nft_id).call()
        return ClaimableInterest(result[0], result[1])

    def get_next_lending_forw_interest(self, pool:IAPHPool, new_deposit_amount:int, forw_price_rate:int)->int:
        """
        Calculates the next lending forward interest for a new deposit in a pool.

        :param pool: The pool contract interface
        :param new_deposit_amount: The new deposit amount
        :param forw_price_rate: The price rate of the forward token
        :return: The next lending forward interest amount
        """
        pool_token = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        forw_token = IERC20Metadata(pool.forwAddress().call(), self.web3)
        new_deposit_amount = parseEther(self.web3, new_deposit_amount, pool_token.decimals().call())
        forw_price_rate = parseEther(self.web3, forw_price_rate, forw_token.decimals().call())
        forw_precision = parseEther(self.web3, 1, forw_token.decimals().call())
        return self.helper_pool.getNextLendingForwInterest(pool.address, new_deposit_amount, forw_price_rate, forw_precision).call()

    def get_next_lending_interest(self, pool:IAPHPool, new_deposit_amount:int)->int:
        """
        Calculates the next lending interest for a new deposit in a pool.

        :param pool: The pool contract interface
        :param new_deposit_amount: The new deposit amount
        :return: The next lending interest amount
        """

        pool_token = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        new_deposit_amount = parseEther(self.web3, new_deposit_amount, pool_token.decimals().call())
        return self.helper_pool.getNextLendingInterest(pool.address, new_deposit_amount).call()

    def get_interest_amount_by_deposit_amount(self, pool:IAPHPool, deposit_amount:int, day_second:int=Day())->int:
        """
        Calculates the interest amount based on a deposit amount for a given time period in a pool.

        :param pool: The pool contract interface
        :param deposit_amount: The deposit amount
        :param day_second: The time period in seconds for which the interest is calculated (default is one day)
        :return: The interest amount for the deposit
        """

        pool_token = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        deposit_amount = parseEther(self.web3, deposit_amount, pool_token.decimals().call())
        return self.helper_pool.getInterestAmountByDepositAmount(pool.address, deposit_amount, day_second).call()
    
    def get_deposit_amount_by_interest_amount(self, pool:IAPHPool, interest_amount:int, day_second:int=Day())->int:
        """
        Calculates the deposit amount required to achieve a target interest amount for a given time period in a pool.

        :param pool: The pool contract interface
        :param interest_amount: The target interest amount
        :param day_second: The time period in seconds for which the deposit is calculated (default is one day)
        :return: The deposit amount required for the target interest
        """
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
        """
        Calculates the borrowing interest for a given loan amount and collateral in a pool.

        :param pool: The pool contract interface
        :param borrow_amount: The borrow amount
        :param collateral_amount: The collateral amount
        :param collateral_token: The collateral token metadata
        :param day_second: The time period in seconds for which the interest is calculated (default is one day)
        :return: A BorrowingInterest object containing the LTV and interest
        """
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
        """
        Retrieves information about a pool, including interest rates, utilization rate, and supply details.

        :param pool: The pool contract interface
        :param forw_price_rate: The price rate of the forward token
        :return: A PoolInfo object containing detailed information about the pool
        """
        forw_token = IERC20Metadata(pool.forwAddress().call(), self.web3)
        forw_price_rate = parseEther(self.web3, forw_price_rate, forw_token.decimals().call())
        forw_precision = parseEther(self.web3, 1, forw_token.decimals().call())
        result = self.helper_pool.getPoolInfo(pool.address, forw_price_rate, forw_precision).call()
        return PoolInfo(*result)

    def get_lending_info(self, pool:IAPHPool, nft_id:int)->LendingInfo:
        """
        Retrieves lending information for a given NFT ID in a pool, including balance, interest gained, and rank.

        :param pool: The pool contract interface
        :param nft_id: The NFT ID to query for lending information
        :return: A LendingInfo object containing detailed information about the lending stake
        """
        result = self.helper_pool.getLendingInfo(pool.address, nft_id).call()
        return LendingInfo(*result[:4], rank_info=RankInfo(*result[4]))
    
    

