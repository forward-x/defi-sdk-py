
from web3 import Web3
from typing import Tuple, Dict, List
import json
#Generate a Python class representing the Ethereum contract.
#:param abi: The ABI (Application Binary Interface) of the contract.
#:type abi: list
#:param contract_name: The name of the contract class default is MyContract.
#:type contract_name: str
#:return: The generated Python class code.
#:rtype: str

class Loan:
    def __init__(self, interestPaid: int, borrowTokenAddress: str, rolloverTimestamp: int, lastSettleTimestamp: int, collateralTokenAddress: str, borrowAmount: int, collateralAmount: int, owedPerDay: int, minInterest: int, interestOwed: int):
        self.interestPaid = interestPaid
        self.borrowTokenAddress = borrowTokenAddress
        self.rolloverTimestamp = rolloverTimestamp
        self.lastSettleTimestamp = lastSettleTimestamp
        self.collateralTokenAddress = collateralTokenAddress
        self.borrowAmount = borrowAmount
        self.collateralAmount = collateralAmount
        self.owedPerDay = owedPerDay
        self.minInterest = minInterest
        self.interestOwed = interestOwed

    def __str__(self):
        return str({
            'interestPaid': self.interestPaid,
            'borrowTokenAddress': self.borrowTokenAddress,
            'rolloverTimestamp': self.rolloverTimestamp,
            'lastSettleTimestamp': self.lastSettleTimestamp,
            'collateralTokenAddress': self.collateralTokenAddress,
            'borrowAmount': self.borrowAmount,
            'collateralAmount': self.collateralAmount,
            'owedPerDay': self.owedPerDay,
            'minInterest': self.minInterest,
            'interestOwed': self.interestOwed,
        })


class ActiveLoanInfo:
    def __init__(self, id: int, currentLTV: int, liquidationLTV: int, apr: int, minInterestOwed: int, actualInterestOwed: int):
        self.id = id
        self.currentLTV = currentLTV
        self.liquidationLTV = liquidationLTV
        self.apr = apr
        self.minInterestOwed = minInterestOwed
        self.actualInterestOwed = actualInterestOwed

    def __str__(self):
        return str({
            'id': self.id,
            'currentLTV': self.currentLTV,
            'liquidationLTV': self.liquidationLTV,
            'apr': self.apr,
            'minInterestOwed': self.minInterestOwed,
            'actualInterestOwed': self.actualInterestOwed,
        })




