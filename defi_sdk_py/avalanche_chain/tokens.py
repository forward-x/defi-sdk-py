from ..abi.IERC20Metadata import IERC20Metadata
from web3 import Web3

class Tokens:
    def __init__(self, web3: Web3):
        # Generate dynamic attributes based on the keys in the address_dict
        self.WAVAX:IERC20Metadata = IERC20Metadata('0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7', web3)
        self.FWX:IERC20Metadata = IERC20Metadata('0x9F0AfA63465606c4a9bD8543FF9FEDC7273F45d9', web3)
        self.USDC:IERC20Metadata = IERC20Metadata('0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E', web3)
        self.COQ:IERC20Metadata = IERC20Metadata('0x420FcA0121DC28039145009570975747295f2329', web3)
        self.SAVAX:IERC20Metadata = IERC20Metadata('0x2b2C81e08f1Af8835a78Bb2A90AE924ACE0eA4bE', web3)
