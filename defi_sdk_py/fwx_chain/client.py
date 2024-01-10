from ..chain_client import ChainClient
from ..address import AddressConst
from ..abi.IERC20Metadata import IERC20Metadata
from web3 import Web3



class Tokens:
    def __init__(self, web3: Web3, address_dict:dict):
        self.BTC = IERC20Metadata(address_dict["BTC"],web3)
        self.WBNB = IERC20Metadata(address_dict["WBNB"],web3)
        self.BUSD = IERC20Metadata(address_dict["BUSD"],web3)
        self.USDT = IERC20Metadata(address_dict["USDT"],web3)
        self.FWX = IERC20Metadata(address_dict["FWX"],web3)
        self.ETH = IERC20Metadata(address_dict["ETH"],web3)


class FWXChainClient:
    def __init__(self, rpc_url: str, private_key: str, address_const: AddressConst):
        self.client:ChainClient = ChainClient(rpc_url,private_key,address_const)
        self.TOKEN:Tokens = Tokens(self.client.web3, self.client.address.get_tokens_address())
