
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


class StakeInfo:
    def __init__(self, stakeBalance: int, claimableAmount: int, startTimestamp: int, endTimestamp: int, lastSettleTimestamp: int, payPattern: int):
        self.stakeBalance = stakeBalance
        self.claimableAmount = claimableAmount
        self.startTimestamp = startTimestamp
        self.endTimestamp = endTimestamp
        self.lastSettleTimestamp = lastSettleTimestamp
        self.payPattern = payPattern

    def __str__(self):
        return str({
            'stakeBalance': self.stakeBalance,
            'claimableAmount': self.claimableAmount,
            'startTimestamp': self.startTimestamp,
            'endTimestamp': self.endTimestamp,
            'lastSettleTimestamp': self.lastSettleTimestamp,
            'payPattern': self.payPattern,
        })




class IHelperMembershipAndStakePool:
    def __init__(self, contract_address, web3):
        """
        Initialize the contract instance.

        :param contract_address: The Ethereum address of the contract.
        :type contract_address: str
        :param web3: The Web3 instance for interacting with Ethereum.
        :type web3: Web3
        """
        self.contract:Web3.eth.contract = web3.eth.contract(address=contract_address, abi=[{'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'getNFTList', 'outputs': [{'internalType': 'uint256', 'name': 'count', 'type': 'uint256'}, {'internalType': 'uint256[]', 'name': 'nftList', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getRankInfoList', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'interestBonusLending', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwardBonusLending', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minimumStakeAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxLTVBonus', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tradingFee', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tradingBonus', 'type': 'uint256'}], 'internalType': 'struct StakePoolBase.RankInfo[]', 'name': 'rankInfos', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'getStakeInfo', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'stakeBalance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'claimableAmount', 'type': 'uint256'}, {'internalType': 'uint64', 'name': 'startTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'endTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'uint256[]', 'name': 'payPattern', 'type': 'uint256[]'}], 'internalType': 'struct StakePoolBase.StakeInfo', 'name': 'stakeInfo', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'stakePoolAddress', 'type': 'address'}], 'name': 'getStakePoolNextSettleTimeStamp', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}])
        self.web3:Web3 = web3
        self.address = contract_address

    def __str__(self):
        return self.address

    # Generated functions
    
    def getNFTList(self, owner: str):
        return self.contract.functions.getNFTList(owner)

    def getRankInfoList(self, ):
        return self.contract.functions.getRankInfoList()

    def getStakeInfo(self, nftId: int):
        return self.contract.functions.getStakeInfo(nftId)

    def getStakePoolNextSettleTimeStamp(self, stakePoolAddress: str):
        return self.contract.functions.getStakePoolNextSettleTimeStamp(stakePoolAddress)
