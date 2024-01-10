
class IAPHCore:
    def __init__(self, contract_address, web3):
        """
        Initialize the contract instance.

        :param contract_address: The Ethereum address of the contract.
        :type contract_address: str
        :param web3: The Web3 instance for interacting with Ethereum.
        :type web3: Web3
        """
        self.contract = web3.eth.contract(address=contract_address, abi=[{'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lossAmount', 'type': 'uint256'}], 'name': 'addLossInUSD', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralAdjustAmount', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'isAdd', 'type': 'bool'}], 'name': 'adjustCollateral', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'uint64', 'name': 'rolloverTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'owedPerDay', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwed', 'type': 'uint256'}], 'internalType': 'struct CoreBase.Loan', 'name': 'loan', 'type': 'tuple'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [], 'name': 'advancedInterestDuration', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'assetToPool', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'auctionSpread', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'collateralSentAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'newOwedPerDay', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestRate', 'type': 'uint256'}], 'name': 'borrow', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'uint64', 'name': 'rolloverTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'owedPerDay', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwed', 'type': 'uint256'}], 'internalType': 'struct CoreBase.Loan', 'name': 'loan', 'type': 'tuple'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'newAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'tokenAddress', 'type': 'address'}], 'name': 'checkStakingAmountSufficient', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'posId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_closingSize', 'type': 'uint256'}], 'name': 'closePosition', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'coreBorrowingAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'coreFutureClosingAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'coreFutureOpeningAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'coreFutureWalletAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'coreSettingAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'coreSwappingAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'currentLoanIndex', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'currentPositionIndex', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'underlyingTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'depositCollateral', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [], 'name': 'feeSpread', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'feeVaultAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'forwAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'forwLendingDistributionPerBlock', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'forwLendingVaultAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'forwStakingMultiplier', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'forwTradingVaultAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'bool', 'name': 'isExactOutput', 'type': 'bool'}, {'internalType': 'bool', 'name': 'extractSwapFee', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'routerIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amountInput', 'type': 'uint256'}, {'internalType': 'address', 'name': 'src', 'type': 'address'}, {'internalType': 'address', 'name': 'dst', 'type': 'address'}], 'name': 'getAmounts', 'outputs': [{'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}, {'internalType': 'uint256', 'name': 'swapFee', 'type': 'uint256'}, {'internalType': 'address', 'name': 'router', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'bool', 'name': 'isExactOutput', 'type': 'bool'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'amountInput', 'type': 'uint256'}, {'internalType': 'address', 'name': 'src', 'type': 'address'}, {'internalType': 'address', 'name': 'dst', 'type': 'address'}, {'internalType': 'uint256', 'name': 'expectedRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'slippage', 'type': 'uint256'}], 'name': 'getAmountsWithRouterSelection', 'outputs': [{'internalType': 'uint256[]', 'name': 'amounts', 'type': 'uint256[]'}, {'internalType': 'uint256', 'name': 'swapFee', 'type': 'uint256'}, {'internalType': 'address', 'name': 'router', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'getLoanCurrentLTV', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getPoolList', 'outputs': [{'internalType': 'address[]', 'name': '', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'bool', 'name': 'isLiquidate', 'type': 'bool'}], 'name': 'getPositionMargin', 'outputs': [{'internalType': 'uint256', 'name': 'margin', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getRouters', 'outputs': [{'internalType': 'address[5]', 'name': '', 'type': 'address[5]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'poolAddress', 'type': 'address'}], 'name': 'isPool', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'lastSettleForw', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'liquidate', 'outputs': [{'internalType': 'uint256', 'name': 'repayBorrow', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'repayInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'bountyReward', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'leftOverCollateral', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}], 'name': 'liquidatePosition', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'liquidationFee', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'loanConfigs', 'outputs': [{'components': [{'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'safeLTV', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxLTV', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'liquidationLTV', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'bountyFeeRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'penaltyFeeRate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxOraclePriceDiffPercent', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxLiquidationOraclePriceDiffPercent', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minimumCollateralInUSD', 'type': 'uint256'}], 'internalType': 'struct CoreBase.LoanConfig', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'loanDuration', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'loanExts', 'outputs': [{'components': [{'internalType': 'bool', 'name': 'active', 'type': 'bool'}, {'internalType': 'uint64', 'name': 'startTimestamp', 'type': 'uint64'}, {'internalType': 'uint256', 'name': 'initialBorrowTokenPrice', 'type': 'uint256'}, {
                                          'internalType': 'uint256', 'name': 'initialCollateralTokenPrice', 'type': 'uint256'}], 'internalType': 'struct CoreBase.LoanExt', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'loans', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'uint64', 'name': 'rolloverTimestamp', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'owedPerDay', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwed', 'type': 'uint256'}], 'internalType': 'struct CoreBase.Loan', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'maximumLeverage', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'membershipAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'nextForwLendingDistributionPerBlock', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'targetBlock', 'type': 'uint256'}], 'internalType': 'struct CoreBase.NextForwLendingDistributionPerBlock', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'nftsLossInUSD', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'components': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'entryPrice', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'leverage', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'slipPage', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwePerDay', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'newLong', 'type': 'bool'}], 'internalType': 'struct APHLibrary.OpenPositionParams', 'name': 'params', 'type': 'tuple'}, {'components': [{'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'swapTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}], 'internalType': 'struct APHLibrary.TokenAddressParams', 'name': 'addressParams', 'type': 'tuple'}], 'name': 'openPosition', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'pairs', 'outputs': [{'components': [{'internalType': 'address', 'name': 'pair0', 'type': 'address'}, {'internalType': 'address', 'name': 'pair1', 'type': 'address'}], 'internalType': 'struct CoreBase.Pair', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'bytes4', 'name': '_func', 'type': 'bytes4'}], 'name': 'pause', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'poolList', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'poolStats', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'totalBorrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'borrowInterestOwedPerDay', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'totalInterestPaid', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'totalBorrowAmountFromTrading', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'borrowInterestOwedPerDayFromTrading', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'totalInterestPaidFromTrading', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'updatedTimestamp', 'type': 'uint256'}], 'internalType': 'struct CoreBase.PoolStat', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'poolToAsset', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'positionConfigs', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'maintenanceMargin', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minimumMargin', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'bountyFeeRateToProtocol', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'bountyFeeRateToLiquidator', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'forwRewardAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'positionSizeTargetInUSD', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minOpenPositionSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxOpenPositionSize', 'type': 'uint256'}], 'internalType': 'struct CoreBase.PositionConfig', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'positionStates', 'outputs': [{'components': [{'internalType': 'bool', 'name': 'active', 'type': 'bool'}, {'internalType': 'bool', 'name': 'isLong', 'type': 'bool'}, {'internalType': 'int128', 'name': 'PNL', 'type': 'int128'}, {'internalType': 'uint64', 'name': 'startTimestamp', 'type': 'uint64'}, {'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}, {'internalType': 'uint128', 'name': 'averageEntryPrice', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'interestPaid', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'totalTradingFee', 'type': 'uint128'}, {'internalType': 'uint128', 'name': 'totalSwapFee', 'type': 'uint128'}], 'internalType': 'struct CoreBase.PositionState', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'positions', 'outputs': [{'components': [{'internalType': 'uint64', 'name': 'id', 'type': 'uint64'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'uint64', 'name': 'lastSettleTimestamp', 'type': 'uint64'}, {'internalType': 'address', 'name': 'borrowTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'swapTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'entryPrice', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'contractSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'borrowAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralSwappedAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwed', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwePerDay', 'type': 'uint256'}], 'internalType': 'struct CoreBase.Position', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'priceFeedAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'repayAmount', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'isOnlyInterest', 'type': 'bool'}], 'name': 'repay', 'outputs': [{'internalType': 'uint256', 'name': 'borrowPaid', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'rollover', 'outputs': [{'internalType': 'uint256', 'name': 'delayInterest', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'collateralBountyReward', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'routers', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}], 'name': 'settleBorrowInterest', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'settleForwInterest', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'swapConfigs', 'outputs': [{'components': [{'internalType': 'address', 'name': 'token0', 'type': 'address'}, {'internalType': 'uint256', 'name': 'maxSwapSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxPriceImpact', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxOraclePriceDiffPercent', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxLiquidationOraclePriceDiffPercent', 'type': 'uint256'}], 'internalType': 'struct CoreBase.SwapConfig', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'swapFeeRates', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'swapableToken', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'tokenPrecisionUnit', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'totalCollateralHold', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'totalLossInUSD', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'tradingCollateralWhitelist', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'tradingFeeToLender', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'bytes4', 'name': '_func', 'type': 'bytes4'}], 'name': 'unPause', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'wallets', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'wethHandler', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'nftId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'underlyingTokenAddress', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'withdrawCollateral', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}])

    # Generated functions

    def addLossInUSD(self, nftId, lossAmount):
        return self.contract.functions.addLossInUSD(nftId, lossAmount).call()

    def adjustCollateral(self, loanId, nftId, collateralAdjustAmount, isAdd):
        return self.contract.functions.adjustCollateral(loanId, nftId, collateralAdjustAmount, isAdd).call()

    def advancedInterestDuration(self):
        return self.contract.functions.advancedInterestDuration().call()

    def assetToPool(self, arg0):
        return self.contract.functions.assetToPool(arg0).call()

    def auctionSpread(self):
        return self.contract.functions.auctionSpread().call()

    def borrow(self, loanId, nftId, borrowAmount, borrowTokenAddress, collateralSentAmount, collateralTokenAddress, newOwedPerDay, interestRate):
        return self.contract.functions.borrow(loanId, nftId, borrowAmount, borrowTokenAddress, collateralSentAmount, collateralTokenAddress, newOwedPerDay, interestRate).call()

    def checkStakingAmountSufficient(self, nftId, newAmount, tokenAddress):
        return self.contract.functions.checkStakingAmountSufficient(nftId, newAmount, tokenAddress).call()

    def closePosition(self, nftId, posId, _closingSize):
        return self.contract.functions.closePosition(nftId, posId, _closingSize).call()

    def coreBorrowingAddress(self):
        return self.contract.functions.coreBorrowingAddress().call()

    def coreFutureClosingAddress(self):
        return self.contract.functions.coreFutureClosingAddress().call()

    def coreFutureOpeningAddress(self):
        return self.contract.functions.coreFutureOpeningAddress().call()

    def coreFutureWalletAddress(self):
        return self.contract.functions.coreFutureWalletAddress().call()

    def coreSettingAddress(self):
        return self.contract.functions.coreSettingAddress().call()

    def coreSwappingAddress(self):
        return self.contract.functions.coreSwappingAddress().call()

    def currentLoanIndex(self, arg0):
        return self.contract.functions.currentLoanIndex(arg0).call()

    def currentPositionIndex(self, arg0):
        return self.contract.functions.currentPositionIndex(arg0).call()

    def depositCollateral(self, nftId, collateralTokenAddress, underlyingTokenAddress, amount):
        return self.contract.functions.depositCollateral(nftId, collateralTokenAddress, underlyingTokenAddress, amount).call()

    def feeSpread(self):
        return self.contract.functions.feeSpread().call()

    def feeVaultAddress(self):
        return self.contract.functions.feeVaultAddress().call()

    def forwAddress(self):
        return self.contract.functions.forwAddress().call()

    def forwLendingDistributionPerBlock(self, arg0):
        return self.contract.functions.forwLendingDistributionPerBlock(arg0).call()

    def forwLendingVaultAddress(self):
        return self.contract.functions.forwLendingVaultAddress().call()

    def forwStakingMultiplier(self):
        return self.contract.functions.forwStakingMultiplier().call()

    def forwTradingVaultAddress(self):
        return self.contract.functions.forwTradingVaultAddress().call()

    def getAmounts(self, isExactOutput, extractSwapFee, routerIndex, amountInput, src, dst):
        return self.contract.functions.getAmounts(isExactOutput, extractSwapFee, routerIndex, amountInput, src, dst).call()

    def getAmountsWithRouterSelection(self, isExactOutput, pairByte, amountInput, src, dst, expectedRate, slippage):
        return self.contract.functions.getAmountsWithRouterSelection(isExactOutput, pairByte, amountInput, src, dst, expectedRate, slippage).call()

    def getLoanCurrentLTV(self, loanId, nftId):
        return self.contract.functions.getLoanCurrentLTV(loanId, nftId).call()

    def getPoolList(self):
        return self.contract.functions.getPoolList().call()

    def getPositionMargin(self, nftId, pairByte, isLiquidate):
        return self.contract.functions.getPositionMargin(nftId, pairByte, isLiquidate).call()

    def getRouters(self):
        return self.contract.functions.getRouters().call()

    def isPool(self, poolAddress):
        return self.contract.functions.isPool(poolAddress).call()

    def lastSettleForw(self, arg0):
        return self.contract.functions.lastSettleForw(arg0).call()

    def liquidate(self, loanId, nftId):
        return self.contract.functions.liquidate(loanId, nftId).call()

    def liquidatePosition(self, nftId, pairByte):
        return self.contract.functions.liquidatePosition(nftId, pairByte).call()

    def liquidationFee(self):
        return self.contract.functions.liquidationFee().call()

    def loanConfigs(self, arg0, arg1):
        return self.contract.functions.loanConfigs(arg0, arg1).call()

    def loanDuration(self):
        return self.contract.functions.loanDuration().call()

    def loanExts(self, arg0, arg1):
        return self.contract.functions.loanExts(arg0, arg1).call()

    def loans(self, arg0, arg1):
        return self.contract.functions.loans(arg0, arg1).call()

    def maximumLeverage(self):
        return self.contract.functions.maximumLeverage().call()

    def membershipAddress(self):
        return self.contract.functions.membershipAddress().call()

    def nextForwLendingDistributionPerBlock(self, arg0):
        return self.contract.functions.nextForwLendingDistributionPerBlock(arg0).call()

    def nftsLossInUSD(self, nftId):
        return self.contract.functions.nftsLossInUSD(nftId).call()

    def openPosition(self, params, addressParams):
        return self.contract.functions.openPosition(params, addressParams).call()

    def pairs(self, arg0):
        return self.contract.functions.pairs(arg0).call()

    def pause(self, _func):
        return self.contract.functions.pause(_func).call()

    def poolList(self, arg0):
        return self.contract.functions.poolList(arg0).call()

    def poolStats(self, arg0):
        return self.contract.functions.poolStats(arg0).call()

    def poolToAsset(self, arg0):
        return self.contract.functions.poolToAsset(arg0).call()

    def positionConfigs(self, arg0):
        return self.contract.functions.positionConfigs(arg0).call()

    def positionStates(self, arg0, arg1):
        return self.contract.functions.positionStates(arg0, arg1).call()

    def positions(self, arg0, arg1):
        return self.contract.functions.positions(arg0, arg1).call()

    def priceFeedAddress(self):
        return self.contract.functions.priceFeedAddress().call()

    def repay(self, loanId, nftId, repayAmount, isOnlyInterest):
        return self.contract.functions.repay(loanId, nftId, repayAmount, isOnlyInterest).call()

    def rollover(self, loanId, nftId):
        return self.contract.functions.rollover(loanId, nftId).call()

    def routers(self, arg0):
        return self.contract.functions.routers(arg0).call()

    def settleBorrowInterest(self, loanId, nftId):
        return self.contract.functions.settleBorrowInterest(loanId, nftId).call()

    def settleForwInterest(self):
        return self.contract.functions.settleForwInterest().call()

    def swapConfigs(self, arg0, arg1):
        return self.contract.functions.swapConfigs(arg0, arg1).call()

    def swapFeeRates(self, arg0):
        return self.contract.functions.swapFeeRates(arg0).call()

    def swapableToken(self, arg0):
        return self.contract.functions.swapableToken(arg0).call()

    def tokenPrecisionUnit(self, arg0):
        return self.contract.functions.tokenPrecisionUnit(arg0).call()

    def totalCollateralHold(self, arg0):
        return self.contract.functions.totalCollateralHold(arg0).call()

    def totalLossInUSD(self):
        return self.contract.functions.totalLossInUSD().call()

    def tradingCollateralWhitelist(self, arg0):
        return self.contract.functions.tradingCollateralWhitelist(arg0).call()

    def tradingFeeToLender(self):
        return self.contract.functions.tradingFeeToLender().call()

    def unPause(self, _func):
        return self.contract.functions.unPause(_func).call()

    def wallets(self, arg0, arg1):
        return self.contract.functions.wallets(arg0, arg1).call()

    def wethHandler(self):
        return self.contract.functions.wethHandler().call()

    def withdrawCollateral(self, nftId, collateralTokenAddress, underlyingTokenAddress, amount):
        return self.contract.functions.withdrawCollateral(nftId, collateralTokenAddress, underlyingTokenAddress, amount).call()
