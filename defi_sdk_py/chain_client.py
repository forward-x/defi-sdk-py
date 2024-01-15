from web3 import Web3, HTTPProvider, types
from web3.middleware import geth_poa_middleware
from .address import AddressConst
from .core import Core
from .pool import Pool
from .membership import Membership
from .stake_pool import StakePool
from .library import Library
from .utils import TransactionReceipt,parseEther
from .abi.IERC20Metadata import IERC20Metadata
from typing import Union
class ChainClient(Library, Core, Pool, Membership, StakePool):

    def __init__(
        self,
        rpc_url: str,
        private_key: str,
        address_const: AddressConst,
        maxFeePerGas:int,
        maxPriorityFeePerGas:int
    ):
        print("init chain client")
        self.rpc_url = rpc_url
        self.private_key = private_key
        self.address_const:AddressConst = address_const
        self.web3 = self.connect_to_web3()
        self.maxFeePerGas=maxFeePerGas
        self.maxPriorityFeePerGas=maxPriorityFeePerGas
        super().__init__()

    def connect_to_web3(self):
        print("try connecting to chain")
        web3: Web3 = Web3(HTTPProvider(self.rpc_url))
        web3.eth.default_account = web3.eth.account.from_key(self.private_key).address
        web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.address = web3.eth.default_account
        if web3.is_connected():
            print(f"Connected to {self.rpc_url}")
        else:
            raise ConnectionError(f"Failed to connect to {self.rpc_url}")
        return web3
    
    def get_balance(self):
        return self.web3.eth.get_balance(self.address)

    def approve(self, token:IERC20Metadata, spender:str, amount:int, is_estimate=False)->TransactionReceipt:
        amount = parseEther(self.web3, amount, token.decimals().call())
        contract_func = token.approve(spender, amount)
        return self.send_transaction(contract_func, 0, is_estimate)

    def send_transaction(self, abi_func, value:int=0, is_estimate=False)->Union[TransactionReceipt, int]:
        try:
            built_tx = abi_func.build_transaction(
                {
                    'gasPrice' : self.web3.eth.gas_price,
                    'value' : 0 if is_estimate else value
                }
            )
            built_tx['nonce'] = self.web3.eth.get_transaction_count(self.address)
            if is_estimate:
                return self.web3.eth.estimate_gas(built_tx)
            signed_tx = self.web3.eth.account.sign_transaction(built_tx, self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            tx_receipt:types.TxReceipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            tx_receipt:TransactionReceipt = TransactionReceipt(
                transactionHash=tx_receipt.transactionHash.hex(),
                transactionIndex=tx_receipt.transactionIndex,
                blockHash=tx_receipt.blockHash.hex(),
                blockNumber=tx_receipt.blockNumber,
                fromAddress=tx_receipt["from"],
                toAddress=tx_receipt.to,
                cumulativeGasUsed=tx_receipt.cumulativeGasUsed,
                gasUsed=tx_receipt.gasUsed,
                contractAddress=tx_receipt.contractAddress,
                logs=tx_receipt.logs,  # This might need to be processed further if logs are complex objects
                status=tx_receipt.status,
                logsBloom=tx_receipt.logsBloom.hex()
            )
            return tx_receipt
        except Exception as err:
            raise err