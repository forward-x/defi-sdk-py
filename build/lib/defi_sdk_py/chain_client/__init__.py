from web3 import Web3, HTTPProvider, types
from web3.middleware import geth_poa_middleware
from ..address_const import AddressConst

from ..core import Core
from ..pool import Pool
from ..membership import Membership
from ..stake_pool import StakePool
from ..library import Library
from ..helper_core import HelperCore
from ..helper_membership_and_stake_pool import HelperMembershipAndStakePool
from ..helper_pool import HelperPool
from ..helper_future_trade import HelperFutureTrade

from ..utils import Day, Decimal, Hour, MAX_UINT_256, parseEther,TransactionReceipt
from ..abi.IERC20Metadata import IERC20Metadata
from typing import Union
class ChainClient(Library, Core, Pool, Membership, StakePool, HelperCore, HelperMembershipAndStakePool, HelperPool, HelperFutureTrade):
    """
    Client for interacting with a blockchain via the Web3.py library.

    This client provides methods to connect to a blockchain node, send transactions, and query balances.

    :param rpc_url: URL of the blockchain node RPC interface
    :param private_key: Private key for signing transactions 
    :param address_const: Constants for blockchain addresses (more details in address constants module)
    :param maxFeePerGas: Maximum fee per gas willing to pay in wei
    :param maxPriorityFeePerGas: Priority fee per gas to incentivize miners
    """
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
        """
        Retrieves the balance of the default account.

        :return: The balance of the account in wei
        """
        return self.web3.eth.get_balance(self.address)

    def approve(self, token:IERC20Metadata, spender:str, amount:int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->TransactionReceipt:
        """
        Approves a spender to withdraw tokens from the default account.

        :param token: The token contract interface (can use with built-in ChainClient.TOKEN.<TOKEN_SYMBOL>)
        :param spender: The address of the spender
        :param amount: The amount of tokens to approve
        :param is_estimate: Whether to estimate the gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        amount = parseEther(self.web3, amount, token.decimals().call())
        contract_func = token.approve(spender, amount)
        return self.send_transaction(contract_func, 0, is_estimate)

    def send_transaction(self, abi_func, value:int=0, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Sends a transaction to the blockchain.

        :param abi_func: The contract function to call (ChainClient built-in)
        :param value: The value in wei to send with the transaction
        :param is_estimate: Whether to estimate the gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas
        """
        try:
            built_tx = abi_func.build_transaction(
                {
                    'gasPrice' : self.web3.eth.gas_price if gas_price == 0 else gas_price,
                    'value' : 0 if is_estimate else value,
                }
            )
            built_tx['nonce'] = self.web3.eth.get_transaction_count(self.address) if nonce == 0 else nonce
            built_tx['gas'] = built_tx['gas'] if gas == 0 else gas
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
    
    # Day, Decimal, Hour, MAX_UINT_256, parseEther

    def day(self):
        return Day()

    def hour(self):
        return Hour()
    
    def max_uint_256(self):
        return MAX_UINT_256()
    
    def parseEther(self, value:int, decimal:int=18):
        return parseEther(self.web3, value, decimal)
