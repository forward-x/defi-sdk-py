import web3

import defi_sdk_py

class FwxWeb3:
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
    def openPosition(self, isLong, collateral, underlying, nftId, entryPrice, contractSize, leverage, slippage):
        pass
    

    # closePosition
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - posId: BigNumberish
    #     - closingSize: BigNumberish
    # - **Output**
    #     - result: CoreBase.Position (struct from solidity)
    def closePosition(self, nftId, posId, closingSize):
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
    def depositCollateral(self, collateral, underlying, nftId, amount):
        validatePair(collateral,underlying)
        collateralDecimal = self.__getTokenDecimal(collateral)
        amount = int(amount * collateralDecimal)
        IAPHCore = self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["CORE"], abi=defi_sdk_py.IAPHCORE_ABI)
        IAPHLibrary = self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["APH_LIBRARY"], abi=defi_sdk_py.IAPHLIBRARY_ABI)
        tx = IAPHCore.functions.depositCollateral(nftId, defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateral], defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlying], amount).buildTransaction( 
            {
                'from': self.signer.address,
                'nonce': self.w3.eth.get_transaction_count(self.signer.address),
                'gas': 1300000,
                'gasPrice': self.w3.toWei(25, 'gwei'),
            }
        )

        # Sign tx
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(tx_hash)
        pairByte = IAPHLibrary.functions.hashPair(
                defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateral],
                defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlying],
                ).call()
        balance = IAPHCore.functions.wallets(nftId, pairByte).call()
        return balance / collateralDecimal


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
    def withdrawCollateral(self, collateral, underlying, nftId, amount):
        validatePair(collateral,underlying)
        collateralDecimal = self.__getTokenDecimal(collateral)
        amount = int(amount * collateralDecimal)
        IAPHCore = self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["CORE"], abi=defi_sdk_py.IAPHCORE_ABI)
        IAPHLibrary = self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["APH_LIBRARY"], abi=defi_sdk_py.IAPHLIBRARY_ABI)
        tx = IAPHCore.functions.withdrawCollateral(nftId, defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateral], defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlying], amount).buildTransaction( 
            {
                'from': self.signer.address,
                'nonce': self.w3.eth.get_transaction_count(self.signer.address),
                'gas': 1300000,
                'gasPrice': self.w3.toWei(25, 'gwei'),
            }
        )

        # Sign tx
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(tx_hash)
        pairByte = IAPHLibrary.functions.hashPair(
                defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateral],
                defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlying],
                ).call()
        balance = IAPHCore.functions.wallets(nftId, pairByte).call()
        return balance / collateralDecimal


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
        IAPHCore = self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["CORE"], abi=defi_sdk_py.IAPHCORE_ABI)
        for pair in pairs:
            collateralTokenSymbol = pair["collateral"]
            underlyingTokenSymbol = pair["underlying"]
            validatePair(collateralTokenSymbol,underlyingTokenSymbol)
            position = self.__getPositionInfo(nftId, collateralTokenSymbol, underlyingTokenSymbol)
            if position["id"] != 0:
                activePositions.append(position)
        return activePositions

    def __getPositionInfo(self, nftId, collateralTokenSymbol, underlyingTokenSymbol):
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        underlyingDecimal = self.__getTokenDecimal(underlyingTokenSymbol)
        positionOutput = self.__getPosition(nftId, collateralTokenSymbol, underlyingTokenSymbol)
        positionStateOutput = self.__getPositionStateInfo(nftId, positionOutput["positions"]["id"])
        if positionStateOutput["isLong"]:
            pass
        else:
            pass
        if positionOutput["positions"]["id"] == 0:
            return {
            "id": 0,
            "entryPrice": 0,
            "contractSize": 0,
            "borrowAmount": 0,
            "collateralUsed": 0,
            "interestOwed": 0,
            "interestOwedPerDay": 0,
            "lastSettleTimestamp": 0,
            }
        borrowingDecimal = collateralDecimal if positionStateOutput["isLong"] else underlyingDecimal
        position = {
            "id": positionOutput["positions"]["id"],
            "entryPrice": positionOutput["positions"]["entryPrice"] / 10**collateralDecimal,
            "contractSize": positionOutput["positions"]["contractSize"] / 10**borrowingDecimal,
            "borrowAmount": positionOutput["positions"]["borrowAmount"] / 10**borrowingDecimal,
            "collateralUsed": positionOutput["positions"]["collateralSwappedAmount"] / 10**collateralDecimal,
            "interestOwed": positionOutput["positions"]["interestOwed"] / 10**borrowingDecimal,
            "interestOwedPerDay": positionOutput["positions"]["interestOwePerDay"] / 10**borrowingDecimal,
            "lastSettleTimestamp": positionOutput["positions"]["lastSettleTimestamp"],
            }
        return position

    def __getPositionStateInfo(self, nftId, posId):
        positionStateOutput = self.__getPositionState(nftId,posId)
        pair = self.__getPair(positionStateOutput["positionStates"]["pairByte"])
        if positionStateOutput["positionStates"]["pairByte"] == 0:
            return {
                "active": 0,
                "isLong": 0,
                "PNL": 0,
                "averageEntryPrice": 0,
                "startTimestamp": 0,
                "interestPaid": 0,
                "totalSwapFeePaid": 0,
                "totalTradingFeePaid": 0,
            }
        
        collateralDecimal = self.__getTokenDecimalFromAddress(pair["collateralAddress"])
        underlyingDecimal = self.__getTokenDecimalFromAddress(pair["underlyingAddress"])
        borrowingDecimal = collateralDecimal if positionStateOutput["positionStates"]["isLong"] else underlyingDecimal
        positionState = {
                "active": positionStateOutput["positionStates"]["active"],
                "isLong": positionStateOutput["positionStates"]["isLong"],
                "PNL": positionStateOutput["positionStates"]["PNL"] / 10**18,
                "averageEntryPrice": positionStateOutput["positionStates"]["averageEntryPrice"] / 10**collateralDecimal,
                "startTimestamp": positionStateOutput["positionStates"]["startTimestamp"],
                "interestPaid": positionStateOutput["positionStates"]["interestPaid"] / 10**borrowingDecimal,
                "totalSwapFeePaid": positionStateOutput["positionStates"]["totalSwapFee"] / 10**borrowingDecimal,
                "totalTradingFeePaid": positionStateOutput["positionStates"]["totalTradingFee"] / 10**collateralDecimal,
            }
        return positionState

    def __getPosition(self, nftId, collateralTokenSymbol, underlyingTokenSymbol):
        IAPHLibrary = self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["APH_LIBRARY"], abi=defi_sdk_py.IAPHLIBRARY_ABI)
        IAPHCore = self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["CORE"], abi=defi_sdk_py.IAPHCORE_ABI)
        pairByte = IAPHLibrary.functions.hashPair(
                defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
                defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol],
                ).call()
        position = IAPHCore.functions.positions(nftId, pairByte).call()
        abi = next(filter(lambda abis: FwxWeb3.filterFunctionABI(abis, "positions"),IAPHCore.abi))
        return FwxWeb3.tupleOutputDecode(position, abi)

    def __getPositionState(self, nftId, posId):
        IAPHCore = self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["CORE"], abi=defi_sdk_py.IAPHCORE_ABI)
        positionState = IAPHCore.functions.positionStates(nftId, posId).call()
        abi = next(filter(lambda abis: FwxWeb3.filterFunctionABI(abis, "positionStates"),IAPHCore.abi))
        return FwxWeb3.tupleOutputDecode(positionState, abi)

    def __getPair(self, pairByte):
        IAPHCore = self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["CORE"], abi=defi_sdk_py.IAPHCORE_ABI)
        pair = IAPHCore.functions.pairs(pairByte).call()
        return {"collateralAddress":pair[0],"underlyingAddress":pair[1]}

    def __getTokenDecimal(self, tokenSymbol):
        IERC20 = self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][tokenSymbol], abi=defi_sdk_py.IERC20_ABI)
        decimal = IERC20.functions.decimals().call()
        return decimal

    def __getTokenDecimalFromAddress(self, tokenAddress):
        IERC20 = self.w3.eth.contract(address=tokenAddress, abi=defi_sdk_py.IERC20_ABI)
        decimal = IERC20.functions.decimals().call()
        return decimal


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


class FwxWebsocketProvider(web3.WebsocketProvider):
    pass

def getClient(url):
    return FwxWeb3(url)

def validatePair(collateral,underlying):
    assert collateral != underlying, "same collateral and underlying token"
    assert collateral in defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"], "collateral not allowed"
    assert underlying in defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"], "underlying not allowed"
