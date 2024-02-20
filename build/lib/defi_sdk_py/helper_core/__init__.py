from ..abi.IHelperCore import *
from ..abi.IERC20Metadata import IERC20Metadata
from ..abi.IHelperCore import IHelperCore
from ..utils import parseEther
import json

class ActiveLoans:
    """
    Represents a collection of active loans along with their corresponding information.

    :param active_loans: A list of active Loan objects
    :param active_loan_infos: A list of ActiveLoanInfo objects with detailed loan information
    :param interest_owed_per_day: A list of interest owed per day for each loan
    :param new_cursor: The new cursor position for pagination
    """
    def __init__(self, active_loans:list, active_loan_infos:list, interest_owed_per_day:list, new_cursor:int):
        self.active_loans:list(Loan) = active_loans
        self.active_loan_infos:list(ActiveLoanInfo) = active_loan_infos
        self.interest_owed_per_day:list(int) = interest_owed_per_day
        self.new_cursor:int = new_cursor

    def __str__(self):
        output = []
        for i in range(len(self.active_loans)):
            output.append(
                str({
                    'active_loans' : self.active_loans[i].__str__(),
                    'active_loan_infos' : self.active_loan_infos[i].__str__(),
                    'interest_owed_per_day' : self.interest_owed_per_day[i],
                })
            )
        output.append(str({'new_cursor':self.new_cursor}))
        return json.dumps(output, indent=3)

class LoanCollateralInfo:
    """
    Represents the collateral information for a loan.

    :param minimumCollateral: The minimum required collateral for the loan
    :param removableCollateral: The amount of collateral that can be removed without affecting the loan
    """

    def __init__(self, minimumCollateral, removableCollateral) -> None:
        self.minimumCollateral = minimumCollateral
        self.removableCollateral = removableCollateral
    def __str__(self):
        return str({
            "minumum_collateral" : self.minimumCollateral,
            "removable_collateral" : self.removableCollateral
        })

class SettleBorrowInfo:
    """
    Represents the information required to settle a borrow.

    :param settledBorrowAmount: The amount of the borrow that has been settled
    :param settledLTV: The loan-to-value ratio after settlement
    :param rate: The rate used in settlement calculations
    :param precision: The precision of the rate
    """
    def __init__(self, settledBorrowAmount, settledLTV, rate, precision,) -> None:
        self.settledBorrowAmount = settledBorrowAmount
        self.settledLTV = settledLTV
        self.rate = rate
        self.precision = precision
    def __str__(self):
        return str({
            "settledBorrowAmount" : self.settledBorrowAmount,
            "settledLTV" : self.settledLTV,
            "rate" : self.rate,
            "precision" : self.precision
        })
class BorrowAmountInfo:
    """
    Represents the information about the maximum borrowable amount and maximum collateral amount.

    :param maxBorrowAmount: The maximum amount that can be borrowed
    :param maxCollateralAmount: The maximum amount of collateral that can be used
    """
    def __init__(self, maxBorrowAmount, maxCollateralAmount) -> None:
        self.maxBorrowAmount = maxBorrowAmount
        self.maxCollateralAmount = maxCollateralAmount

    def __str__(self):
        return str({
            "maxBorrowAmount" : self.maxBorrowAmount,
            "maxCollateralAmount" : self.maxCollateralAmount
        })

