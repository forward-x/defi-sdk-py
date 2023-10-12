import web3

import defi_sdk_py


class FwxWeb3:

    FUNCTION_NAME = "positions"
    FUNCTION_NAME = "positionStates"
    ID = "id"
    ENTRYPRICE = "entryPrice"
    CONTRACTSIZE = "contractSize"
    BORROWAMOUNT = "borrowAmount"
    COLLATERALUSED = "collateralUsed"
    COLLATERALSWAPPEDAMOUNT = "collateralSwappedAmount"
    INTERESTOWED = "interestOwed"
    INTERESTOWEDPERDAY = "interestOwedPerDay"
    INTERESTOWEPERDAY = "interestOwePerDay"
    LASTSETTLETIMESTAMP = "lastSettleTimestamp"

    ACTIVE = "active"
    ISLONG = "isLong"
    PNL = "PNL"
    AVERAGEENTRYPRICE = "averageEntryPrice"
    STARTTIMESTAMP = "startTimestamp"
    INTERESTPAID = "interestPaid"
    TOTALSWAPFEEPAID = "totalSwapFeePaid"
    TOTALSWAPFEE = "totalSwapFee"
    TOTALTRADINGFEEPAID = "totalTradingFeePaid"
    TOTALTRADINGFEE = "totalTradingFee"
    PAIRBYTE = "pairByte"

    FREE_BALANCE = "freeBalance"
    USED_BALANCE = "usedBalance"
    TOTAL_BALANCE = "totalBalance"

    COLLATERAL_ADDRESS = "collateralAddress"
    UNDERLYING_ADDRESS = "underlyingAddress"

    def __init__(self, url):
        self.w3 = web3.Web3(web3.HTTPProvider(url))

    def setSigner(self, privateKey):
        self.signer = web3.Account.privateKeyToAccount(privateKey)

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
    def openPosition(self, isLong, collateralTokenSymbol, underlyingTokenSymbol, nftId, entryPrice, contractSize, leverage, slippage, gas=1300000, gasPrice=25):
        validatePair(collateralTokenSymbol, underlyingTokenSymbol)
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        underlyingDecimal = self.__getTokenDecimal(underlyingTokenSymbol)

        tx = None
        contractSize = int(contractSize * 10**underlyingDecimal)
        leverage = int(leverage * 10**18)
        slippage = int(slippage * 10**18)
        entryPrice = entryPrice * 10**collateralDecimal
        if isLong:
            pool = self.__getPool(
                defi_sdk_py.ADDRESSES["AVAX"]["POOL"][collateralTokenSymbol])
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
                    'nonce': self.w3.eth.get_transaction_count(self.signer.address),
                    'gas': gas,
                    'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
                }
            )
        else:
            pool = self.__getPool(
                defi_sdk_py.ADDRESSES["AVAX"]["POOL"][underlyingTokenSymbol])
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
                    'nonce': self.w3.eth.get_transaction_count(self.signer.address),
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
    def closePosition(self, nftId, posId, closingSize, gas=1300000, gasPrice=25):
        positionState = self.__getPositionState(nftId, posId)
        pair = self.__getPair(
            positionState[FwxWeb3.FUNCTION_NAME][FwxWeb3.PAIRBYTE])
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
                'nonce': self.w3.eth.get_transaction_count(self.signer.address),
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
    def depositCollateral(self, collateralTokenSymbol, underlyingTokenSymbol, nftId, amount, gas=1300000, gasPrice=25):
        validatePair(collateralTokenSymbol, underlyingTokenSymbol)
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        amount = int(amount * 10 ** collateralDecimal)
        core = self.__getCore()
        library = self.__getLibrary()
        tx = core.functions.depositCollateral(nftId, defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol], defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol], amount).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': self.w3.eth.get_transaction_count(self.signer.address),
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
    def withdrawCollateral(self, collateralTokenSymbol, underlyingTokenSymbol, nftId, amount, gas=1300000, gasPrice=25):
        validatePair(collateralTokenSymbol, underlyingTokenSymbol)
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        amount = int(amount * 10**collateralDecimal)
        core = self.__getCore()
        library = self.__getLibrary()
        tx = core.functions.withdrawCollateral(nftId, defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol], defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol], amount).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': self.w3.eth.get_transaction_count(self.signer.address),
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
            nftId, positionOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.ID])
        if positionOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.ID] == 0:
            return {
                FwxWeb3.ID: 0,
                FwxWeb3.ENTRYPRICE: 0,
                FwxWeb3.CONTRACTSIZE: 0,
                FwxWeb3.BORROWAMOUNT: 0,
                FwxWeb3.COLLATERALUSED: 0,
                FwxWeb3.INTERESTOWED: 0,
                FwxWeb3.INTERESTOWEDPERDAY: 0,
                FwxWeb3.LASTSETTLETIMESTAMP: 0,
            }
        borrowingDecimal = collateralDecimal if positionState[
            FwxWeb3.ISLONG] else underlyingDecimal
        position = {
            FwxWeb3.ID: positionOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.ID],
            FwxWeb3.ENTRYPRICE: positionOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.ENTRYPRICE] / 10**collateralDecimal,
            FwxWeb3.CONTRACTSIZE: positionOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.CONTRACTSIZE] / 10**borrowingDecimal,
            FwxWeb3.BORROWAMOUNT: positionOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.BORROWAMOUNT] / 10**borrowingDecimal,
            FwxWeb3.COLLATERALUSED: positionOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.COLLATERALSWAPPEDAMOUNT] / 10**collateralDecimal,
            FwxWeb3.INTERESTOWED: positionOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.INTERESTOWED] / 10**borrowingDecimal,
            FwxWeb3.INTERESTOWEDPERDAY: positionOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.INTERESTOWEPERDAY] / 10**borrowingDecimal,
            FwxWeb3.LASTSETTLETIMESTAMP: positionOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.LASTSETTLETIMESTAMP],
        }
        return position

    def __getPositionStateInfo(self, nftId, posId):
        positionStateOutput = self.__getPositionState(nftId, posId)
        pair = self.__getPair(
            positionStateOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.PAIRBYTE])
        if int.from_bytes(positionStateOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.PAIRBYTE], 'big') == 0:
            return {
                FwxWeb3.ACTIVE: False,
                FwxWeb3.ISLONG: False,
                FwxWeb3.PNL: 0,
                FwxWeb3.AVERAGEENTRYPRICE: 0,
                FwxWeb3.STARTTIMESTAMP: 0,
                FwxWeb3.INTERESTPAID: 0,
                FwxWeb3.TOTALSWAPFEEPAID: 0,
                FwxWeb3.TOTALTRADINGFEEPAID: 0,
            }

        collateralDecimal = self.__getTokenDecimalFromAddress(
            pair[FwxWeb3.COLLATERAL_ADDRESS])
        underlyingDecimal = self.__getTokenDecimalFromAddress(
            pair[FwxWeb3.UNDERLYING_ADDRESS])
        borrowingDecimal = collateralDecimal if positionStateOutput[
            FwxWeb3.FUNCTION_NAME][FwxWeb3.ISLONG] else underlyingDecimal
        positionState = {
            FwxWeb3.ACTIVE: positionStateOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.ACTIVE],
            FwxWeb3.ISLONG: positionStateOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.ISLONG],
            FwxWeb3.PNL: positionStateOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.PNL] / 10**18,
            FwxWeb3.AVERAGEENTRYPRICE: positionStateOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.AVERAGEENTRYPRICE] / 10**collateralDecimal,
            FwxWeb3.STARTTIMESTAMP: positionStateOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.STARTTIMESTAMP],
            FwxWeb3.INTERESTPAID: positionStateOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.INTERESTPAID] / 10**borrowingDecimal,
            FwxWeb3.TOTALSWAPFEEPAID: positionStateOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.TOTALSWAPFEE] / 10**borrowingDecimal,
            FwxWeb3.TOTALTRADINGFEEPAID: positionStateOutput[FwxWeb3.FUNCTION_NAME][FwxWeb3.TOTALTRADINGFEE] / 10**collateralDecimal,
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
            abis, FwxWeb3.FUNCTION_NAME), core.abi))
        return FwxWeb3.tupleOutputDecode(position, abi)

    def __getPositionState(self, nftId, posId):
        core = self.__getCore()
        positionState = core.functions.positionStates(nftId, posId).call()
        abi = next(filter(lambda abis: FwxWeb3.filterFunctionABI(
            abis, FwxWeb3.FUNCTION_NAME), core.abi))
        return FwxWeb3.tupleOutputDecode(positionState, abi)

    def __getPair(self, pairByte):
        core = self.__getCore()
        pair = core.functions.pairs(pairByte).call()
        return {FwxWeb3.COLLATERAL_ADDRESS: pair[0], FwxWeb3.UNDERLYING_ADDRESS: pair[1]}

    def __getTokenDecimal(self, tokenSymbol):
        token = self.__getToken(
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][tokenSymbol])
        decimal = token.functions.decimals().call()
        return decimal

    def __getTokenDecimalFromAddress(self, tokenAddress):
        token = self.__getToken(tokenAddress)
        decimal = token.functions.decimals().call()
        return decimal

    def __getCore(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["CORE"], abi=defi_sdk_py.IAPHCORE_ABI)

    def __getPool(self, poolAddress):
        return self.w3.eth.contract(address=poolAddress, abi=defi_sdk_py.IAPHPOOL_ABI)

    def __getHelperFutureTrade(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["HELPER_FUTURETRADE"], abi=defi_sdk_py.IHELPERFUTURETRADE_ABI)

    def __getLibrary(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["APH_LIBRARY"], abi=defi_sdk_py.IAPHLIBRARY_ABI)

    def __getToken(self, tokenAddress):
        return self.w3.eth.contract(address=tokenAddress, abi=defi_sdk_py.IERC20_ABI)

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
