import web3

import defi_sdk_py

class FwxWeb3:
    def __init__(self, url):
        self.w3 = web3.Web3(web3.HTTPProvider(url))

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
    #         - lastSettleTimstamp: BigNumberish
    def getAllActivePosition(self, nftId, pairs):
        activePositions = []
        IAPHLibrary = self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["APH_LIBRARY"], abi=defi_sdk_py.IAPHLIBRARY_ABI)
        IAPHCore = self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["CORE"], abi=defi_sdk_py.IAPHCORE_ABI)
        for pair in pairs:
            collateralTokenSymbol = pair["collateral"]
            underlyingTokenSymbol = pair["underlying"]
            validatePair(collateralTokenSymbol,underlyingTokenSymbol)
            pairByte = IAPHLibrary.functions.hashPair(
                    defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
                    defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol],
                    ).call()
            position = IAPHCore.functions.positions(nftId, pairByte).call()
            abi = next(filter(lambda abis: FwxWeb3.filterFunctionABI(abis, "positions"),IAPHCore.abi))
            output = FwxWeb3.tupleOutputDecode(position, abi)
            if output["positions"]["id"] != 0:
                position = {
                    "id": output["positions"]["id"],
                    "entryPrice": output["positions"]["entryPrice"],
                    "contractSize": output["positions"]["contractSize"],
                    "borrowAmount": output["positions"]["borrowAmount"],
                    "collateralUsed": output["positions"]["collateralSwappedAmount"],
                    "interestOwed": output["positions"]["interestOwed"],
                    "interestOwedPerDay": output["positions"]["interestOwePerDay"],
                    "lastSettleTimestamp": output["positions"]["lastSettleTimestamp"],
                    }
                activePositions.append(position)
        return activePositions

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
