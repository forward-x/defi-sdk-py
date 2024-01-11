from ..chain_client import ChainClient
from ..address import AddressConst
from web3 import Web3
from .tokens import Tokens
class FWXChainClient(ChainClient):
    def __init__(self, rpc_url: str, private_key: str, address_const: AddressConst):
        super().__init__(rpc_url, private_key, address_const)
        self.TOKEN:Tokens = Tokens(self.web3)