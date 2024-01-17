from ..chain_client import ChainClient
from ..address_const import AddressConst
from web3 import Web3
from .tokens import Tokens
from .pools import Pools

class FWXChainClient(ChainClient):
    """
    FWXChainClient is a client for interacting with the FWX blockchain.

    Args:
        rpc_url (str): The URL of the FWX blockchain RPC endpoint.
        private_key (str): The private key used for interacting with the blockchain.
        address_const (AddressConst): An instance of AddressConst containing relevant address constants.
        maxFeePerGas (int): The maximum fee per gas for transactions.
        maxPriorityFeePerGas (int): The maximum priority fee per gas for transactions.

    Attributes:
        TOKEN (Tokens): An instance of Tokens for interacting with tokens on the FWX blockchain.
        POOLS (Pools): An instance of Pools for interacting with liquidity pools on the FWX blockchain.
        native: Represents the native token (WBNB) on the FWX blockchain.

    Example:
        ```python
        from defi_sdk_py import FWXChainClient

        # Instantiate FWX Chain Client
        fwx_client = FWXChainClient(
            rpc_url="https://fwx.example.com/rpc",
            private_key="your_private_key",
            address_const=your_address_const_instance,
            maxFeePerGas=your_max_fee_per_gas,
            maxPriorityFeePerGas=your_max_priority_fee_per_gas
        )
        ```
    """

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