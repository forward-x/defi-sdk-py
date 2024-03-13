from ..abi.IERC20Metadata import IERC20Metadata
from web3 import Web3

class Tokens:
    def __init__(self, web3: Web3):
        # Generate dynamic attributes based on the keys in the address_dict
        self.BTC:IERC20Metadata = IERC20Metadata('0xdC6Aa912093A32BE700b8F4c0DdFF843c0e72597', web3)
        self.WBNB:IERC20Metadata = IERC20Metadata('0xe5e9c0642f74C01dF7cA4f82b151E211A3d9C739', web3)
        self.BUSD:IERC20Metadata = IERC20Metadata('0xF13060533f23B261e7B2b3843eCFC46AA935a182', web3)
        self.USDT:IERC20Metadata = IERC20Metadata('0x809ABB78e06b46fFd2Fa38169D92db12b33A2d2C', web3)
        self.FWX:IERC20Metadata = IERC20Metadata('0x0d1CE7e2B7a0ecEa6bE5e75532211a89572ebDE1', web3)
        self.ETH:IERC20Metadata = IERC20Metadata('0x7C175D30afcb368193FCeDeb10e4ecb4033658F0', web3)
