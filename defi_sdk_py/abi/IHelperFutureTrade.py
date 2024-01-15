
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

class PositionData:
    def __init__(self, position: Tuple, PNL: int, ROE: int, margin: int, rate: int, liqPrice: int):
        self.position = position
        self.PNL = PNL
        self.ROE = ROE
        self.margin = margin
        self.rate = rate
        self.liqPrice = liqPrice

    def __str__(self):
        return str({
            'position': self.position,
            'PNL': self.PNL,
            'ROE': self.ROE,
            'margin': self.margin,
            'rate': self.rate,
            'liqPrice': self.liqPrice,
        })


class PositionState:
    def __init__(self, active: bool, isLong: bool, PNL: int, startTimestamp: int, pairByte: bytes, averageEntryPrice: int, interestPaid: int, totalTradingFee: int, totalSwapFee: int):
        self.active = active
        self.isLong = isLong
        self.PNL = PNL
        self.startTimestamp = startTimestamp
        self.pairByte = pairByte
        self.averageEntryPrice = averageEntryPrice
        self.interestPaid = interestPaid
        self.totalTradingFee = totalTradingFee
        self.totalSwapFee = totalSwapFee

    def __str__(self):
        return str({
            'active': self.active,
            'isLong': self.isLong,
            'PNL': self.PNL,
            'startTimestamp': self.startTimestamp,
            'pairByte': self.pairByte,
            'averageEntryPrice': self.averageEntryPrice,
            'interestPaid': self.interestPaid,
            'totalTradingFee': self.totalTradingFee,
            'totalSwapFee': self.totalSwapFee,
        })




