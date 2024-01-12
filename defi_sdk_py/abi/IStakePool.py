
from web3 import Web3
from typing import Tuple, Dict, List
#Generate a Python class representing the Ethereum contract.
#:param abi: The ABI (Application Binary Interface) of the contract.
#:type abi: list
#:param contract_name: The name of the contract class default is MyContract.
#:type contract_name: str
#:return: The generated Python class code.
#:rtype: str

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




class IStakePool:
    def __init__(self, contract_address, web3):
        """
        Initialize the contract instance.

        :param contract_address: The Ethereum address of the contract.
        :type contract_address: str
        :param web3: The Web3 instance for interacting with Ethereum.
        :type web3: Web3
        """
        self.contract:Web3.eth.contract = web3.eth.contract(address=contract_address, abi=[{'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'Stake', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'Unstake', 'type': 'event'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'deprecateStakeInfo', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'getMaxLTVBonus', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'getStakeInfo', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'stakeBalance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'claimableAmount', 'type': 'uint256'}, {'internalType': 'uint64', 'name': 'startTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'endTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'uint256[]', 'name': 'payPattern', 'type': 'uint256[]'}], 'internalType': 'struct StakePoolBase.StakeInfo', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'migrate', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'stakeBalance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'claimableAmount', 'type': 'uint256'}, {'internalType': 'uint64', 'name': 'startTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'endTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'uint256[]', 'name': 'payPattern', 'type': 'uint256[]'}], 'internalType': 'struct StakePoolBase.StakeInfo', 'name': '', 'type': 'tuple'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'poolStartTimestamp', 'outputs': [{'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint8', 'name': 'rankNumber', 'type': 'uint8'}], 'name': 'rankInfos', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'interestBonusLending', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwardBonusLending', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minimumStakeAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxLTVBonus', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tradingFee', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tradingBonus', 'type': 'uint256'}], 'internalType': 'struct StakePoolBase.RankInfo', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'rankLen', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256[]', 'name': '_interestBonusLending', 'type': 'uint256[]'}, {'internalType': 'uint256[]', 'name': '_forwardBonusLending', 'type': 'uint256[]'}, {'internalType': 'uint256[]', 'name': '_minimumStakeAmount', 'type': 'uint256[]'}, {'internalType': 'uint256[]', 'name': '_maxLTVBonus', 'type': 'uint256[]'}, {'internalType': 'uint256[]', 'name': '_tradingFee', 'type': 'uint256[]'}, {'internalType': 'uint256[]', 'name': '_tradingBonus', 'type': 'uint256[]'}], 'name': 'setRankInfo', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'stake', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'stakeBalance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'claimableAmount', 'type': 'uint256'}, {'internalType': 'uint64', 'name': 'startTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'endTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'uint256[]', 'name': 'payPattern', 'type': 'uint256[]'}], 'internalType': 'struct StakePoolBase.StakeInfo', 'name': 'stakeInfo', 'type': 'tuple'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'stakeInfos', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'stakeBalance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'claimableAmount', 'type': 'uint256'}, {'internalType': 'uint64', 'name': 'startTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'endTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'uint256[]', 'name': 'payPattern', 'type': 'uint256[]'}], 'internalType': 'struct StakePoolBase.StakeInfo', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'totalStakeAmount', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'unstake', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'stakeBalance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'claimableAmount', 'type': 'uint256'}, {'internalType': 'uint64', 'name': 'startTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'endTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'uint256[]', 'name': 'payPattern', 'type': 'uint256[]'}], 'internalType': 'struct StakePoolBase.StakeInfo', 'name': 'stakeInfo', 'type': 'tuple'}], 'stateMutability': 'nonpayable', 'type': 'function'}])
        self.web3:Web3 = web3
        self.address = contract_address

    def __str__(self):
        return self.address

    # Generated functions
    
    def eventStake(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.Stake().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def eventUnstake(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.Unstake().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def deprecateStakeInfo(self, nftId: int):
        return self.contract.functions.deprecateStakeInfo(nftId)

    def getMaxLTVBonus(self, nftId: int):
        return self.contract.functions.getMaxLTVBonus(nftId)

    def getStakeInfo(self, nftId: int):
        return self.contract.functions.getStakeInfo(nftId)

    def migrate(self, nftId: int):
        return self.contract.functions.migrate(nftId)

    def poolStartTimestamp(self, ):
        return self.contract.functions.poolStartTimestamp()

    def rankInfos(self, rankNumber: int):
        return self.contract.functions.rankInfos(rankNumber)

    def rankLen(self, ):
        return self.contract.functions.rankLen()

    def setRankInfo(self, _interestBonusLending: int, _forwardBonusLending: int, _minimumStakeAmount: int, _maxLTVBonus: int, _tradingFee: int, _tradingBonus: int):
        return self.contract.functions.setRankInfo(_interestBonusLending, _forwardBonusLending, _minimumStakeAmount, _maxLTVBonus, _tradingFee, _tradingBonus)

    def stake(self, nftId: int, amount: int):
        return self.contract.functions.stake(nftId, amount)

    def stakeInfos(self, nftId: int):
        return self.contract.functions.stakeInfos(nftId)

    def totalStakeAmount(self, ):
        return self.contract.functions.totalStakeAmount()

    def unstake(self, nftId: int, amount: int):
        return self.contract.functions.unstake(nftId, amount)
