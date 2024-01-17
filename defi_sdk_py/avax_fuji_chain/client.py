from ..chain_client import ChainClient
from ..address_const import AddressConst
from .tokens import Tokens
from .pools import Pools
class AVAXFUJIChainClient(ChainClient):
    """
    AVAXFUJIChainClient is a client for interacting with the AVAX Fuji C-Chain.

    Args:
        rpc_url (str): The URL of the AVAX Fuji C-Chain RPC endpoint.
        private_key (str): The private key used for interacting with the blockchain.
        address_const (AddressConst): An instance of AddressConst containing relevant address constants.
        maxFeePerGas (int): The maximum fee per gas for transactions.
        maxPriorityFeePerGas (int): The maximum priority fee per gas for transactions.

    Attributes:
        TOKEN (Tokens): An instance of Tokens for interacting with tokens on the AVAX Fuji C-Chain.
        POOLS (Pools): An instance of Pools for interacting with liquidity pools on the AVAX Fuji C-Chain.
        native: Represents the native token (WAVAX) on the AVAX Fuji C-Chain.

    Example:
        ```python
        from defi_sdk_py import AVAXFUJIChainClient
        
        # Instantiate AVAX Fuji Chain Client
        avax_fuji_client = AVAXFUJIChainClient(
            rpc_url="https://fuji.avax.network/ext/bc/C/rpc",
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
        self.native = self.TOKEN.WAVAX