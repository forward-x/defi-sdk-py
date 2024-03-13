from ..abi.IERC20Metadata import IERC20Metadata
from web3 import Web3

class Tokens:
    def __init__(self, web3: Web3):
        # Generate dynamic attributes based on the keys in json address
        self.BTC:IERC20Metadata = IERC20Metadata('0xe0C84666a19D8d1EB4bB5D652C09c1E15755a3fc', web3)
        self.FWX:IERC20Metadata = IERC20Metadata('0xb93faf323f840b4dD8afAc5C7a1734107f7448b0', web3)
        self.ETH:IERC20Metadata = IERC20Metadata('0xd792B832C9f1Bf9bedE77422F2Cabf9a8b9964b8', web3)
        self.USDC:IERC20Metadata = IERC20Metadata('0x26a0417Aa86ED40750CBa69F9a2126473346224c', web3)
        self.WAVAX:IERC20Metadata = IERC20Metadata('0x45f42F0dA25906e5741a74CE418623E00739cc9A', web3)
        self.COQ:IERC20Metadata = IERC20Metadata('0x6d0874777F2b12f5711FEa9123d6C5bF221021A6', web3)

    def __str__(self):
        return self.address
