
class IAPHPool:
    def __init__(self, contract_address, web3):
        """
        Initialize the contract instance.

        :param contract_address: The Ethereum address of the contract.
        :type contract_address: str
        :param web3: The Web3 instance for interacting with Ethereum.
        :type web3: Web3
        """
        self.contract:Web3.eth.contract = web3.eth.contract(address=contract_address, abi=[{'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'oldRank', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint8', 'name': 'newRank', 'type': 'uint8'}], 'name': 'ActivateRank', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'indexed': True, 'internalType': 'address', 'name': 'tokenAddress', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'isTrading', 'type': 'bool'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'Borrow', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'interestForwClaimed', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'interestForwBonus', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'burnedIfp', 'type': 'uint256'}], 'name': 'ClaimForwInterest', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'interestTokenClaimed', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'interestTokenBonus', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'burnedItp', 'type': 'uint256'}], 'name': 'ClaimTokenInterest', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'depositAmount', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'mintedP', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'mintedAtp', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'mintedItp', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'mintedIfp', 'type': 'uint256'}], 'name': 'Deposit', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'withdrawAmount', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'burnedP', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'burnedAtp', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'burnedLoss', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'burnedItp', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'burnedIfp', 'type': 'uint256'}], 'name': 'Withdraw', 'type': 'event'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'activateRank', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'addLoss', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'atpTokenTotalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'balanceAtpTokenOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'balanceIfpTokenOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'balanceItpTokenOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'balancePTokenOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralSentAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}], 'name': 'borrow', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'uint64', 'name': 'rolloverTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'owedPerDay', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwed', 'type': 'uint256'}], 'internalType': 'struct CoreBase.Loan', 'name': '', 'type': 'tuple'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}], 'name': 'calculateInterest', 'outputs': [{'internalType': 'uint256', 'name': 'interestRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwedPerDay', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'claimAllInterest', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'principle', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'pTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'atpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lossBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'itpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ifpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterestBonus', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterestBonus', 'type': 'uint256'}], 'internalType': 'struct PoolBase.WithdrawResult', 'name': '', 'type': 'tuple'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'claimAmount', 'type': 'uint256'}], 'name': 'claimForwInterest', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'principle', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'pTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'atpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lossBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'itpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ifpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterestBonus', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterestBonus', 'type': 'uint256'}], 'internalType': 'struct PoolBase.WithdrawResult', 'name': '', 'type': 'tuple'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'claimAmount', 'type': 'uint256'}], 'name': 'claimTokenInterest', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'principle', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'pTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'atpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lossBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'itpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ifpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterestBonus', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterestBonus', 'type': 'uint256'}], 'internalType': 'struct PoolBase.WithdrawResult', 'name': '', 'type': 'tuple'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'coreAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'currentSupply', 'outputs': [{'internalType': 'uint256', 'name': '_currentSupply', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'depositAmount', 'type': 'uint256'}], 'name': 'deposit', 'outputs': [{'internalType': 'uint256', 'name': 'mintedP', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'mintedItp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'mintedIfp', 'type': 'uint256'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [], 'name': 'getActualTokenPrice', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getInterestForwPrice', 'outputs': [{'internalType': 'uint256', 'name': 'ifpPrice', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getInterestTokenPrice', 'outputs': [{'internalType': 'uint256', 'name': 'itpPrice', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}], 'name': 'getNextBorrowingInterest', 'outputs': [{'internalType': 'uint256', 'name': 'nextInterestRate', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getRates', 'outputs': [{'internalType': 'uint256[10]', 'name': '', 'type': 'uint256[10]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getUtils', 'outputs': [{'internalType': 'uint256[10]', 'name': '', 'type': 'uint256[10]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'ifpTokenTotalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'itpTokenTotalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'NFTId', 'type': 'uint256'}], 'name': 'lenders', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}, {'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'membershipAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'swapTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'entryPrice', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'leverage', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'slippage', 'type': 'uint256'}], 'name': 'openPosition', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'pTokenTotalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'tokenAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'tokenHolders', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'pToken', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'atpToken', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'itpToken', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ifpToken', 'type': 'uint256'}], 'internalType': 'struct PoolToken.PoolTokens', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'utilizationRate', 'outputs': [{'internalType': 'uint256', 'name': '_utilizationRate', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'withdrawAmount', 'type': 'uint256'}], 'name': 'withdraw', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'principle', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'pTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'atpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lossBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'itpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ifpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterestBonus', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterestBonus', 'type': 'uint256'}], 'internalType': 'struct PoolBase.WithdrawResult', 'name': '', 'type': 'tuple'}], 'stateMutability': 'nonpayable', 'type': 'function'}])
        self.web3:Web3 = web3
        self.address = contract_address

    def __str__(self):
        return self.address

    # Generated functions
    
    def eventActivateRank(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.ActivateRank().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def eventBorrow(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.Borrow().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def eventClaimForwInterest(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.ClaimForwInterest().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def eventClaimTokenInterest(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.ClaimTokenInterest().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def eventDeposit(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.Deposit().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def eventWithdraw(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.Withdraw().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def activateRank(self, nftId: int):
        return self.contract.functions.activateRank(nftId).call()

    def addLoss(self, amount: int):
        return self.contract.functions.addLoss(amount).call()

    def atpTokenTotalSupply(self, ):
        return self.contract.functions.atpTokenTotalSupply().call()

    def balanceAtpTokenOf(self, nftId: int):
        return self.contract.functions.balanceAtpTokenOf(nftId).call()

    def balanceIfpTokenOf(self, nftId: int):
        return self.contract.functions.balanceIfpTokenOf(nftId).call()

    def balanceItpTokenOf(self, nftId: int):
        return self.contract.functions.balanceItpTokenOf(nftId).call()

    def balancePTokenOf(self, nftId: int):
        return self.contract.functions.balancePTokenOf(nftId).call()

    def borrow(self, loanId: int, nftId: int, borrowAmount: int, collateralSentAmount: int, collateralTokenAddress: str):
        return self.contract.functions.borrow(loanId, nftId, borrowAmount, collateralSentAmount, collateralTokenAddress).call()

    def calculateInterest(self, borrowAmount: int):
        return self.contract.functions.calculateInterest(borrowAmount).call()

    def claimAllInterest(self, nftId: int):
        return self.contract.functions.claimAllInterest(nftId).call()

    def claimForwInterest(self, nftId: int, claimAmount: int):
        return self.contract.functions.claimForwInterest(nftId, claimAmount).call()

    def claimTokenInterest(self, nftId: int, claimAmount: int):
        return self.contract.functions.claimTokenInterest(nftId, claimAmount).call()

    def coreAddress(self, ):
        return self.contract.functions.coreAddress().call()

    def currentSupply(self, ):
        return self.contract.functions.currentSupply().call()

    def deposit(self, nftId: int, depositAmount: int):
        return self.contract.functions.deposit(nftId, depositAmount).call()

    def getActualTokenPrice(self, ):
        return self.contract.functions.getActualTokenPrice().call()

    def getInterestForwPrice(self, ):
        return self.contract.functions.getInterestForwPrice().call()

    def getInterestTokenPrice(self, ):
        return self.contract.functions.getInterestTokenPrice().call()

    def getNextBorrowingInterest(self, borrowAmount: int):
        return self.contract.functions.getNextBorrowingInterest(borrowAmount).call()

    def getRates(self, ):
        return self.contract.functions.getRates().call()

    def getUtils(self, ):
        return self.contract.functions.getUtils().call()

    def ifpTokenTotalSupply(self, ):
        return self.contract.functions.ifpTokenTotalSupply().call()

    def itpTokenTotalSupply(self, ):
        return self.contract.functions.itpTokenTotalSupply().call()

    def lenders(self, NFTId: int):
        return self.contract.functions.lenders(NFTId).call()

    def membershipAddress(self, ):
        return self.contract.functions.membershipAddress().call()

    def openPosition(self, nftId: int, collateralTokenAddress: str, swapTokenAddress: str, entryPrice: int, contractSize: int, leverage: int, slippage: int):
        return self.contract.functions.openPosition(nftId, collateralTokenAddress, swapTokenAddress, entryPrice, contractSize, leverage, slippage).call()

    def pTokenTotalSupply(self, ):
        return self.contract.functions.pTokenTotalSupply().call()

    def tokenAddress(self, ):
        return self.contract.functions.tokenAddress().call()

    def tokenHolders(self, nftId: int):
        return self.contract.functions.tokenHolders(nftId).call()

    def utilizationRate(self, ):
        return self.contract.functions.utilizationRate().call()

    def withdraw(self, nftId: int, withdrawAmount: int):
        return self.contract.functions.withdraw(nftId, withdrawAmount).call()
