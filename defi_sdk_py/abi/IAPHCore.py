
class IAPHCore:
    def __init__(self, contract_address, web3):
        """
        Initialize the contract instance.

        :param contract_address: The Ethereum address of the contract.
        :type contract_address: str
        :param web3: The Web3 instance for interacting with Ethereum.
        :type web3: Web3
        """
        self.contract:Web3.eth.contract = web3.eth.contract(address=contract_address, abi=[{'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralAdjustAmount', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'isAdd', 'type': 'bool'}], 'name': 'adjustCollateral', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'uint64', 'name': 'rolloverTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'owedPerDay', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwed', 'type': 'uint256'}], 'internalType': 'struct CoreBase.Loan', 'name': 'loan', 'type': 'tuple'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [], 'name': 'advancedInterestDuration', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'collateralSentAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'newOwedPerDay', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestRate', 'type': 'uint256'}], 'name': 'borrow', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'uint64', 'name': 'rolloverTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'owedPerDay', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwed', 'type': 'uint256'}], 'internalType': 'struct CoreBase.Loan', 'name': 'loan', 'type': 'tuple'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'newAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'tokenAddress', 'type': 'address'}], 'name': 'checkStakingAmountSufficient', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'posId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_closingSize', 'type': 'uint256'}], 'name': 'closePosition', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'currentLoanIndex', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'currentPositionIndex', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'underlyingTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'depositCollateral', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [], 'name': 'feeSpread', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'bool', 'name': 'isExactOutput', 'type': 'bool'}, {'internalType': 'bool', 'name': 'extractSwapFee', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'routerIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amountInput', 'type': 'uint256'}, {'internalType': 'address', 'name': 'src', 'type': 'address'}, {'internalType': 'address', 'name': 'dst', 'type': 'address'}], 'name': 'getAmounts', 'outputs': [{'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}, {'internalType': 'uint256', 'name': 'swapFee', 'type': 'uint256'}, {'internalType': 'address', 'name': 'router', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'bool', 'name': 'isExactOutput', 'type': 'bool'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'amountInput', 'type': 'uint256'}, {'internalType': 'address', 'name': 'src', 'type': 'address'}, {'internalType': 'address', 'name': 'dst', 'type': 'address'}, {'internalType': 'uint256', 'name': 'expectedRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'slippage', 'type': 'uint256'}], 'name': 'getAmountsWithRouterSelection', 'outputs': [{'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}, {'internalType': 'uint256', 'name': 'swapFee', 'type': 'uint256'}, {'internalType': 'address', 'name': 'router', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'getLoanCurrentLTV', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getPoolList', 'outputs': [{'internalType': 'address[]', 'name': 'poolList', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'bool', 'name': 'isLiquidate', 'type': 'bool'}], 'name': 'getPositionMargin', 'outputs': [{'internalType': 'uint256', 'name': 'margin', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'poolAddress', 'type': 'address'}], 'name': 'isPool', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'liquidate', 'outputs': [{'internalType': 'uint256', 'name': 'repayBorrow', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'repayInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'bountyReward', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'leftOverCollateral', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}], 'name': 'liquidatePosition', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'liquidationFee', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'loanDuration', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'loanExts', 'outputs': [{'components': [{'internalType': 'bool', 'name': 'active', 'type': 'bool'}, {'internalType': 'uint64', 'name': 'startTimestamp', 'type': 'uint64'}, {'internalType': 'uint256', 'name': 'initialBorrowTokenPrice', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'initialCollateralTokenPrice', 'type': 'uint256'}], 'internalType': 'struct CoreBase.LoanExt', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'loans', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'uint64', 'name': 'rolloverTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'owedPerDay', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwed', 'type': 'uint256'}], 'internalType': 'struct CoreBase.Loan', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'maximumLeverage', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'membershipAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'components': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'entryPrice', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'leverage', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'slipPage', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwePerDay', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'newLong', 'type': 'bool'}], 'internalType': 'struct APHLibrary.OpenPositionParams', 'name': 'params', 'type': 'tuple'}, {'components': [{'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'swapTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}], 'internalType': 'struct APHLibrary.TokenAddressParams', 'name': 'addressParams', 'type': 'tuple'}], 'name': 'openPosition', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}], 'name': 'pairs', 'outputs': [{'components': [{'internalType': 'address', 'name': 'pair0', 'type': 'address'}, {'internalType': 'address', 'name': 'pair1', 'type': 'address'}], 'internalType': 'struct CoreBase.Pair', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'posId', 'type': 'uint256'}], 'name': 'positionStates', 'outputs': [{'components': [{'internalType': 'bool', 'name': 'active', 'type': 'bool'}, {'internalType': 'bool', 'name': 'isLong', 'type': 'bool'}, {'internalType': 'int128', 'name': 'PNL', 'type': 'int128'}, {'internalType': 'uint64', 'name': 'startTimestamp', 'type': 'uint64'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'uint128', 'name': 'averageEntryPrice', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'interestPaid', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'totalTradingFee', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'totalSwapFee', 'type': 'uint128'}], 'internalType': 'struct CoreBase.PositionState', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}], 'name': 'positions', 'outputs': [{'components': [{'internalType': 'uint64', 'name': 'id', 'type': 'uint64'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'swapTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'entryPrice', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralSwappedAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwed', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwePerDay', 'type': 'uint256'}], 'internalType': 'struct CoreBase.Position', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'repayAmount', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'isOnlyInterest', 'type': 'bool'}], 'name': 'repay', 'outputs': [{'internalType': 'uint256', 'name': 'borrowPaid', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'rollover', 'outputs': [{'internalType': 'uint256', 'name': 'delayInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralBountyReward', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'settleBorrowInterest', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'routerAddress', 'type': 'address'}], 'name': 'swapFeeRates', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'tokenAddress', 'type': 'address'}], 'name': 'tokenPrecisionUnit', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}], 'name': 'wallets', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'underlyingTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'withdrawCollateral', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}])
        self.web3:Web3 = web3
        self.address = contract_address

    def __str__(self):
        return self.address

    # Generated functions
    
    def adjustCollateral(self, loanId: int, nftId: int, collateralAdjustAmount: int, isAdd: str):
        return self.contract.functions.adjustCollateral(loanId, nftId, collateralAdjustAmount, isAdd).call()

    def advancedInterestDuration(self, ):
        return self.contract.functions.advancedInterestDuration().call()

    def borrow(self, loanId: int, nftId: int, borrowAmount: int, borrowTokenAddress: str, collateralSentAmount: int, collateralTokenAddress: str, newOwedPerDay: int, interestRate: int):
        return self.contract.functions.borrow(loanId, nftId, borrowAmount, borrowTokenAddress, collateralSentAmount, collateralTokenAddress, newOwedPerDay, interestRate).call()

    def checkStakingAmountSufficient(self, nftId: int, newAmount: int, tokenAddress: str):
        return self.contract.functions.checkStakingAmountSufficient(nftId, newAmount, tokenAddress).call()

    def closePosition(self, nftId: int, posId: int, _closingSize: int):
        return self.contract.functions.closePosition(nftId, posId, _closingSize).call()

    def currentLoanIndex(self, nftId: int):
        return self.contract.functions.currentLoanIndex(nftId).call()

    def currentPositionIndex(self, nftId: int):
        return self.contract.functions.currentPositionIndex(nftId).call()

    def depositCollateral(self, nftId: int, collateralTokenAddress: str, underlyingTokenAddress: str, amount: int):
        return self.contract.functions.depositCollateral(nftId, collateralTokenAddress, underlyingTokenAddress, amount).call()

    def feeSpread(self, ):
        return self.contract.functions.feeSpread().call()

    def getAmounts(self, isExactOutput: str, extractSwapFee: str, routerIndex: int, amountInput: int, src: str, dst: str):
        return self.contract.functions.getAmounts(isExactOutput, extractSwapFee, routerIndex, amountInput, src, dst).call()

    def getAmountsWithRouterSelection(self, isExactOutput: str, pairByte: str, amountInput: int, src: str, dst: str, expectedRate: int, slippage: int):
        return self.contract.functions.getAmountsWithRouterSelection(isExactOutput, pairByte, amountInput, src, dst, expectedRate, slippage).call()

    def getLoanCurrentLTV(self, loanId: int, nftId: int):
        return self.contract.functions.getLoanCurrentLTV(loanId, nftId).call()

    def getPoolList(self, ):
        return self.contract.functions.getPoolList().call()

    def getPositionMargin(self, nftId: int, pairByte: str, isLiquidate: str):
        return self.contract.functions.getPositionMargin(nftId, pairByte, isLiquidate).call()

    def isPool(self, poolAddress: str):
        return self.contract.functions.isPool(poolAddress).call()

    def liquidate(self, loanId: int, nftId: int):
        return self.contract.functions.liquidate(loanId, nftId).call()

    def liquidatePosition(self, nftId: int, pairByte: str):
        return self.contract.functions.liquidatePosition(nftId, pairByte).call()

    def liquidationFee(self, ):
        return self.contract.functions.liquidationFee().call()

    def loanDuration(self, ):
        return self.contract.functions.loanDuration().call()

    def loanExts(self, nftId: int, loanId: int):
        return self.contract.functions.loanExts(nftId, loanId).call()

    def loans(self, nftId: int, loanId: int):
        return self.contract.functions.loans(nftId, loanId).call()

    def maximumLeverage(self, ):
        return self.contract.functions.maximumLeverage().call()

    def membershipAddress(self, ):
        return self.contract.functions.membershipAddress().call()

    def openPosition(self, params: str, addressParams: str):
        return self.contract.functions.openPosition(params, addressParams).call()

    def pairs(self, pairByte: str):
        return self.contract.functions.pairs(pairByte).call()

    def positionStates(self, nftId: int, posId: int):
        return self.contract.functions.positionStates(nftId, posId).call()

    def positions(self, nftId: int, pairByte: str):
        return self.contract.functions.positions(nftId, pairByte).call()

    def repay(self, loanId: int, nftId: int, repayAmount: int, isOnlyInterest: str):
        return self.contract.functions.repay(loanId, nftId, repayAmount, isOnlyInterest).call()

    def rollover(self, loanId: int, nftId: int):
        return self.contract.functions.rollover(loanId, nftId).call()

    def settleBorrowInterest(self, loanId: int, nftId: int):
        return self.contract.functions.settleBorrowInterest(loanId, nftId).call()

    def swapFeeRates(self, routerAddress: str):
        return self.contract.functions.swapFeeRates(routerAddress).call()

    def tokenPrecisionUnit(self, tokenAddress: str):
        return self.contract.functions.tokenPrecisionUnit(tokenAddress).call()

    def wallets(self, nftId: int, pairByte: str):
        return self.contract.functions.wallets(nftId, pairByte).call()

    def withdrawCollateral(self, nftId: int, collateralTokenAddress: str, underlyingTokenAddress: str, amount: int):
        return self.contract.functions.withdrawCollateral(nftId, collateralTokenAddress, underlyingTokenAddress, amount).call()
