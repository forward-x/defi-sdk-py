
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
        return self.contract.functions.deprecateStakeInfo(nftId).call()

    def getMaxLTVBonus(self, nftId: int):
        return self.contract.functions.getMaxLTVBonus(nftId).call()

    def getStakeInfo(self, nftId: int):
        return self.contract.functions.getStakeInfo(nftId).call()

    def migrate(self, nftId: int):
        return self.contract.functions.migrate(nftId).call()

    def poolStartTimestamp(self, ):
        return self.contract.functions.poolStartTimestamp().call()

    def rankInfos(self, rankNumber: int):
        return self.contract.functions.rankInfos(rankNumber).call()

    def rankLen(self, ):
        return self.contract.functions.rankLen().call()

    def setRankInfo(self, _interestBonusLending: int, _forwardBonusLending: int, _minimumStakeAmount: int, _maxLTVBonus: int, _tradingFee: int, _tradingBonus: int):
        return self.contract.functions.setRankInfo(_interestBonusLending, _forwardBonusLending, _minimumStakeAmount, _maxLTVBonus, _tradingFee, _tradingBonus).call()

    def stake(self, nftId: int, amount: int):
        return self.contract.functions.stake(nftId, amount).call()

    def stakeInfos(self, nftId: int):
        return self.contract.functions.stakeInfos(nftId).call()

    def totalStakeAmount(self, ):
        return self.contract.functions.totalStakeAmount().call()

    def unstake(self, nftId: int, amount: int):
        return self.contract.functions.unstake(nftId, amount).call()
