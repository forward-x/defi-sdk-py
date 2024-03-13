
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


class WithdrawResult:
    def __init__(self, principle: int, tokenInterest: int, forwInterest: int, pTokenBurn: int, atpTokenBurn: int, lossBurn: int, itpTokenBurn: int, ifpTokenBurn: int, tokenInterestBonus: int, forwInterestBonus: int):
        self.principle = principle
        self.tokenInterest = tokenInterest
        self.forwInterest = forwInterest
        self.pTokenBurn = pTokenBurn
        self.atpTokenBurn = atpTokenBurn
        self.lossBurn = lossBurn
        self.itpTokenBurn = itpTokenBurn
        self.ifpTokenBurn = ifpTokenBurn
        self.tokenInterestBonus = tokenInterestBonus
        self.forwInterestBonus = forwInterestBonus

    def __str__(self):
        return str({
            'principle': self.principle,
            'tokenInterest': self.tokenInterest,
            'forwInterest': self.forwInterest,
            'pTokenBurn': self.pTokenBurn,
            'atpTokenBurn': self.atpTokenBurn,
            'lossBurn': self.lossBurn,
            'itpTokenBurn': self.itpTokenBurn,
            'ifpTokenBurn': self.ifpTokenBurn,
            'tokenInterestBonus': self.tokenInterestBonus,
            'forwInterestBonus': self.forwInterestBonus,
        })


class Lend:
    def __init__(self, rank: int, updatedTimestamp: int):
        self.rank = rank
        self.updatedTimestamp = updatedTimestamp

    def __str__(self):
        return str({
            'rank': self.rank,
            'updatedTimestamp': self.updatedTimestamp,
        })


class PoolTokens:
    def __init__(self, pToken: int, atpToken: int, itpToken: int, ifpToken: int):
        self.pToken = pToken
        self.atpToken = atpToken
        self.itpToken = itpToken
        self.ifpToken = ifpToken

    def __str__(self):
        return str({
            'pToken': self.pToken,
            'atpToken': self.atpToken,
            'itpToken': self.itpToken,
            'ifpToken': self.ifpToken,
        })


class ActivateRankEvent:
    def __init__(self, event_data):
        self.owner: str = event_data.get('owner')
        self.nftId: int = event_data.get('nftId')
        self.oldRank: int = event_data.get('oldRank')
        self.newRank: int = event_data.get('newRank')

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)


class BorrowEvent:
    def __init__(self, event_data):
        self.owner: str = event_data.get('owner')
        self.nftId: int = event_data.get('nftId')
        self.tokenAddress: str = event_data.get('tokenAddress')
        self.isTrading: bool = event_data.get('isTrading')
        self.amount: int = event_data.get('amount')

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)


class ClaimForwInterestEvent:
    def __init__(self, event_data):
        self.owner: str = event_data.get('owner')
        self.nftId: int = event_data.get('nftId')
        self.interestForwClaimed: int = event_data.get('interestForwClaimed')
        self.interestForwBonus: int = event_data.get('interestForwBonus')
        self.burnedIfp: int = event_data.get('burnedIfp')

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)


class ClaimTokenInterestEvent:
    def __init__(self, event_data):
        self.owner: str = event_data.get('owner')
        self.nftId: int = event_data.get('nftId')
        self.interestTokenClaimed: int = event_data.get('interestTokenClaimed')
        self.interestTokenBonus: int = event_data.get('interestTokenBonus')
        self.burnedItp: int = event_data.get('burnedItp')

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)


class DepositEvent:
    def __init__(self, event_data):
        self.owner: str = event_data.get('owner')
        self.nftId: int = event_data.get('nftId')
        self.depositAmount: int = event_data.get('depositAmount')
        self.mintedP: int = event_data.get('mintedP')
        self.mintedAtp: int = event_data.get('mintedAtp')
        self.mintedItp: int = event_data.get('mintedItp')
        self.mintedIfp: int = event_data.get('mintedIfp')

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)


