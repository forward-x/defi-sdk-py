
class IAPHPool:
    def __init__(self, contract_address, web3):
        """
        Initialize the contract instance.

        :param contract_address: The Ethereum address of the contract.
        :type contract_address: str
        :param web3: The Web3 instance for interacting with Ethereum.
        :type web3: Web3
        """
        self.contract = web3.eth.contract(address=contract_address, abi=[{'inputs': [], 'name': 'BLOCK_TIME', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'activateRank', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'addLoss', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'atpTokenTotalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'NFTId', 'type': 'uint256'}], 'name': 'balanceAtpTokenOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'NFTId', 'type': 'uint256'}], 'name': 'balanceIfpTokenOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'NFTId', 'type': 'uint256'}], 'name': 'balanceItpTokenOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'NFTId', 'type': 'uint256'}], 'name': 'balancePTokenOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralSentAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}], 'name': 'borrow', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'uint64', 'name': 'rolloverTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'owedPerDay', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwed', 'type': 'uint256'}], 'internalType': 'struct CoreBase.Loan', 'name': '', 'type': 'tuple'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}], 'name': 'calculateInterest', 'outputs': [{'internalType': 'uint256', 'name': 'interestRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwedPerDay', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'claimAllInterest', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'principle', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'pTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'atpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lossBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'itpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ifpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterestBonus', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterestBonus', 'type': 'uint256'}], 'internalType': 'struct PoolBase.WithdrawResult', 'name': '', 'type': 'tuple'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'claimAmount', 'type': 'uint256'}], 'name': 'claimForwInterest', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'principle', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'pTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'atpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lossBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'itpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ifpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterestBonus', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterestBonus', 'type': 'uint256'}], 'internalType': 'struct PoolBase.WithdrawResult', 'name': '', 'type': 'tuple'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'claimAmount', 'type': 'uint256'}], 'name': 'claimTokenInterest', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'principle', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'pTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'atpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lossBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'itpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ifpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterestBonus', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterestBonus', 'type': 'uint256'}], 'internalType': 'struct PoolBase.WithdrawResult', 'name': '', 'type': 'tuple'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'coreAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'currentSupply', 'outputs': [{'internalType': 'uint256', 'name': '_currentSupply', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'depositAmount', 'type': 'uint256'}], 'name': 'deposit', 'outputs': [
                                          {'internalType': 'uint256', 'name': 'mintedP', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'mintedItp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'mintedIfp', 'type': 'uint256'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [], 'name': 'forwAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getActualTokenPrice', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getInterestForwPrice', 'outputs': [{'internalType': 'uint256', 'name': 'ifpPrice', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getInterestTokenPrice', 'outputs': [{'internalType': 'uint256', 'name': 'itpPrice', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}], 'name': 'getNextBorrowingInterest', 'outputs': [{'internalType': 'uint256', 'name': 'nextInterestRate', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getRates', 'outputs': [{'internalType': 'uint256[10]', 'name': '', 'type': 'uint256[10]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getUtils', 'outputs': [{'internalType': 'uint256[10]', 'name': '', 'type': 'uint256[10]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'ifpTokenTotalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'interestVaultAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'itpTokenTotalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'lambda', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'NFTId', 'type': 'uint256'}], 'name': 'lenders', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}, {'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'loss', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'membershipAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'swapTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'entryPrice', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'leverage', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'slippage', 'type': 'uint256'}], 'name': 'openPosition', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'pTokenTotalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'bytes4', 'name': '_func', 'type': 'bytes4'}], 'name': 'pause', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'poolBorrowingAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'poolLendingAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'rates', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'targetSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'tokenAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'tokenHolders', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'pToken', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'atpToken', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'itpToken', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ifpToken', 'type': 'uint256'}], 'internalType': 'struct PoolToken.PoolTokens', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'bytes4', 'name': '_func', 'type': 'bytes4'}], 'name': 'unPause', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'utilizationRate', 'outputs': [{'internalType': 'uint256', 'name': '_utilizationRate', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'utils', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'utilsLen', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'withdrawAmount', 'type': 'uint256'}], 'name': 'withdraw', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'principle', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'pTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'atpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lossBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'itpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'ifpTokenBurn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'tokenInterestBonus', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwInterestBonus', 'type': 'uint256'}], 'internalType': 'struct PoolBase.WithdrawResult', 'name': '', 'type': 'tuple'}], 'stateMutability': 'nonpayable', 'type': 'function'}])

    # Generated functions

    def BLOCK_TIME(self):
        return self.contract.functions.BLOCK_TIME().call()

    def activateRank(self, nftId):
        return self.contract.functions.activateRank(nftId).call()

    def addLoss(self, amount):
        return self.contract.functions.addLoss(amount).call()

    def atpTokenTotalSupply(self):
        return self.contract.functions.atpTokenTotalSupply().call()

    def balanceAtpTokenOf(self, NFTId):
        return self.contract.functions.balanceAtpTokenOf(NFTId).call()

    def balanceIfpTokenOf(self, NFTId):
        return self.contract.functions.balanceIfpTokenOf(NFTId).call()

    def balanceItpTokenOf(self, NFTId):
        return self.contract.functions.balanceItpTokenOf(NFTId).call()

    def balancePTokenOf(self, NFTId):
        return self.contract.functions.balancePTokenOf(NFTId).call()

    def borrow(self, loanId, nftId, borrowAmount, collateralSentAmount, collateralTokenAddress):
        return self.contract.functions.borrow(loanId, nftId, borrowAmount, collateralSentAmount, collateralTokenAddress).call()

    def calculateInterest(self, borrowAmount):
        return self.contract.functions.calculateInterest(borrowAmount).call()

    def claimAllInterest(self, nftId):
        return self.contract.functions.claimAllInterest(nftId).call()

    def claimForwInterest(self, nftId, claimAmount):
        return self.contract.functions.claimForwInterest(nftId, claimAmount).call()

    def claimTokenInterest(self, nftId, claimAmount):
        return self.contract.functions.claimTokenInterest(nftId, claimAmount).call()

    def coreAddress(self):
        return self.contract.functions.coreAddress().call()

    def currentSupply(self):
        return self.contract.functions.currentSupply().call()

    def deposit(self, nftId, depositAmount):
        return self.contract.functions.deposit(nftId, depositAmount).call()

    def forwAddress(self):
        return self.contract.functions.forwAddress().call()

    def getActualTokenPrice(self):
        return self.contract.functions.getActualTokenPrice().call()

    def getInterestForwPrice(self):
        return self.contract.functions.getInterestForwPrice().call()

    def getInterestTokenPrice(self):
        return self.contract.functions.getInterestTokenPrice().call()

    def getNextBorrowingInterest(self, borrowAmount):
        return self.contract.functions.getNextBorrowingInterest(borrowAmount).call()

    def getRates(self):
        return self.contract.functions.getRates().call()

    def getUtils(self):
        return self.contract.functions.getUtils().call()

    def ifpTokenTotalSupply(self):
        return self.contract.functions.ifpTokenTotalSupply().call()

    def interestVaultAddress(self):
        return self.contract.functions.interestVaultAddress().call()

    def itpTokenTotalSupply(self):
        return self.contract.functions.itpTokenTotalSupply().call()

    def lenders(self, NFTId):
        return self.contract.functions.lenders(NFTId).call()

    def loss(self):
        return self.contract.functions.loss().call()

    def membershipAddress(self):
        return self.contract.functions.membershipAddress().call()

    def openPosition(self, nftId, collateralTokenAddress, swapTokenAddress, entryPrice, contractSize, leverage, slippage):
        return self.contract.functions.openPosition(nftId, collateralTokenAddress, swapTokenAddress, entryPrice, contractSize, leverage, slippage).call()

    def pTokenTotalSupply(self):
        return self.contract.functions.pTokenTotalSupply().call()

    def pause(self, _func):
        return self.contract.functions.pause(_func).call()

    def poolBorrowingAddress(self):
        return self.contract.functions.poolBorrowingAddress().call()

    def poolLendingAddress(self):
        return self.contract.functions.poolLendingAddress().call()

    def rates(self, arg0):
        return self.contract.functions.rates(arg0).call()

    def targetSupply(self):
        return self.contract.functions.targetSupply().call()

    def tokenAddress(self):
        return self.contract.functions.tokenAddress().call()

    def tokenHolders(self, nftId):
        return self.contract.functions.tokenHolders(nftId).call()

    def unPause(self, _func):
        return self.contract.functions.unPause(_func).call()

    def utilizationRate(self):
        return self.contract.functions.utilizationRate().call()

    def utils(self, arg0):
        return self.contract.functions.utils(arg0).call()

    def utilsLen(self):
        return self.contract.functions.utilsLen().call()

    def withdraw(self, nftId, withdrawAmount):
        return self.contract.functions.withdraw(nftId, withdrawAmount).call()
