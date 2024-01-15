
from web3 import Web3
from typing import Tuple, Dict, List
import json
#Generate a Python class representing the Ethereum contract.
#:param abi: The ABI (Application Binary Interface) of the contract.
#:type abi: list
#:param contract_name: The name of the contract class default is MyContract.
#:type contract_name: str
#:return: The generated Python class code.
#:rtype: str

class ApprovalEvent:
    def __init__(self, event_data):
        self.owner: str = event_data.get('owner')
        self.spender: str = event_data.get('spender')
        self.value: int = event_data.get('value')

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)


class TransferEvent:
    def __init__(self, event_data):
        self._from: str = event_data.get('_from')
        self.to: str = event_data.get('to')
        self.value: int = event_data.get('value')

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)




class IERC20Metadata:
    def __init__(self, contract_address, web3):
        """
        Initialize the contract instance.

        :param contract_address: The Ethereum address of the contract.
        :type contract_address: str
        :param web3: The Web3 instance for interacting with Ethereum.
        :type web3: Web3
        """
        self.contract:Web3.eth.contract = web3.eth.contract(address=contract_address, abi=[{'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}])
        self.web3:Web3 = web3
        self.address = contract_address

    def __str__(self):
        return self.address

    # Generated functions
    
    def event_approval_by_block(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.Approval().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def event_approval_by_tx(self, tx_hash:str):
        receipt = self.web3.eth.get_transaction_receipt(tx_hash)
        events = self.contract.events.Approval().process_receipt(receipt)
        if len(events) > 0:
            return events[0].args
        else:
            raise Exception('Event not found in transaction')


    def event_transfer_by_block(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.Transfer().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def event_transfer_by_tx(self, tx_hash:str):
        receipt = self.web3.eth.get_transaction_receipt(tx_hash)
        events = self.contract.events.Transfer().process_receipt(receipt)
        if len(events) > 0:
            return events[0].args
        else:
            raise Exception('Event not found in transaction')


    def allowance(self, owner: str, spender: str):
        return self.contract.functions.allowance(owner, spender)

    def approve(self, spender: str, amount: int):
        return self.contract.functions.approve(spender, amount)

    def balanceOf(self, account: str):
        return self.contract.functions.balanceOf(account)

    def decimals(self, ):
        return self.contract.functions.decimals()

    def name(self, ):
        return self.contract.functions.name()

    def symbol(self, ):
        return self.contract.functions.symbol()

    def totalSupply(self, ):
        return self.contract.functions.totalSupply()

    def transfer(self, to: str, amount: int):
        return self.contract.functions.transfer(to, amount)

    def transferFrom(self, _from: str, to: str, amount: int):
        return self.contract.functions.transferFrom(_from, to, amount)
