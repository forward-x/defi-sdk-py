import web3

import defi_sdk_py


class FwxWeb3:

    POSITION_FUNCTION_NAME = "positions"
    POSITION_STATE_FUNCTION_NAME = "positionStates"
    POSITION_ID = "id"
    POSITION_ENTRYPRICE = "entryPrice"
    POSITION_CONTRACTSIZE = "contractSize"
    POSITION_BORROWAMOUNT = "borrowAmount"
    POSITION_COLLATERALUSED = "collateralUsed"
    POSITION_COLLATERALSWAPPEDAMOUNT = "collateralSwappedAmount"
    POSITION_INTERESTOWED = "interestOwed"
    POSITION_INTERESTOWEDPERDAY = "interestOwedPerDay"
    POSITION_INTERESTOWEPERDAY = "interestOwePerDay"
    POSITION_LASTSETTLETIMESTAMP = "lastSettleTimestamp"

    POSITION_STATE_ACTIVE = "active"
    POSITION_STATE_ISLONG = "isLong"
    POSITION_STATE_PNL = "PNL"
    POSITION_STATE_AVERAGEENTRYPRICE = "averageEntryPrice"
    POSITION_STATE_STARTTIMESTAMP = "startTimestamp"
    POSITION_STATE_INTERESTPAID = "interestPaid"
    POSITION_STATE_TOTALSWAPFEEPAID = "totalSwapFeePaid"
    POSITION_STATE_TOTALSWAPFEE = "totalSwapFee"
    POSITION_STATE_TOTALTRADINGFEEPAID = "totalTradingFeePaid"
    POSITION_STATE_TOTALTRADINGFEE = "totalTradingFee"
    POSITION_STATE_PAIRBYTE = "pairByte"

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
                    'gas': 1500000,
                    'gasPrice': self.w3.toWei(25, 'gwei'),
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
        pass

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
        amount = int(amount * collateralDecimal)
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
        return (txHash, balance / collateralDecimal)

    # withdrawCollateral
    #
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
        amount = int(amount * collateralDecimal)
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
        return (txHash, balance / collateralDecimal)

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

    def __getPositionInfo(self, nftId, collateralTokenSymbol, underlyingTokenSymbol):
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        underlyingDecimal = self.__getTokenDecimal(underlyingTokenSymbol)
        positionOutput = self.__getPosition(
            nftId, collateralTokenSymbol, underlyingTokenSymbol)
        positionStateOutput = self.__getPositionStateInfo(
            nftId, positionOutput[FwxWeb3.POSITION_FUNCTION_NAME][FwxWeb3.POSITION_ID])
        if positionOutput[FwxWeb3.POSITION_FUNCTION_NAME][FwxWeb3.POSITION_ID] == 0:
            return {
                FwxWeb3.POSITION_ID: 0,
                FwxWeb3.POSITION_ENTRYPRICE: 0,
                FwxWeb3.POSITION_CONTRACTSIZE: 0,
                FwxWeb3.POSITION_BORROWAMOUNT: 0,
                FwxWeb3.POSITION_COLLATERALUSED: 0,
                FwxWeb3.POSITION_INTERESTOWED: 0,
                FwxWeb3.POSITION_INTERESTOWEDPERDAY: 0,
                FwxWeb3.POSITION_LASTSETTLETIMESTAMP: 0,
            }
        borrowingDecimal = collateralDecimal if positionStateOutput["ISLONG"] else underlyingDecimal
        position = {
            FwxWeb3.POSITION_ID: positionOutput[FwxWeb3.POSITION_FUNCTION_NAME][FwxWeb3.POSITION_ID],
            FwxWeb3.POSITION_ENTRYPRICE: positionOutput[FwxWeb3.POSITION_FUNCTION_NAME][FwxWeb3.POSITION_ENTRYPRICE] / 10**collateralDecimal,
            FwxWeb3.POSITION_CONTRACTSIZE: positionOutput[FwxWeb3.POSITION_FUNCTION_NAME][FwxWeb3.POSITION_CONTRACTSIZE] / 10**borrowingDecimal,
            FwxWeb3.POSITION_BORROWAMOUNT: positionOutput[FwxWeb3.POSITION_FUNCTION_NAME][FwxWeb3.POSITION_BORROWAMOUNT] / 10**borrowingDecimal,
            FwxWeb3.POSITION_COLLATERALUSED: positionOutput[FwxWeb3.POSITION_FUNCTION_NAME][FwxWeb3.POSITION_COLLATERALSWAPPEDAMOUNT] / 10**collateralDecimal,
            FwxWeb3.POSITION_INTERESTOWED: positionOutput[FwxWeb3.POSITION_FUNCTION_NAME][FwxWeb3.POSITION_INTERESTOWED] / 10**borrowingDecimal,
            FwxWeb3.POSITION_INTERESTOWEDPERDAY: positionOutput[FwxWeb3.POSITION_FUNCTION_NAME][FwxWeb3.POSITION_INTERESTOWEPERDAY] / 10**borrowingDecimal,
            FwxWeb3.POSITION_LASTSETTLETIMESTAMP: positionOutput[FwxWeb3.POSITION_FUNCTION_NAME][FwxWeb3.POSITION_LASTSETTLETIMESTAMP],
        }
        return position

    def __getPositionStateInfo(self, nftId, posId):
        positionStateOutput = self.__getPositionState(nftId, posId)
        pair = self.__getPair(
            positionStateOutput[FwxWeb3.POSITION_STATE_FUNCTION_NAME][FwxWeb3.POSITION_STATE_PAIRBYTE])
        if positionStateOutput[FwxWeb3.POSITION_STATE_FUNCTION_NAME][FwxWeb3.POSITION_STATE_PAIRBYTE] == 0:
            return {
                FwxWeb3.POSITION_STATE_ACTIVE: 0,
                FwxWeb3.POSITION_STATE_ISLONG: 0,
                FwxWeb3.POSITION_STATE_PNL: 0,
                FwxWeb3.POSITION_STATE_AVERAGEENTRYPRICE: 0,
                FwxWeb3.POSITION_STATE_STARTTIMESTAMP: 0,
                FwxWeb3.POSITION_STATE_INTERESTPAID: 0,
                FwxWeb3.POSITION_STATE_TOTALSWAPFEEPAID: 0,
                FwxWeb3.POSITION_STATE_TOTALTRADINGFEEPAID: 0,
            }

        collateralDecimal = self.__getTokenDecimalFromAddress(
            pair[FwxWeb3.COLLATERAL_ADDRESS])
        underlyingDecimal = self.__getTokenDecimalFromAddress(
            pair[FwxWeb3.UNDERLYING_ADDRESS])
        borrowingDecimal = collateralDecimal if positionStateOutput[
            FwxWeb3.POSITION_STATE_FUNCTION_NAME][FwxWeb3.POSITION_STATE_ISLONG] else underlyingDecimal
        positionState = {
            FwxWeb3.POSITION_STATE_ACTIVE: positionStateOutput[FwxWeb3.POSITION_STATE_FUNCTION_NAME][FwxWeb3.POSITION_STATE_ACTIVE],
            FwxWeb3.POSITION_STATE_ISLONG: positionStateOutput[FwxWeb3.POSITION_STATE_FUNCTION_NAME][FwxWeb3.POSITION_STATE_ISLONG],
            FwxWeb3.POSITION_STATE_PNL: positionStateOutput[FwxWeb3.POSITION_STATE_FUNCTION_NAME][FwxWeb3.POSITION_STATE_PNL] / 10**18,
            FwxWeb3.POSITION_STATE_AVERAGEENTRYPRICE: positionStateOutput[FwxWeb3.POSITION_STATE_FUNCTION_NAME][FwxWeb3.POSITION_STATE_AVERAGEENTRYPRICE] / 10**collateralDecimal,
            FwxWeb3.POSITION_STATE_STARTTIMESTAMP: positionStateOutput[FwxWeb3.POSITION_STATE_FUNCTION_NAME][FwxWeb3.POSITION_STATE_STARTTIMESTAMP],
            FwxWeb3.POSITION_STATE_INTERESTPAID: positionStateOutput[FwxWeb3.POSITION_STATE_FUNCTION_NAME][FwxWeb3.POSITION_STATE_INTERESTPAID] / 10**borrowingDecimal,
            FwxWeb3.POSITION_STATE_TOTALSWAPFEEPAID: positionStateOutput[FwxWeb3.POSITION_STATE_FUNCTION_NAME][FwxWeb3.POSITION_STATE_TOTALSWAPFEE] / 10**borrowingDecimal,
            FwxWeb3.POSITION_STATE_TOTALTRADINGFEEPAID: positionStateOutput[FwxWeb3.POSITION_STATE_FUNCTION_NAME][FwxWeb3.POSITION_STATE_TOTALTRADINGFEE] / 10**collateralDecimal,
        }
        return positionState

    def __getPosition(self, nftId, collateralTokenSymbol, underlyingTokenSymbol):
        core = self.__getCore()
        library = self.__getLibrary()
        pairByte = library.functions.hashPair(
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol],
        ).call()
        position = core.functions.positions(nftId, pairByte).call()

        abi = next(filter(lambda abis: FwxWeb3.filterFunctionABI(
            abis, FwxWeb3.POSITION_FUNCTION_NAME), core.abi))
        return FwxWeb3.tupleOutputDecode(position, abi)

    def __getPositionState(self, nftId, posId):
        core = self.__getCore()
        positionState = core.functions.positionStates(nftId, posId).call()
        abi = next(filter(lambda abis: FwxWeb3.filterFunctionABI(
            abis, FwxWeb3.POSITION_STATE_FUNCTION_NAME), core.abi))
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
