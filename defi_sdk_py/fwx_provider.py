import web3

import defi_sdk_py


class FwxWeb3:

    POSITIONS = "positions"
    ID = "id"
    ENTRY_PRICE = "entryPrice"
    CONTRACT_SIZE = "contractSize"
    BORROW_AMOUNT = "borrowAmount"
    COLLATERAL_USED = "collateralUsed"
    COLLATERAL_SWAPPED_AMOUNT = "collateralSwappedAmount"
    INTEREST_OWED = "interestOwed"
    INTEREST_OWED_PER_DAY = "interestOwedPerDay"
    INTEREST_OWE_PER_DAY = "interestOwePerDay"
    LAST_SETTLE_TIMESTAMP = "lastSettleTimestamp"

    POSITION_STATES = "positionStates"
    ACTIVE = "active"
    ISLONG = "isLong"
    PNL = "PNL"
    AVERAGE_ENTRY_PRICE = "averageEntryPrice"
    START_TIMESTAMP = "startTimestamp"
    INTEREST_PAID = "interestPaid"
    TOTAL_SWAP_FEE_PAID = "totalSwapFeePaid"
    TOTAL_SWAP_FEE = "totalSwapFee"
    TOTAL_TRADING_FEE_PAID = "totalTradingFeePaid"
    TOTAL_TRADING_FEE = "totalTradingFee"
    PAIR_BYTE = "pairByte"

    ACTIVE_LOAN = "activeLoan"
    ACTIVE_LOAN_INFO = "activeLoanInfo"

    LOAN = "loans"
    INTEREST_PAID = "interestPaid"
    BORROW_TOKEN_ADDRESS = "borrowTokenAddress"
    ROLLOVER_TIMESTAMP = "rolloverTimestamp"
    LAST_SETTLE_TIMESTAMP = "lastSettleTimestamp"
    COLLATERAL_TOKEN_ADDRESS = "collateralTokenAddress"
    BORROW_AMOUNT = "borrowAmount"
    COLLATERAL_AMOUNT = "collateralAmount"
    OWED_PER_DAY = "owedPerDay"
    MIN_INTEREST = "minInterest"
    INTEREST_OWED = "interestOwed"

    FREE_BALANCE = "freeBalance"
    USED_BALANCE = "usedBalance"
    TOTAL_BALANCE = "totalBalance"

    COLLATERAL_ADDRESS = "collateralAddress"
    UNDERLYING_ADDRESS = "underlyingAddress"

    def __init__(self, url):
        self.w3 = web3.Web3(web3.HTTPProvider(url))

    def setSigner(self, privateKey):
        self.signer = web3.Account.privateKeyToAccount(privateKey)

    # Membership

    # mint
    # - **Instance**: Membership
    # - **Parameters**
    #     - referral: BigNumberish
    # - **Output**
    #     - tokenId: BigNumberish
    def mint(self, referral, gas=220000, gasPrice=25, nonce=0):
        membership = self.__getMembership()

        tx = membership.functions.mint(
            referral
        ).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
            }
        )
        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        txReceipt = self.w3.eth.wait_for_transaction_receipt(txHash)
        if txReceipt["status"] == 0:
            return (txHash, -1)
        helperMembershipAndStakePool = self.__getHelperMembershipAndStakePool()
        result = helperMembershipAndStakePool.functions.getNFTList(
            self.signer.address).call()
        return (txHash, result[1][len(result[1])-1])

    # getRank
    # - **Instance**: Membership
    # - **Note**: If `pool` exist we’ll get a rank from that pool, otherwise get from a current pool
    # - **Parameters**
    #     - tokenId: BigNumberish
    #     - pool?: string (address of StakePool)
    # - **Output**:
    #     - rank: BigNumberish
    def getRank(self, tokenId, stakePoolAddress=""):
        membership = self.__getMembership()
        result = None
        if stakePoolAddress == "":
            result = membership.functions.getRank(tokenId).call()
        else:
            result = membership.functions.getRank(
                stakePoolAddress, tokenId).call()
        return result

    # ownerOf
    # - **Instance**: Membership
    # - **Parameters**
    #     - target: address
    # - **Output**:
    #     - owner: address
    def ownerOf(self, tokenId):
        membership = self.__getMembership()
        return membership.functions.ownerOf(tokenId).call()

    # usableToken
    # - **Instance**: Membership
    # - **Note**: We can use `callstatic` to prevent revert from chain and handle error for the users
    # - **Parameters**
    #     - owner: address
    #     - tokenId: BigNumberish
    # - **Output**:
    #     - useableTokenId: BigNumberish
    def usableToken(self, ownerAddress, tokenId):
        membership = self.__getMembership()
        return membership.functions.usableTokenId(ownerAddress, tokenId).call({"from": ownerAddress})

    # Borrowing

    # borrow
    # - **Instance**: APHPool
    # - **Parameters**
    #     - pool: TokenSymbols
    #     - nftId: BigNumberish
    #     - loanId: BigNumberish
    #     - borrowAmount: BigNumberish
    #     - collateralAmount: BigNumberish
    #     - collateralToken: TokenSymbols
    # - **Output**
    #     - result: CoreBase.Loan (struct from solidity)
    def borrow(self, poolTokenSymbol, nftId, loanId, borrowAmount, collateralAmount, collateralTokenSymbol, gas=800000, gasPrice=25, nonce=0):
        validatePair(collateralTokenSymbol, poolTokenSymbol)
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        poolTokenDecimal = self.__getTokenDecimal(poolTokenSymbol)
        pool = self.__getPool(poolTokenSymbol)
        collateralAmount = int(collateralAmount * 10**collateralDecimal)
        borrowAmount = int(borrowAmount * 10**poolTokenDecimal)
        tx = pool.functions.borrow(
            loanId,
            nftId,
            borrowAmount,
            collateralAmount,
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol]
        ).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
                'value': collateralAmount if self.__isTokenSymbolNative(collateralTokenSymbol) else 0
            }
        )
        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(txHash)

        return (txHash, self.__getActiveLoan(nftId)[-1][FwxWeb3.ACTIVE_LOAN])

    def __getActiveLoan(self, nftId):
        helperCore = self.__getHelperCore()
        core = self.__getCore()
        currentLoanIndex = core.functions.currentLoanIndex(nftId).call()
        newCursor = 1
        resultPerPage = 10
        results = []
        abi = next(filter(lambda abis: FwxWeb3.filterFunctionABI(
            abis, FwxWeb3.LOAN), core.abi))

        while newCursor <= currentLoanIndex:
            helperReturn = helperCore.functions.getActiveLoans(
                nftId, newCursor, resultPerPage).call()
            results += list(
                map(
                    lambda lst: dict(
                        (key, v) for key, v in zip(
                            [FwxWeb3.ACTIVE_LOAN, FwxWeb3.ACTIVE_LOAN_INFO,
                             FwxWeb3.INTEREST_OWE_PER_DAY],
                            [FwxWeb3.tupleOutputDecode(
                                lst[0], abi)[FwxWeb3.LOAN], lst[1], lst[2]]
                        )
                    ),
                    [[helperReturn[0][i], helperReturn[1][i], helperReturn[2][i]]
                        for i in range(len(helperReturn[0]))]
                )
            )
            newCursor = helperReturn[3]
        return results

    # Trading

    # openPosition
    # - **Instance**: APHPool
    # - **Note**: The user doesn’t have to know borrow token and swap token, just choose collateral and underlying then trade.
    # - **Parameters**
    #     - isLong: boolean
    #     - collateral: TokenSymbols
    #     - underlying: TokenSymbols
    #     - nftId: BigNumberish
    #     - entryPrice: BigNumberish
    #     - contractSize: BigNumberish
    #     - leverage: BigNumberish
    #     - slippage: BigNumberish
    # - **Output**
    #     - result: CoreBase.Position (struct from solidity)
    def openPosition(self, isLong, collateralTokenSymbol, underlyingTokenSymbol, nftId, entryPrice, contractSize, leverage, slippage, gas=1300000, gasPrice=25, nonce=0):
        validatePair(collateralTokenSymbol, underlyingTokenSymbol)
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        underlyingDecimal = self.__getTokenDecimal(underlyingTokenSymbol)

        tx = None
        contractSize = int(contractSize * 10**underlyingDecimal)
        leverage = int(leverage * 10**18)
        slippage = int(slippage * 10**18)
        entryPrice = entryPrice * 10**collateralDecimal
        if isLong:
            pool = self.__getPool(collateralTokenSymbol)
            tx = pool.functions.openPosition(
                nftId,
                defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
                defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol],
                entryPrice,
                contractSize,
                leverage,
                slippage
            ).buildTransaction(
                {
                    'from': self.signer.address,
                    'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                    'gas': gas,
                    'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
                }
            )
        else:
            pool = self.__getPool(underlyingTokenSymbol)
            tx = pool.functions.openPosition(
                nftId,
                defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
                defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
                entryPrice,
                contractSize,
                leverage,
                slippage
            ).buildTransaction(
                {
                    'from': self.signer.address,
                    'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                    'gas': gas,
                    'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
                }
            )
        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(txHash)
        position = self.__getPosition(
            nftId, collateralTokenSymbol, underlyingTokenSymbol)
        return (txHash, position)

    # closePosition
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - posId: BigNumberish
    #     - closingSize: BigNumberish
    # - **Output**
    #     - result: CoreBase.Position (struct from solidity)
    def closePosition(self, nftId, posId, closingSize, gas=1300000, gasPrice=25, nonce=0):
        positionState = self.__getPositionState(nftId, posId)
        pair = self.__getPair(
            positionState[FwxWeb3.PAIR_BYTE])
        underlyingDecimal = self.__getTokenDecimalFromAddress(
            pair[FwxWeb3.UNDERLYING_ADDRESS])
        closingSize = int(closingSize * 10**underlyingDecimal)
        core = self.__getCore()
        tx = core.functions.closePosition(
            nftId,
            posId,
            closingSize
        ).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
            }
        )

        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(txHash)
        position = self.__getPositionFromAddress(
            nftId, pair[FwxWeb3.COLLATERAL_ADDRESS], pair[FwxWeb3.UNDERLYING_ADDRESS])
        return (txHash, position)

    # depositCollateral
    # - **Instance**: APHCore
    # - **Parameters**
    #     - collateral: TokenSymbols
    #     - underlying: TokenSymbols
    #     - nftId: BigNumberish
    #     - amount: BigNumberish
    # - **Output**
    #     - balance: BigNumberish
    def depositCollateral(self, collateralTokenSymbol, underlyingTokenSymbol, nftId, amount, gas=1300000, gasPrice=25, nonce=0):
        validatePair(collateralTokenSymbol, underlyingTokenSymbol)
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        amount = int(amount * 10 ** collateralDecimal)
        core = self.__getCore()
        library = self.__getLibrary()
        tx = core.functions.depositCollateral(nftId, defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol], defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol], amount).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
            }
        )

        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(txHash)
        pairByte = library.functions.hashPair(
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol],
        ).call()
        balance = core.functions.wallets(nftId, pairByte).call()
        return (txHash, balance / 10 ** collateralDecimal)

    # withdrawCollateral
    # - **Instance**: APHCore
    # - **Parameters**
    #     - collateral: TokenSymbols
    #     - underlying: TokenSymbols
    #     - nftId: BigNumberish
    #     - amount: BigNumberish
    # - **Output**
    #     - balance: BigNumberish
    def withdrawCollateral(self, collateralTokenSymbol, underlyingTokenSymbol, nftId, amount, gas=1300000, gasPrice=25, nonce=0):
        validatePair(collateralTokenSymbol, underlyingTokenSymbol)
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        amount = int(amount * 10**collateralDecimal)
        core = self.__getCore()
        library = self.__getLibrary()
        tx = core.functions.withdrawCollateral(nftId, defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol], defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol], amount).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
            }
        )

        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(txHash)
        pairByte = library.functions.hashPair(
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol],
        ).call()
        balance = core.functions.wallets(nftId, pairByte).call()
        return (txHash, balance / 10 ** collateralDecimal)

    def getCollateralBalance(self, collateralTokenSymbol, underlyingTokenSymbol, nftId):
        validatePair(collateralTokenSymbol, underlyingTokenSymbol)
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        core = self.__getCore()
        library = self.__getLibrary()
        pairByte = library.functions.hashPair(
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol],
        ).call()
        balance = core.functions.wallets(nftId, pairByte).call()
        return balance / 10 ** collateralDecimal

    # getPositionInfo
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - collateral: TokenSymbols
    #     - underlying: TokenSymbols
    # - **Output**
    #     - id: BigNumberish
    #     - entryPrice: BigNumberish
    #     - contractSize: BigNumberish
    #     - borrowAmount: BigNumberish
    #     - collateralUsed: BigNumberish (collateral swapped)
    #     - interestOwed: BigNumberish
    #     - interestOwedPerDay: BigNumberish
    #     - lastSettleTimstamp: BigNumberish
    def getPositionInfo(self, nftId, collateralTokenSymbol, underlyingTokenSymbol):
        return self.__getPositionInfo(nftId, collateralTokenSymbol, underlyingTokenSymbol)

    #  getAllActivePosition
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - pairs: Array of object {collateral: TokenSymbols, underlying: TokenSymbols}
    # - **Output**
    #     - **Array** of Positions
    #         - id: BigNumberish
    #         - entryPrice: BigNumberish
    #         - contractSize: BigNumberish
    #         - borrowAmount: BigNumberish
    #         - collateralUsed: BigNumberish (collateral swapped)
    #         - interestOwed: BigNumberish
    #         - interestOwedPerDay: BigNumberish
    #         - lastSettleTimestamp: BigNumberish
    def getAllActivePosition(self, nftId, pairs):
        activePositions = []
        for pair in pairs:
            collateralTokenSymbol = pair["collateral"]
            underlyingTokenSymbol = pair["underlying"]
            validatePair(collateralTokenSymbol, underlyingTokenSymbol)
            position = self.__getPositionInfo(
                nftId, collateralTokenSymbol, underlyingTokenSymbol)
            if position["id"] != 0:
                activePositions.append(position)
        return activePositions

    # getPositionStateInfo
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - posId: BigNumberish
    # - **Output**
    #     - active: boolean
    #     - isLong: boolean
    #     - PNL: BigNumberish
    #     - averateEntryProce: BigNumberish
    #     - startTimstamp: BigNumberish
    #     - interestPaid: BigNumberish
    #     - totalSwapFeePaid: BigNumberish
    #     - totalTradingFeePaid: BigNumberish
    def getPositionStateInfo(self, nftId, posId):
        return self.__getPositionStateInfo(nftId, posId)

    # getCurrentMargin
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - collateral: TokenSymbols
    #     - underlying: TokenSymbols
    # - **Output**
    #     - PNL: BigNumberish (optional, can be separated to another function)
    #     - margin: BigNumberish
    def getCurrentMargin(self, nftId, collateralTokenSymbol, underlyingTokenSymbol):
        helperFutureTrade = self.__getHelperFutureTrade()
        library = self.__getLibrary()
        pairByte = library.functions.hashPair(
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol]
        ).call()

        return helperFutureTrade.functions.getPositionMargin(nftId, pairByte).call() / 10 ** 18

    # getAvailableCollateral
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - collateral: TokenSymbols
    #     - underlying: TokenSymbols
    # - **Output**
    #     - freeBalance: BigNumberish
    #     - usedBalance: BigNumberish
    #     - totalBalance: BigNumberish
    def getAvailableCollateral(self, nftId, collateralTokenSymbol, underlyingTokenSymbol):
        helperFutureTrade = self.__getHelperFutureTrade()
        library = self.__getLibrary()
        pairByte = library.functions.hashPair(
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol]
        ).call()
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        balanceDetail = helperFutureTrade.functions.getBalanceDetails(
            nftId, pairByte).call()
        return {
            FwxWeb3.FREE_BALANCE: balanceDetail[0] / 10 ** collateralDecimal,
            FwxWeb3.USED_BALANCE: balanceDetail[1] / 10 ** collateralDecimal,
            FwxWeb3.TOTAL_BALANCE: balanceDetail[2] / 10 ** collateralDecimal,
        }

    def __getPositionInfo(self, nftId, collateralTokenSymbol, underlyingTokenSymbol):
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        underlyingDecimal = self.__getTokenDecimal(underlyingTokenSymbol)
        positionOutput = self.__getPosition(
            nftId, collateralTokenSymbol, underlyingTokenSymbol)
        positionState = self.__getPositionStateInfo(
            nftId, positionOutput[FwxWeb3.ID])
        if positionOutput[FwxWeb3.ID] == 0:
            return {
                FwxWeb3.ID: 0,
                FwxWeb3.ENTRY_PRICE: 0,
                FwxWeb3.CONTRACT_SIZE: 0,
                FwxWeb3.BORROW_AMOUNT: 0,
                FwxWeb3.COLLATERAL_USED: 0,
                FwxWeb3.INTEREST_OWED: 0,
                FwxWeb3.INTEREST_OWED_PER_DAY: 0,
                FwxWeb3.LAST_SETTLE_TIMESTAMP: 0,
            }
        borrowingDecimal = collateralDecimal if positionState[
            FwxWeb3.ISLONG] else underlyingDecimal
        position = {
            FwxWeb3.ID: positionOutput[FwxWeb3.ID],
            FwxWeb3.ENTRY_PRICE: positionOutput[FwxWeb3.ENTRY_PRICE] / 10**collateralDecimal,
            FwxWeb3.CONTRACT_SIZE: positionOutput[FwxWeb3.CONTRACT_SIZE] / 10**borrowingDecimal,
            FwxWeb3.BORROW_AMOUNT: positionOutput[FwxWeb3.BORROW_AMOUNT] / 10**borrowingDecimal,
            FwxWeb3.COLLATERAL_USED: positionOutput[FwxWeb3.COLLATERAL_SWAPPED_AMOUNT] / 10**collateralDecimal,
            FwxWeb3.INTEREST_OWED: positionOutput[FwxWeb3.INTEREST_OWED] / 10**borrowingDecimal,
            FwxWeb3.INTEREST_OWED_PER_DAY: positionOutput[FwxWeb3.INTEREST_OWE_PER_DAY] / 10**borrowingDecimal,
            FwxWeb3.LAST_SETTLE_TIMESTAMP: positionOutput[FwxWeb3.LAST_SETTLE_TIMESTAMP],
        }
        return position

    def __getPositionStateInfo(self, nftId, posId):
        positionStateOutput = self.__getPositionState(nftId, posId)
        pair = self.__getPair(
            positionStateOutput[FwxWeb3.PAIR_BYTE])
        if int.from_bytes(positionStateOutput[FwxWeb3.PAIR_BYTE], 'big') == 0:
            return {
                FwxWeb3.ACTIVE: False,
                FwxWeb3.ISLONG: False,
                FwxWeb3.PNL: 0,
                FwxWeb3.AVERAGE_ENTRY_PRICE: 0,
                FwxWeb3.START_TIMESTAMP: 0,
                FwxWeb3.INTEREST_PAID: 0,
                FwxWeb3.TOTAL_SWAP_FEE_PAID: 0,
                FwxWeb3.TOTAL_TRADING_FEE_PAID: 0,
            }

        collateralDecimal = self.__getTokenDecimalFromAddress(
            pair[FwxWeb3.COLLATERAL_ADDRESS])
        underlyingDecimal = self.__getTokenDecimalFromAddress(
            pair[FwxWeb3.UNDERLYING_ADDRESS])
        borrowingDecimal = collateralDecimal if positionStateOutput[
            FwxWeb3.ISLONG] else underlyingDecimal
        positionState = {
            FwxWeb3.ACTIVE: positionStateOutput[FwxWeb3.ACTIVE],
            FwxWeb3.ISLONG: positionStateOutput[FwxWeb3.ISLONG],
            FwxWeb3.PNL: positionStateOutput[FwxWeb3.PNL] / 10**18,
            FwxWeb3.AVERAGE_ENTRY_PRICE: positionStateOutput[FwxWeb3.AVERAGE_ENTRY_PRICE] / 10**collateralDecimal,
            FwxWeb3.START_TIMESTAMP: positionStateOutput[FwxWeb3.START_TIMESTAMP],
            FwxWeb3.INTEREST_PAID: positionStateOutput[FwxWeb3.INTEREST_PAID] / 10**borrowingDecimal,
            FwxWeb3.TOTAL_SWAP_FEE_PAID: positionStateOutput[FwxWeb3.TOTAL_SWAP_FEE] / 10**borrowingDecimal,
            FwxWeb3.TOTAL_TRADING_FEE_PAID: positionStateOutput[FwxWeb3.TOTAL_TRADING_FEE] / 10**collateralDecimal,
        }
        return positionState

    def __getPosition(self, nftId, collateralTokenSymbol, underlyingTokenSymbol):
        return self.__getPositionFromAddress(nftId, defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol], defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol])

    def __getPositionFromAddress(self, nftId, collateralTokenAddress, underlyingTokenAddress):
        core = self.__getCore()
        library = self.__getLibrary()
        pairByte = library.functions.hashPair(
            collateralTokenAddress,
            underlyingTokenAddress,
        ).call()
        position = core.functions.positions(nftId, pairByte).call()

        abi = next(filter(lambda abis: FwxWeb3.filterFunctionABI(
            abis, FwxWeb3.POSITIONS), core.abi))
        return FwxWeb3.tupleOutputDecode(position, abi)[FwxWeb3.POSITIONS]

    def __getPositionState(self, nftId, posId):
        core = self.__getCore()
        positionState = core.functions.positionStates(nftId, posId).call()
        abi = next(filter(lambda abis: FwxWeb3.filterFunctionABI(
            abis, FwxWeb3.POSITION_STATES), core.abi))
        return FwxWeb3.tupleOutputDecode(positionState, abi)[FwxWeb3.POSITION_STATES]

    def __getPair(self, pairByte):
        core = self.__getCore()
        pair = core.functions.pairs(pairByte).call()
        return {FwxWeb3.COLLATERAL_ADDRESS: pair[0], FwxWeb3.UNDERLYING_ADDRESS: pair[1]}

    def approveToken(self, spenderAddress, tokenSymbol, gas=1300000, gasPrice=25, nonce=0):
        token = self.__getToken(tokenSymbol)

        amount = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        tx = token.functions.approve(spenderAddress, amount).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
            }
        )

        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(txHash)
        return True

    def getTokenDecimal(self, tokenSymbol):
        return self.__getTokenDecimal(tokenSymbol)

    def __getTokenDecimal(self, tokenSymbol):
        token = self.__getTokenFromAddress(
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][tokenSymbol])
        decimal = token.functions.decimals().call()
        return decimal

    def __getTokenDecimalFromAddress(self, tokenAddress):
        token = self.__getTokenFromAddress(tokenAddress)
        decimal = token.functions.decimals().call()
        return decimal

    def __getCore(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["CORE"], abi=defi_sdk_py.IAPHCORE_ABI)

    def __getPool(self, poolTokenSymbol):
        return self.__getPoolFromAddress(defi_sdk_py.ADDRESSES["AVAX"]["POOL"][poolTokenSymbol])

    def __getPoolFromAddress(self, poolAddress):
        return self.w3.eth.contract(address=poolAddress, abi=defi_sdk_py.IAPHPOOL_ABI)

    def getMembership(self):
        return self.__getMembership()

    def __getMembership(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["MEMBERSHIP"], abi=defi_sdk_py.IMEMBERSHIP_ABI)

    def __getHelperCore(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["HELPER_CORE"], abi=defi_sdk_py.IHELPERCORE_ABI)

    def __getHelperMembershipAndStakePool(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["HELPER_MEMBERSHIP_AND_STAKEPOOL"], abi=defi_sdk_py.IHELPERMEMBERSHIPANDSTAKEPOOL_ABI)

    def __getHelperFutureTrade(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["HELPER_FUTURETRADE"], abi=defi_sdk_py.IHELPERFUTURETRADE_ABI)

    def __getLibrary(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["APH_LIBRARY"], abi=defi_sdk_py.IAPHLIBRARY_ABI)

    def getToken(self, tokenSymbol):
        return self.__getToken(tokenSymbol)

    def __getToken(self, tokenSymbol):
        return self.__getTokenFromAddress(defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][tokenSymbol])

    def getTokenFromAddress(self, tokenAddress):
        return self.__getTokenFromAddress(tokenAddress)

    def __getTokenFromAddress(self, tokenAddress):
        return self.w3.eth.contract(address=tokenAddress, abi=defi_sdk_py.IERC20_ABI)

    def __isTokenSymbolNative(self, tokenSymbol):
        return True if tokenSymbol in ["WAVAX"] else False

    def getW3(self):
        return self.w3

    def getSigner(self):
        return self.signer

    @staticmethod
    def tupleOutputDecode(value, abi):
        """Decode tuple as dict."""
        abiOutputs = {}
        if "outputs" in abi:
            abiOutputs = abi.get("outputs", abi)[0]

        # complex value
        if 'components' in abiOutputs:
            inner = {}
            for x, y in zip(value, abiOutputs["components"]):
                inner.update(FwxWeb3.tupleOutputDecode(x, y))
            result = {abi["name"]: inner}
            return result.get("", result)

        # basic value
        return {abi["name"]: value}

    @staticmethod
    def filterFunctionABI(abi, functionName):
        if abi["name"] == functionName:
            return True
        return False


def getClient(url):
    return FwxWeb3(url)


def validatePair(collateral, underlying):
    assert collateral != underlying, "same collateral and underlying token"
    assert collateral in defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"], "collateral not allowed"
    assert underlying in defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"], "underlying not allowed"
