
class APHLibrary:
    def __init__(self, contract_address, web3):
        """
        Initialize the contract instance.

        :param contract_address: The Ethereum address of the contract.
        :type contract_address: str
        :param web3: The Web3 instance for interacting with Ethereum.
        :type web3: Web3
        """
        self.contract:Web3.eth.contract = web3.eth.contract(address=contract_address, abi=[{'inputs': [{'internalType': 'uint256', 'name': 'a', 'type': 'uint256'}, {'internalType': 'int256', 'name': 'b', 'type': 'int256'}], 'name': 'addIntToUint', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'pure', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'wallet', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'swappedCollateral', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestOwed', 'type': 'uint256'}, {'internalType': 'int256', 'name': 'PNL', 'type': 'int256'}, {'internalType': 'uint256', 'name': 'positionSize', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'feeAmount', 'type': 'uint256'}], 'name': 'calculateMargin', 'outputs': [{'internalType': 'uint256', 'name': 'result', 'type': 'uint256'}], 'stateMutability': 'pure', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'firstValue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'secondValue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'multiplier', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'divisor', 'type': 'uint256'}], 'name': 'calculatePNL', 'outputs': [{'internalType': 'int256', 'name': '', 'type': 'int256'}], 'stateMutability': 'pure', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'collateralTokenAddress', 'type': 'address'}, {'internalType': 'address', 'name': 'underlyingTokenAddress', 'type': 'address'}], 'name': 'hashPair', 'outputs': [{'internalType': 'bytes32', 'name': 'pairByte', 'type': 'bytes32'}], 'stateMutability': 'pure', 'type': 'function'}])
        self.web3:Web3 = web3
        self.address = contract_address

    def __str__(self):
        return self.address

    # Generated functions
    
    def addIntToUint(self, a: int, b: str):
        return self.contract.functions.addIntToUint(a, b).call()

    def calculateMargin(self, wallet: int, swappedCollateral: int, interestOwed: int, PNL: str, positionSize: int, feeAmount: int):
        return self.contract.functions.calculateMargin(wallet, swappedCollateral, interestOwed, PNL, positionSize, feeAmount).call()

    def calculatePNL(self, firstValue: int, secondValue: int, multiplier: int, divisor: int):
        return self.contract.functions.calculatePNL(firstValue, secondValue, multiplier, divisor).call()

    def hashPair(self, collateralTokenAddress: str, underlyingTokenAddress: str):
        return self.contract.functions.hashPair(collateralTokenAddress, underlyingTokenAddress).call()