class WithdrawEvent:
    def __init__(self, event_data):
        self.owner: str = event_data.get('owner')
        self.nftId: int = event_data.get('nftId')
        self.withdrawAmount: int = event_data.get('withdrawAmount')
        self.burnedP: int = event_data.get('burnedP')
        self.burnedAtp: int = event_data.get('burnedAtp')
        self.burnedLoss: int = event_data.get('burnedLoss')
        self.burnedItp: int = event_data.get('burnedItp')
        self.burnedIfp: int = event_data.get('burnedIfp')

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)




class IAPHPool:
    def __init__(self, contract_address, web3):
        """
        Initialize the contract instance.

        :param contract_address: The Ethereum address of the contract.
        :type contract_address: str
        :param web3: The Web3 instance for interacting with Ethereum.
        :type web3: Web3
        """
        self.contract:Web3.eth.contract = web3.eth.contract(address=contract_address, abi=[{'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'oldRank', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint8', 'name': 'newRank', 'type': 'uint8'}], 'name': 'ActivateRank', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'indexed': True, 'internalType': 'address', 'name': 'tokenAddress', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'isTrading', 'type': 'bool'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'Borrow', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'interestForwClaimed', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'interestForwBonus', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'burnedIfp', 'type': 'uint256'}], 'name': 'ClaimForwInterest', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'interestTokenClaimed', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'interestTokenBonus', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'burnedItp', 'type': 'uint256'}], 'name': 'ClaimTokenInterest', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'depositAmount', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'mintedP', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'mintedAtp', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'mintedItp', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'mintedIfp', 'type': 'uint256'}], 'name': 'Deposit', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'withdrawAmount', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'burnedP', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'burnedAtp', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'burnedLoss', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'burnedItp', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'burnedIfp', 'type': 'uint256'}], 'name': 'Withdraw', 'type': 'event'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'activateRank', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'addLoss', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'atpTokenTotalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'balanceAtpTokenOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'balanceIfpTokenOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'balanceItpTokenOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'balancePTokenOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralSentAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}], 'name': 'borrow', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'uint64', 'name': 'rolloverTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'owedPerDay', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwed', 'type': 'uint256'}], 'internalType': 'struct CoreBase.Loan', 'name': '', 'type': 'tuple'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}], 'name': 'calculateInterest', 'outputs': [{'internalType': 'uint256', 'name': 'interestRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwedPerDay', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'claimAllInterest', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'principle', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'pTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'atpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lossBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'itpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ifpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterestBonus', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterestBonus', 'type': 'uint256'}], 'internalType': 'struct PoolBase.WithdrawResult', 'name': '', 'type': 'tuple'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'claimAmount', 'type': 'uint256'}], 'name': 'claimForwInterest', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'principle', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'pTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'atpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lossBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'itpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ifpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterestBonus', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterestBonus', 'type': 'uint256'}], 'internalType': 'struct PoolBase.WithdrawResult', 'name': '', 'type': 'tuple'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'claimAmount', 'type': 'uint256'}], 'name': 'claimTokenInterest', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'principle', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'pTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'atpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lossBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'itpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ifpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterestBonus', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterestBonus', 'type': 'uint256'}], 'internalType': 'struct PoolBase.WithdrawResult', 'name': '', 'type': 'tuple'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'coreAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'currentSupply', 'outputs': [{'internalType': 'uint256', 'name': '_currentSupply', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'depositAmount', 'type': 'uint256'}], 'name': 'deposit', 'outputs': [{'internalType': 'uint256', 'name': 'mintedP', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'mintedItp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'mintedIfp', 'type': 'uint256'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [], 'name': 'forwAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getActualTokenPrice', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getInterestForwPrice', 'outputs': [{'internalType': 'uint256', 'name': 'ifpPrice', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getInterestTokenPrice', 'outputs': [{'internalType': 'uint256', 'name': 'itpPrice', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}], 'name': 'getNextBorrowingInterest', 'outputs': [{'internalType': 'uint256', 'name': 'nextInterestRate', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getRates', 'outputs': [{'internalType': 'uint256[10]', 'name': '', 'type': 'uint256[10]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getUtils', 'outputs': [{'internalType': 'uint256[10]', 'name': '', 'type': 'uint256[10]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'ifpTokenTotalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'itpTokenTotalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'NFTId', 'type': 'uint256'}], 'name': 'lenders', 'outputs': [{'components': [{'internalType': 'uint8', 'name': 'rank', 'type': 'uint8'}, {'internalType': 'uint64', 'name': 'updatedTimestamp', 'type': 'uint64'}], 'internalType': 'struct PoolBase.Lend', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'membershipAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'swapTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'entryPrice', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'leverage', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'slippage', 'type': 'uint256'}], 'name': 'openPosition', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'pTokenTotalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'tokenAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'tokenHolders', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'pToken', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'atpToken', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'itpToken', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ifpToken', 'type': 'uint256'}], 'internalType': 'struct PoolToken.PoolTokens', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'utilizationRate', 'outputs': [{'internalType': 'uint256', 'name': '_utilizationRate', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'withdrawAmount', 'type': 'uint256'}], 'name': 'withdraw', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'principle', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'pTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'atpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lossBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'itpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ifpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterestBonus', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterestBonus', 'type': 'uint256'}], 'internalType': 'struct PoolBase.WithdrawResult', 'name': '', 'type': 'tuple'}], 'stateMutability': 'nonpayable', 'type': 'function'}])
        self.web3:Web3 = web3
        self.address = contract_address

    def __str__(self):
        return self.address

    # Generated functions
    
    def event_activaterank_by_block(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.ActivateRank().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def event_activaterank_by_tx(self, tx_hash:str):
        receipt = self.web3.eth.get_transaction_receipt(tx_hash)
        events = self.contract.events.ActivateRank().process_receipt(receipt, errors=DISCARD)
        if len(events) > 0:
            return events[0].args
        else:
            raise Exception('Event not found in transaction')


    def event_borrow_by_block(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.Borrow().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def event_borrow_by_tx(self, tx_hash:str):
        receipt = self.web3.eth.get_transaction_receipt(tx_hash)
        events = self.contract.events.Borrow().process_receipt(receipt, errors=DISCARD)
        if len(events) > 0:
            return events[0].args
        else:
            raise Exception('Event not found in transaction')


    def event_claimforwinterest_by_block(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.ClaimForwInterest().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def event_claimforwinterest_by_tx(self, tx_hash:str):
        receipt = self.web3.eth.get_transaction_receipt(tx_hash)
        events = self.contract.events.ClaimForwInterest().process_receipt(receipt, errors=DISCARD)
        if len(events) > 0:
            return events[0].args
        else:
            raise Exception('Event not found in transaction')


    def event_claimtokeninterest_by_block(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.ClaimTokenInterest().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def event_claimtokeninterest_by_tx(self, tx_hash:str):
        receipt = self.web3.eth.get_transaction_receipt(tx_hash)
        events = self.contract.events.ClaimTokenInterest().process_receipt(receipt, errors=DISCARD)
        if len(events) > 0:
            return events[0].args
        else:
            raise Exception('Event not found in transaction')


    def event_deposit_by_block(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.Deposit().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def event_deposit_by_tx(self, tx_hash:str):
        receipt = self.web3.eth.get_transaction_receipt(tx_hash)
        events = self.contract.events.Deposit().process_receipt(receipt, errors=DISCARD)
        if len(events) > 0:
            return events[0].args
        else:
            raise Exception('Event not found in transaction')


    def event_withdraw_by_block(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.Withdraw().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def event_withdraw_by_tx(self, tx_hash:str):
        receipt = self.web3.eth.get_transaction_receipt(tx_hash)
        events = self.contract.events.Withdraw().process_receipt(receipt, errors=DISCARD)
        if len(events) > 0:
            return events[0].args
        else:
            raise Exception('Event not found in transaction')


    def activateRank(self, nftId: int):
        return self.contract.functions.activateRank(nftId)

    def addLoss(self, amount: int):
        return self.contract.functions.addLoss(amount)

    def atpTokenTotalSupply(self, ):
        return self.contract.functions.atpTokenTotalSupply()

    def balanceAtpTokenOf(self, nftId: int):
        return self.contract.functions.balanceAtpTokenOf(nftId)

    def balanceIfpTokenOf(self, nftId: int):
        return self.contract.functions.balanceIfpTokenOf(nftId)

    def balanceItpTokenOf(self, nftId: int):
        return self.contract.functions.balanceItpTokenOf(nftId)

    def balancePTokenOf(self, nftId: int):
        return self.contract.functions.balancePTokenOf(nftId)

    def borrow(self, loanId: int, nftId: int, borrowAmount: int, collateralSentAmount: int, collateralTokenAddress: str):
        return self.contract.functions.borrow(loanId, nftId, borrowAmount, collateralSentAmount, collateralTokenAddress)

    def calculateInterest(self, borrowAmount: int):
        return self.contract.functions.calculateInterest(borrowAmount)

    def claimAllInterest(self, nftId: int):
        return self.contract.functions.claimAllInterest(nftId)

    def claimForwInterest(self, nftId: int, claimAmount: int):
        return self.contract.functions.claimForwInterest(nftId, claimAmount)

    def claimTokenInterest(self, nftId: int, claimAmount: int):
        return self.contract.functions.claimTokenInterest(nftId, claimAmount)

    def coreAddress(self, ):
        return self.contract.functions.coreAddress()

    def currentSupply(self, ):
        return self.contract.functions.currentSupply()

    def deposit(self, nftId: int, depositAmount: int):
        return self.contract.functions.deposit(nftId, depositAmount)

    def forwAddress(self, ):
        return self.contract.functions.forwAddress()

    def getActualTokenPrice(self, ):
        return self.contract.functions.getActualTokenPrice()

    def getInterestForwPrice(self, ):
        return self.contract.functions.getInterestForwPrice()

    def getInterestTokenPrice(self, ):
        return self.contract.functions.getInterestTokenPrice()

    def getNextBorrowingInterest(self, borrowAmount: int):
        return self.contract.functions.getNextBorrowingInterest(borrowAmount)

    def getRates(self, ):
        return self.contract.functions.getRates()

    def getUtils(self, ):
        return self.contract.functions.getUtils()

    def ifpTokenTotalSupply(self, ):
        return self.contract.functions.ifpTokenTotalSupply()

    def itpTokenTotalSupply(self, ):
        return self.contract.functions.itpTokenTotalSupply()

    def lenders(self, NFTId: int):
        return self.contract.functions.lenders(NFTId)

    def membershipAddress(self, ):
        return self.contract.functions.membershipAddress()

    def openPosition(self, nftId: int, collateralTokenAddress: str, swapTokenAddress: str, entryPrice: int, contractSize: int, leverage: int, slippage: int):
        return self.contract.functions.openPosition(nftId, collateralTokenAddress, swapTokenAddress, entryPrice, contractSize, leverage, slippage)

    def pTokenTotalSupply(self, ):
        return self.contract.functions.pTokenTotalSupply()

    def tokenAddress(self, ):
        return self.contract.functions.tokenAddress()

    def tokenHolders(self, nftId: int):
        return self.contract.functions.tokenHolders(nftId)

    def utilizationRate(self, ):
        return self.contract.functions.utilizationRate()

    def withdraw(self, nftId: int, withdrawAmount: int):
        return self.contract.functions.withdraw(nftId, withdrawAmount)