class IHelperFutureTrade:
    def __init__(self, contract_address, web3):
        """
        Initialize the contract instance.

        :param contract_address: The Ethereum address of the contract.
        :type contract_address: str
        :param web3: The Web3 instance for interacting with Ethereum.
        :type web3: Web3
        """
        self.contract:Web3.eth.contract = web3.eth.contract(address=contract_address, abi=[{'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'getAllActivePositions', 'outputs': [{'components': [{'components': [{'internalType': 'uint64', 'name': 'id', 'type': 'uint64'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'swapTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'entryPrice', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralSwappedAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwed', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwePerDay', 'type': 'uint256'}], 'internalType': 'struct CoreBase.Position', 'name': 'position', 'type': 'tuple'}, {'internalType': 'int256', 'name': 'PNL', 'type': 'int256'}, {'internalType': 'int256', 'name': 'ROE', 'type': 'int256'}, {'internalType': 'int256', 'name': 'margin', 'type': 'int256'}, {'internalType': 'uint256', 'name': 'rate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'liqPrice', 'type': 'uint256'}], 'internalType': 'struct HelperBase.PositionData[]', 'name': 'data', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'bool', 'name': 'isLong', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'expectedRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'slippage', 'type': 'uint256'}], 'name': 'getAveragePrice', 'outputs': [{'internalType': 'uint256', 'name': 'averagePrice', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'bool', 'name': 'isLong', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'expectedRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'slippage', 'type': 'uint256'}], 'name': 'getBalanceAfterOpenPosition', 'outputs': [{'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}], 'name': 'getBalanceDetails', 'outputs': [{'internalType': 'uint256', 'name': 'freeBalance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'usedBalance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'totalBalance', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}], 'name': 'getClosingFee', 'outputs': [{'internalType': 'uint256', 'name': 'swapFee', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tradingFee', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'totalFee', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'bool', 'name': 'isLong', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'expectedRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'slippage', 'type': 'uint256'}], 'name': 'getEntryPrice', 'outputs': [{'internalType': 'uint256', 'name': 'entryPrice', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'swapFee', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'swapSize', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'bool', 'name': 'isLong', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'expectedRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'slippage', 'type': 'uint256'}], 'name': 'getLiqPriceAfterOpenPosition', 'outputs': [{'internalType': 'uint256', 'name': 'liquidationPrice', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}], 'name': 'getLiquidationPrice', 'outputs': [{'internalType': 'uint256', 'name': 'liquidationPrice', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'bool', 'name': 'isAdd', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'getMarginAfterAdjustCollateral', 'outputs': [{'internalType': 'int256', 'name': 'margin', 'type': 'int256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'closingSize', 'type': 'uint256'}], 'name': 'getMarginAfterClosePosition', 'outputs': [{'internalType': 'int256', 'name': 'margin', 'type': 'int256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'bool', 'name': 'isLong', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'expectedRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'slippage', 'type': 'uint256'}], 'name': 'getMarginAfterOpenPosition', 'outputs': [{'internalType': 'int256', 'name': 'margin', 'type': 'int256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'bool', 'name': 'isLong', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'leverage', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'expectedRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'slippage', 'type': 'uint256'}], 'name': 'getMaxContractSize', 'outputs': [{'internalType': 'uint256', 'name': 'maxContractSize', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}], 'name': 'getMaxWithdrawal', 'outputs': [{'internalType': 'uint256', 'name': 'maxWithdrawal', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'bool', 'name': 'isLong', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'expectedRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'slippage', 'type': 'uint256'}], 'name': 'getOpeningFee', 'outputs': [{'internalType': 'uint256', 'name': 'swapFee', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tradingFee', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'totalFee', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'closingSize', 'type': 'uint256'}], 'name': 'getPNLAfterClosePosition', 'outputs': [{'internalType': 'int256', 'name': 'PNL', 'type': 'int256'}, {'internalType': 'int256', 'name': 'ROE', 'type': 'int256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}], 'name': 'getPositionMargin', 'outputs': [{'internalType': 'int256', 'name': 'margin', 'type': 'int256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'cursor', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'resultsPerPage', 'type': 'uint256'}], 'name': 'getPositionStates', 'outputs': [{'components': [{'internalType': 'bool', 'name': 'active', 'type': 'bool'}, {'internalType': 'bool', 'name': 'isLong', 'type': 'bool'}, {'internalType': 'int128', 'name': 'PNL', 'type': 'int128'}, {'internalType': 'uint64', 'name': 'startTimestamp', 'type': 'uint64'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'uint128', 'name': 'averageEntryPrice', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'interestPaid', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'totalTradingFee', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'totalSwapFee', 'type': 'uint128'}], 'internalType': 'struct CoreBase.PositionState[]', 'name': 'positionStates', 'type': 'tuple[]'}, {'internalType': 'uint256', 'name': 'newCursor', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'bool', 'name': 'isLong', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'leverage', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'expectedRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'slippage', 'type': 'uint256'}], 'name': 'getRequiredCollateral', 'outputs': [{'internalType': 'uint256', 'name': 'collateral', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}], 'name': 'getUnrealizedPNL', 'outputs': [{'internalType': 'int256', 'name': 'PNL', 'type': 'int256'}, {'internalType': 'int256', 'name': 'ROE', 'type': 'int256'}], 'stateMutability': 'view', 'type': 'function'}])
        self.web3:Web3 = web3
        self.address = contract_address

    def __str__(self):
        return self.address

    # Generated functions
    
    def getAllActivePositions(self, nftId: int):
        return self.contract.functions.getAllActivePositions(nftId)

    def getAveragePrice(self, nftId: int, pairByte: bytes, isLong: bool, contractSize: int, expectedRate: int, slippage: int):
        return self.contract.functions.getAveragePrice(nftId, pairByte, isLong, contractSize, expectedRate, slippage)

    def getBalanceAfterOpenPosition(self, nftId: int, pairByte: bytes, isLong: bool, contractSize: int, expectedRate: int, slippage: int):
        return self.contract.functions.getBalanceAfterOpenPosition(nftId, pairByte, isLong, contractSize, expectedRate, slippage)

    def getBalanceDetails(self, nftId: int, pairByte: bytes):
        return self.contract.functions.getBalanceDetails(nftId, pairByte)

    def getClosingFee(self, nftId: int, pairByte: bytes, contractSize: int):
        return self.contract.functions.getClosingFee(nftId, pairByte, contractSize)

    def getEntryPrice(self, nftId: int, pairByte: bytes, isLong: bool, contractSize: int, expectedRate: int, slippage: int):
        return self.contract.functions.getEntryPrice(nftId, pairByte, isLong, contractSize, expectedRate, slippage)

    def getLiqPriceAfterOpenPosition(self, nftId: int, pairByte: bytes, isLong: bool, contractSize: int, expectedRate: int, slippage: int):
        return self.contract.functions.getLiqPriceAfterOpenPosition(nftId, pairByte, isLong, contractSize, expectedRate, slippage)

    def getLiquidationPrice(self, nftId: int, pairByte: bytes):
        return self.contract.functions.getLiquidationPrice(nftId, pairByte)

    def getMarginAfterAdjustCollateral(self, nftId: int, pairByte: bytes, isAdd: bool, amount: int):
        return self.contract.functions.getMarginAfterAdjustCollateral(nftId, pairByte, isAdd, amount)

    def getMarginAfterClosePosition(self, nftId: int, pairByte: bytes, closingSize: int):
        return self.contract.functions.getMarginAfterClosePosition(nftId, pairByte, closingSize)

    def getMarginAfterOpenPosition(self, nftId: int, pairByte: bytes, isLong: bool, contractSize: int, expectedRate: int, slippage: int):
        return self.contract.functions.getMarginAfterOpenPosition(nftId, pairByte, isLong, contractSize, expectedRate, slippage)

    def getMaxContractSize(self, nftId: int, pairByte: bytes, isLong: bool, leverage: int, expectedRate: int, slippage: int):
        return self.contract.functions.getMaxContractSize(nftId, pairByte, isLong, leverage, expectedRate, slippage)

    def getMaxWithdrawal(self, nftId: int, pairByte: bytes):
        return self.contract.functions.getMaxWithdrawal(nftId, pairByte)

    def getOpeningFee(self, nftId: int, pairByte: bytes, isLong: bool, contractSize: int, expectedRate: int, slippage: int):
        return self.contract.functions.getOpeningFee(nftId, pairByte, isLong, contractSize, expectedRate, slippage)

    def getPNLAfterClosePosition(self, nftId: int, pairByte: bytes, closingSize: int):
        return self.contract.functions.getPNLAfterClosePosition(nftId, pairByte, closingSize)

    def getPositionMargin(self, nftId: int, pairByte: bytes):
        return self.contract.functions.getPositionMargin(nftId, pairByte)

    def getPositionStates(self, nftId: int, cursor: int, resultsPerPage: int):
        return self.contract.functions.getPositionStates(nftId, cursor, resultsPerPage)

    def getRequiredCollateral(self, nftId: int, pairByte: bytes, isLong: bool, contractSize: int, leverage: int, expectedRate: int, slippage: int):
        return self.contract.functions.getRequiredCollateral(nftId, pairByte, isLong, contractSize, leverage, expectedRate, slippage)

    def getUnrealizedPNL(self, nftId: int, pairByte: bytes):
        return self.contract.functions.getUnrealizedPNL(nftId, pairByte)
