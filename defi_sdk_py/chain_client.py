from web3 import Web3, HTTPProvider
from .address import AddressConst

class ChainClient:

    def __init__(self, rpc_url: str, private_key: str, address_const: AddressConst):
        print("init chain client")
        self.rpc_url = rpc_url
        self.private_key = private_key
        self.web3 = self.connect_to_web3()
        self.address:AddressConst = address_const

    def connect_to_web3(self):
        print("try connecting to chain")
        web3: Web3 = Web3(HTTPProvider(self.rpc_url))
        web3.eth.default_account = web3.eth.account.from_key(self.private_key).address
        self.client = web3.eth.default_account
        if web3.is_connected():
            print(f"Connected to {self.rpc_url}")
        else:
            raise ConnectionError(f"Failed to connect to {self.rpc_url}")
        return web3
