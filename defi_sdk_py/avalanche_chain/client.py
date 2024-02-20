from ..chain_client import ChainClient
from ..address_const import AddressConst
from web3 import Web3
from .tokens import Tokens
from .pools import Pools

class AvalancheChainClient(ChainClient):

    def __init__(
        self,
        rpc_url: str,
        private_key: str,
        address_const: AddressConst,
        maxFeePerGas:int,
        maxPriorityFeePerGas:int
    ):
        super().__init__(rpc_url, private_key, address_const, maxFeePerGas,maxPriorityFeePerGas)
        self.TOKEN:Tokens = Tokens(self.web3)
        self.POOLS:Pools = Pools(self.web3)
        self.native = self.TOKEN.WBNB