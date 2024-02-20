from ..abi.IAPHPool import IAPHPool
from web3 import Web3

class Pools:
    def __init__(self, web3: Web3):
        # Generate dynamic attributes based on the keys in json address
        self.WAVAX:IAPHPool = IAPHPool('0xd5Ace308e8e2621796EeF1740996dC18b1307248', web3)
        self.ETH:IAPHPool = IAPHPool('0xD688C531770D36BC6b05F617De1CA7EA0116a452', web3)
        self.USDC:IAPHPool = IAPHPool('0x90A6452a352E70fdab9b6c8185DF575e682483F1', web3)
        self.BTC:IAPHPool = IAPHPool('0x11C0D17F633Ae1BCB3fF12E92835545846511B35', web3)
        self.COQ:IAPHPool = IAPHPool('0xf46cB6e4Bd835DDf9EeB47C5Ba70Cf773B9AEe80', web3)
