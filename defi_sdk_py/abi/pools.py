from ..abi.IAPHPool import IAPHPool
from web3 import Web3

class Pool:
    def __init__(self, web3: Web3):
        # Generate dynamic attributes based on the keys in json address
        self.POOL.WBNB:IAPHPool = IAPHPool('0x7A6245162E2F51CEdc259Bd9D19ba91fb3B71ab3', web3)
        self.POOL.ETH:IAPHPool = IAPHPool('0x053E0D6D561cAb2aab9CB5e92E9574049471Fe61', web3)
        self.POOL.BTC:IAPHPool = IAPHPool('0x4746970CcE4dd47C183a698CA91EDa6730e8BBA9', web3)
        self.POOL.USDT:IAPHPool = IAPHPool('0x82bAb8815780F0FfE2DD8C559C19Cf42BBfc2d4A', web3)
        self.POOL.BUSD:IAPHPool = IAPHPool('0x922F2E0bbe9e83c20bDcd90e3A9c7b089bA32768', web3)

    def __str__(self):
        return self.address
# 