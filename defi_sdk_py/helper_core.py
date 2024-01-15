from web3 import Web3, types
from .abi.IHelperCore import *
from .abi.IERC20Metadata import IERC20Metadata
from .abi.IHelperCore import IHelperCore
from .utils import parseEther, TransactionReceipt
from .address_const import AddressConst
from typing import Union, List
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