class HelperCore:
    """
    HelperCore provides utility functions to assist with loan and collateral calculations.
    """
    def __init__(self):
        """
        Initializes the HelperCore by setting up the helper core contract interface.
        """
        super(HelperCore, self).__init__()
        self.helper_core:IHelperCore = IHelperCore(self.address_const.get_helper_core_address(), self.web3)

    def get_active_loans(self, nft_id:int, cursor:int=1, result_per_page:int=1)->ActiveLoans:
        """
        Retrieves the active loans for a given NFT ID.
        :param nft_id: The NFT ID to query for active loans
        :param cursor: The cursor position for pagination
        :param result_per_page: The number of results per page
        :return: An ActiveLoans object containing a list of active loans and related information
        """    
        active_list = self.helper_core.getActiveLoans(nftId=nft_id, cursor=cursor, resultsPerPage=result_per_page).call()
        active_loans = []
        active_loan_infos = []
        interest_owed_per_day = []
        new_cursor = 0

        active_loans:list(Loan) = [Loan(*i) for i in active_list[0]]
        active_loan_infos:list(ActiveLoanInfo) = [ActiveLoanInfo(*i) for i in active_list[1]]
        interest_owed_per_day:list(int) =  active_list[2]
        new_cursor = active_list[3]

        return ActiveLoans(
            active_loans,
            active_loan_infos,
            interest_owed_per_day,
            new_cursor
        ) 

    def get_loan_borrow_amount(self, nft_id:int, loan_id:int)->int:
        """
        Retrieves the borrow amount for a specific loan.
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :return: The borrow amount for the loan
        """    
        return self.helper_core.getLoanBorrowAmount(nft_id, loan_id).call()

    def get_loan_collateral_info(self, nft_id:int, loan_id:int)->LoanCollateralInfo:
        """
        Retrieves the collateral information for a specific loan.
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :return: A LoanCollateralInfo object containing the collateral information for the loan
        """
        return LoanCollateralInfo(*(self.helper_core.getLoanCollateralInfo(nft_id, loan_id).call()))
    
    def get_loan_current_ltv(self, nft_id:int, loan_id:int)->int:
        """
        Retrieves the current loan-to-value (LTV) ratio for a specific loan.
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :return: The current LTV ratio for the loan
        """
        return self.helper_core.getLoanCurrentLTV(loan_id, nft_id).call()
    
    def is_loan_liquidatable(self, loan_id:int)->bool:
        """
        Determines whether a loan is liquidatable.
        :param loan_id: The loan ID to check
        :return: True if the loan is liquidatable, False otherwise
        """
        return self.helper_core.isLoanLiquidable(loan_id).call()
    
    def get_settle_borrow_info(self, nft_id:int, loan_id:int)->SettleBorrowInfo:
        """
        Retrieves the information required to settle a borrow for a specific loan.
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :return: A SettleBorrowInfo object containing the settlement information for the loan
        """
        return SettleBorrowInfo(*(self.helper_core.getSettleBorrowInfo(nft_id, loan_id).call()))
    
    def get_pernalty_fee(self, nft_id:int, loan_id:int)->int:
        """
        Retrieves the penalty fee for a specific loan.
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :return: The penalty fee for the loan
        """
        return self.helper_core.getPenaltyFee(nft_id, loan_id).call()

    def calculate_max_repay(self, nft_id:int, loan_id:int, gap_time_borrow_interest_second:int )->int:
        """
        Calculates the maximum repayable amount for a loan given the gap time for borrow interest.
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :param gap_time_borrow_interest_second: The gap time in seconds for calculating borrow interest
        :return: The maximum repayable amount for the loan
        """
        return self.helper_core.calculateMaxRepay(nft_id, loan_id, gap_time_borrow_interest_second).call()
        
    def calculate_ltv_for_borrow(self, nft_id:int, loan_id:int, borrow_amount:int, borrow_token:IERC20Metadata, collateral_amount:int, collateral_token:IERC20Metadata)->int:
        """
        Calculates the loan-to-value (LTV) ratio for a loan when borrowing a specific amount.
        
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :param borrow_amount: The amount intended to borrow
        :param borrow_token: The token metadata of the borrowing token
        :param collateral_amount: The amount of collateral provided
        :param collateral_token: The token metadata of the collateral token
        :return: The calculated LTV ratio for the proposed borrow scenario
        """
        borrow_amount = parseEther(self.web3, borrow_amount, borrow_token.decimals().call())
        collateral_sent_amount = parseEther(self.web3, collateral_amount, collateral_token.decimals().call())
        return self.helper_core.calculateLTVForBorrow(
            nft_id,
            loan_id,
            borrow_amount,
            borrow_token.address,
            collateral_sent_amount,
            collateral_token.address
        ).call()
    
    def calculate_ltv_for_repay(self, nft_id:int, loan_id:int, repay_amount:int, is_only_interest:bool)->int:
        """
        Calculates the LTV ratio for a loan after repaying a specific amount.
        
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :param repay_amount: The amount intended to repay
        :param is_only_interest: A boolean indicating whether only the interest is being repaid
        :return: The calculated LTV ratio after the repayment
        """

        loan = self.loans(nft_id, loan_id)
        borrow_token:IERC20Metadata = IERC20Metadata(loan.borrowTokenAddress, self.web3)
        repay_amount = parseEther(self.web3, repay_amount, borrow_token.decimals().call())
        return self.helper_core.calculateLTVForRepay(nft_id, loan_id, repay_amount, is_only_interest).call()

    def calculate_ltv_for_adjust_collateral(self, nft_id:int, loan_id:int, adjust_amount:int, is_add:bool)->int:
        """
        Calculates the LTV ratio for a loan after adjusting the collateral by a specific amount.
        
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :param adjust_amount: The amount by which the collateral is being adjusted
        :param is_add: A boolean indicating whether the collateral is being added (True) or removed (False)
        :return: The calculated LTV ratio after the collateral adjustment
        """

        loan:Loan = self.loans(nft_id, loan_id)
        collateral_token:IERC20Metadata = IERC20Metadata(loan.collateralTokenAddress, self.web3)
        adjust_amount = parseEther(self.web3, adjust_amount, collateral_token.decimals().call())
        return self.helper_core.calculateLTVForAdjustColla(nft_id, loan_id, adjust_amount, is_add).call()
    
    def calculate_borrow_amount(self, nft_id:int, loan_id:int, borrow_amount:int, borrow_token:IERC20Metadata, collateral_sent_amount:int, collateral_token:IERC20Metadata, ltv:int)->BorrowAmountInfo:
        """
        Calculates the maximum amount that can be borrowed and the corresponding collateral amount required based on a specified LTV ratio.
        
        :param nft_id: The NFT ID associated with the loan
        :param loan_id: The loan ID
        :param borrow_amount: The amount intended to borrow
        :param borrow_token: The token metadata of the borrowing token
        :param collateral_sent_amount: The amount of collateral provided
        :param collateral_token: The token metadata of the collateral token
        :param ltv: The desired LTV ratio for the loan
        :return: A BorrowAmountInfo object containing the calculated maximum borrow amount and collateral amount
        """
        borrow_amount = parseEther(self.web3, borrow_amount, borrow_token.decimals().call())
        collateral_sent_amount = parseEther(self.web3, collateral_sent_amount, collateral_token.decimals().call())
        ltv = parseEther(self.web3, ltv)
        return BorrowAmountInfo(*(self.helper_core.calculateBorrowAmount(
            nft_id,
            loan_id,
            borrow_amount,
            borrow_token.address,
            collateral_sent_amount,
            collateral_token.address,
            ltv
        ).call()))
    