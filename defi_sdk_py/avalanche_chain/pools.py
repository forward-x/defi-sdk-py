from ..abi.IAPHPool import IAPHPool
from web3 import Web3

class Pools:
    def __init__(self, web3: Web3):
        # Generate dynamic attributes based on the keys in json address
        self.WAVAX:IAPHPool = IAPHPool('0x7F91272ff1A0114743D2df95F5905F9613Fd92b3', web3)
        self.USDC:IAPHPool = IAPHPool('0x94732A5319e1feAcc7d08e08Fdc4C2c7f5123143', web3)
        self.CQO:IAPHPool = IAPHPool('0xc97d9B3971BfE1B8Ac8EA7f990Df721d8f695223', web3)
        self.SAVAX:IAPHPool = IAPHPool('0xe57a4042eA63Df072B2cf6352F9779E4D2445A92', web3)