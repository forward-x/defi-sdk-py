
from web3 import Web3
from web3.logs import STRICT, IGNORE, DISCARD, WARN
from typing import Tuple, Dict, List
import json
#Generate a Python class representing the Ethereum contract.
#:param abi: The ABI (Application Binary Interface) of the contract.
#:type abi: list
#:param contract_name: The name of the contract class default is MyContract.
#:type contract_name: str
#:return: The generated Python class code.
#:rtype: str

class RankInfo:
    def __init__(self, interestBonusLending: int, forwardBonusLending: int, minimumStakeAmount: int, maxLTVBonus: int, tradingFee: int, tradingBonus: int):
        self.interestBonusLending = interestBonusLending
        self.forwardBonusLending = forwardBonusLending
        self.minimumStakeAmount = minimumStakeAmount
        self.maxLTVBonus = maxLTVBonus
        self.tradingFee = tradingFee
        self.tradingBonus = tradingBonus

    def __str__(self):
        return str({
            'interestBonusLending': self.interestBonusLending,
            'forwardBonusLending': self.forwardBonusLending,
            'minimumStakeAmount': self.minimumStakeAmount,
            'maxLTVBonus': self.maxLTVBonus,
            'tradingFee': self.tradingFee,
            'tradingBonus': self.tradingBonus,
        })




class IHelperPool:
    def __init__(self, contract_address, web3):
        """
        Initialize the contract instance.

        :param contract_address: The Ethereum address of the contract.
        :type contract_address: str
        :param web3: The Web3 instance for interacting with Ethereum.
        :type web3: Web3
        """
        self.contract:Web3.eth.contract = web3.eth.contract(address=contract_address, abi=[{'inputs': [{'internalType': 'address', 'name': 'poolAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'daySecond', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'borrowingAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}], 'name': 'calculateBorrowingInterest', 'outputs': [{'internalType': 'uint256', 'name': 'ltv', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interest', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'poolAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'claimableInterest', 'outputs': [{'internalType': 'uint256', 'name': 'tokenInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterest', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'poolAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'claimableInterestMembership', 'outputs': [{'internalType': 'uint256', 'name': 'tokenInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterest', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'poolAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'interestAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'daySecond', 'type': 'uint256'}], 'name': 'getDepositAmountByInterestAmount', 'outputs': [{'internalType': 'uint256', 'name': 'depositAmount', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'poolAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'depositAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'daySecond', 'type': 'uint256'}], 'name': 'getInterestAmountByDepositAmount', 'outputs': [{'internalType': 'uint256', 'name': 'interestAmount', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'poolAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'getLendingInfo', 'outputs': [{'internalType': 'uint256', 'name': 'lendingBalance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestTokenGained', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestForwGained', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'rank', 'type': 'uint8'}, {'components': [{'internalType': 'uint256', 'name': 'interestBonusLending', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwardBonusLending', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minimumStakeAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxLTVBonus', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tradingFee', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tradingBonus', 'type': 'uint256'}], 'internalType': 'struct StakePoolBase.RankInfo', 'name': 'rankInfo', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'poolAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'newDepositAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwPriceRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwPricePrecision', 'type': 'uint256'}], 'name': 'getNextLendingForwInterest', 'outputs': [{'internalType': 'uint256', 'name': 'interestRate', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'poolAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'depositAmount', 'type': 'uint256'}], 'name': 'getNextLendingInterest', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'getPenaltyFee', 'outputs': [{'internalType': 'uint256', 'name': 'penaltyFee', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'poolAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'forwPriceRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwPricePrecision', 'type': 'uint256'}], 'name': 'getPoolInfo', 'outputs': [{'internalType': 'uint256', 'name': 'borrowingInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lendingTokenInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lendingForwInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'utilizationRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'pTokenTotalSupply', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'currentSupply', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}])
        self.web3:Web3 = web3
        self.address = contract_address

    def __str__(self):
        return self.address

    # Generated functions
    
    def calculateBorrowingInterest(self, poolAddress: str, daySecond: int, borrowingAmount: int, collateralAmount: int, collateralTokenAddress: str):
        return self.contract.functions.calculateBorrowingInterest(poolAddress, daySecond, borrowingAmount, collateralAmount, collateralTokenAddress)

    def claimableInterest(self, poolAddress: str, nftId: int):
        return self.contract.functions.claimableInterest(poolAddress, nftId)

    def claimableInterestMembership(self, poolAddress: str, nftId: int):
        return self.contract.functions.claimableInterestMembership(poolAddress, nftId)

    def getDepositAmountByInterestAmount(self, poolAddress: str, interestAmount: int, daySecond: int):
        return self.contract.functions.getDepositAmountByInterestAmount(poolAddress, interestAmount, daySecond)

    def getInterestAmountByDepositAmount(self, poolAddress: str, depositAmount: int, daySecond: int):
        return self.contract.functions.getInterestAmountByDepositAmount(poolAddress, depositAmount, daySecond)

    def getLendingInfo(self, poolAddress: str, nftId: int):
        return self.contract.functions.getLendingInfo(poolAddress, nftId)

    def getNextLendingForwInterest(self, poolAddress: str, newDepositAmount: int, forwPriceRate: int, forwPricePrecision: int):
        return self.contract.functions.getNextLendingForwInterest(poolAddress, newDepositAmount, forwPriceRate, forwPricePrecision)

    def getNextLendingInterest(self, poolAddress: str, depositAmount: int):
        return self.contract.functions.getNextLendingInterest(poolAddress, depositAmount)

    def getPenaltyFee(self, nftId: int, loanId: int):
        return self.contract.functions.getPenaltyFee(nftId, loanId)

    def getPoolInfo(self, poolAddress: str, forwPriceRate: int, forwPricePrecision: int):
        return self.contract.functions.getPoolInfo(poolAddress, forwPriceRate, forwPricePrecision)
