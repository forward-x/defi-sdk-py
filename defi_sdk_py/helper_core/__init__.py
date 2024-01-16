from ..abi.IHelperCore import *
from ..abi.IERC20Metadata import IERC20Metadata
from ..abi.IHelperCore import IHelperCore
from ..utils import parseEther
import json

class ActiveLoans:

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

    def __init__(self, minimumCollateral, removableCollateral) -> None:
        self.minimumCollateral = minimumCollateral
        self.removableCollateral = removableCollateral
    def __str__(self):
        return str({
            "minumum_collateral" : self.minimumCollateral,
            "removable_collateral" : self.removableCollateral
        })

class SettleBorrowInfo:

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

    def __init__(self, maxBorrowAmount, maxCollateralAmount) -> None:
        self.maxBorrowAmount = maxBorrowAmount
        self.maxCollateralAmount = maxCollateralAmount

    def __str__(self):
        return str({
            "maxBorrowAmount" : self.maxBorrowAmount,
            "maxCollateralAmount" : self.maxCollateralAmount
        })

class HelperCore:

    def __init__(self):
        super(HelperCore, self).__init__()
        self.helper_core:IHelperCore = IHelperCore(self.address_const.get_helper_core_address(), self.web3)

    def get_active_loans(self, nft_id:int, cursor:int=1, result_per_page:int=1)->ActiveLoans:
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
        return self.helper_core.getLoanBorrowAmount(nft_id, loan_id).call()

    def get_loan_collateral_info(self, nft_id:int, loan_id:int)->LoanCollateralInfo:
        return LoanCollateralInfo(*(self.helper_core.getLoanCollateralInfo(nft_id, loan_id).call()))
    
    def get_loan_current_ltv(self, nft_id:int, loan_id:int)->int:
        return self.helper_core.getLoanCurrentLTV(loan_id, nft_id).call()
    
    def is_loan_liquidatable(self, loan_id:int)->bool:
        return self.helper_core.isLoanLiquidable(loan_id).call()
    
    def get_settle_borrow_info(self, nft_id:int, loan_id:int)->SettleBorrowInfo:
        return SettleBorrowInfo(*(self.helper_core.getSettleBorrowInfo(nft_id, loan_id).call()))
    
    def get_pernalt_fee(self, nft_id:int, loan_id:int)->int:
        return self.helper_core.getPenaltyFee(nft_id, loan_id).call()

    def calculate_max_repay(self, nft_id:int, loan_id:int, gap_time_borrow_interest_second:int )->int:
        return self.helper_core.calculateMaxRepay(nft_id, loan_id, gap_time_borrow_interest_second).call()
        
    def calculate_ltv_for_borrow(self, nft_id:int, loan_id:int, borrow_amount:int, borrow_token:IERC20Metadata, collateral_amount:int, collateral_token:IERC20Metadata)->int:
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
        loan = self.loans(nft_id, loan_id)
        borrow_token:IERC20Metadata = IERC20Metadata(loan.borrowTokenAddress, self.web3)
        repay_amount = parseEther(self.web3, repay_amount, borrow_token.decimals().call())
        return self.helper_core.calculateLTVForRepay(nft_id, loan_id, repay_amount, is_only_interest).call()

    def calculate_ltv_for_adjust_collateral(self, nft_id:int, loan_id:int, adjust_amount:int, is_add:bool)->int:
        loan:Loan = self.loans(nft_id, loan_id)
        collateral_token:IERC20Metadata = IERC20Metadata(loan.collateralTokenAddress, self.web3)
        adjust_amount = parseEther(self.web3, adjust_amount, collateral_token.decimals().call())
        return self.helper_core.calculateLTVForAdjustColla(nft_id, loan_id, adjust_amount, is_add).call()
    
    def calculate_borrow_amount(self, nft_id:int, loan_id:int, borrow_amount:int, borrow_token:IERC20Metadata, collateral_sent_amount:int, collateral_token:IERC20Metadata, ltv:int)->BorrowAmountInfo:
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
    