class IHelperCore:
    def __init__(self, contract_address, web3):
        """
        Initialize the contract instance.

        :param contract_address: The Ethereum address of the contract.
        :type contract_address: str
        :param web3: The Web3 instance for interacting with Ethereum.
        :type web3: Web3
        """
        self.contract:Web3.eth.contract = web3.eth.contract(address=contract_address, abi=[{'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'collateralAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'ltv', 'type': 'uint256'}], 'name': 'calculateBorrowAmount', 'outputs': [{'internalType': 'uint256', 'name': 'maxBorrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxCollateralAmount', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'isAdd', 'type': 'bool'}], 'name': 'calculateLTVForAdjustColla', 'outputs': [{'internalType': 'uint256', 'name': 'ltv', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'collateralAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}], 'name': 'calculateLTVForBorrow', 'outputs': [{'internalType': 'uint256', 'name': 'ltv', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'repayAmount', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'isOnlyInterest', 'type': 'bool'}], 'name': 'calculateLTVForRepay', 'outputs': [{'internalType': 'uint256', 'name': 'ltv', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'gapTimeBorrowInterestSecond', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'isOnlyInterest', 'type': 'bool'}], 'name': 'calculateMaxRepay', 'outputs': [{'internalType': 'uint256', 'name': 'maxRepay', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'cursor', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'resultsPerPage', 'type': 'uint256'}], 'name': 'getActiveLoans', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'uint64', 'name': 'rolloverTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'owedPerDay', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwed', 'type': 'uint256'}], 'internalType': 'struct CoreBase.Loan[]', 'name': 'activeLoans', 'type': 'tuple[]'}, {'components': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'currentLTV', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'liquidationLTV', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'apr', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterestOwed', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'actualInterestOwed', 'type': 'uint256'}], 'internalType': 'struct HelperBase.ActiveLoanInfo[]', 'name': 'activeLoanInfos', 'type': 'tuple[]'}, {'internalType': 'uint256[]', 'name': 'interestOwedPerDays', 'type': 'uint256[]'}, {'internalType': 'uint256', 'name': 'newCursor', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'getLoanBorrowAmount', 'outputs': [{'internalType': 'uint256', 'name': 'maximumBorrowAmount', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'getLoanCollateralInfo', 'outputs': [{'internalType': 'uint256', 'name': 'minimumCollateral', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'removableCollateral', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'getLoanCurrentLTV', 'outputs': [{'internalType': 'uint256', 'name': 'ltv', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'getPenaltyFee', 'outputs': [{'internalType': 'uint256', 'name': 'penaltyFee', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'getSettleBorrowInfo', 'outputs': [{'internalType': 'uint256', 'name': 'settledBorrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'settledLTV', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'rate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'precision', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'isLoanLiquidable', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'poolAddess', 'type': 'address'}], 'name': 'isPool', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}])
        self.web3:Web3 = web3
        self.address = contract_address

    def __str__(self):
        return self.address

    # Generated functions
    
    def calculateBorrowAmount(self, nftId: int, loanId: int, borrowAmount: int, borrowTokenAddress: str, collateralAmount: int, collateralTokenAddress: str, ltv: int):
        return self.contract.functions.calculateBorrowAmount(nftId, loanId, borrowAmount, borrowTokenAddress, collateralAmount, collateralTokenAddress, ltv)

    def calculateLTVForAdjustColla(self, nftId: int, loanId: int, amount: int, isAdd: bool):
        return self.contract.functions.calculateLTVForAdjustColla(nftId, loanId, amount, isAdd)

    def calculateLTVForBorrow(self, nftId: int, loanId: int, borrowAmount: int, borrowTokenAddress: str, collateralAmount: int, collateralTokenAddress: str):
        return self.contract.functions.calculateLTVForBorrow(nftId, loanId, borrowAmount, borrowTokenAddress, collateralAmount, collateralTokenAddress)

    def calculateLTVForRepay(self, nftId: int, loanId: int, repayAmount: int, isOnlyInterest: bool):
        return self.contract.functions.calculateLTVForRepay(nftId, loanId, repayAmount, isOnlyInterest)

    def calculateMaxRepay(self, nftId: int, loanId: int, gapTimeBorrowInterestSecond: int, isOnlyInterest: bool):
        return self.contract.functions.calculateMaxRepay(nftId, loanId, gapTimeBorrowInterestSecond, isOnlyInterest)

    def getActiveLoans(self, nftId: int, cursor: int, resultsPerPage: int):
        return self.contract.functions.getActiveLoans(nftId, cursor, resultsPerPage)

    def getLoanBorrowAmount(self, nftId: int, loanId: int):
        return self.contract.functions.getLoanBorrowAmount(nftId, loanId)

    def getLoanCollateralInfo(self, nftId: int, loanId: int):
        return self.contract.functions.getLoanCollateralInfo(nftId, loanId)

    def getLoanCurrentLTV(self, loanId: int, nftId: int):
        return self.contract.functions.getLoanCurrentLTV(loanId, nftId)

    def getPenaltyFee(self, nftId: int, loanId: int):
        return self.contract.functions.getPenaltyFee(nftId, loanId)

    def getSettleBorrowInfo(self, nftId: int, loanId: int):
        return self.contract.functions.getSettleBorrowInfo(nftId, loanId)

    def isLoanLiquidable(self, nftId: int, loanId: int):
        return self.contract.functions.isLoanLiquidable(nftId, loanId)

    def isPool(self, poolAddess: str):
        return self.contract.functions.isPool(poolAddess)
