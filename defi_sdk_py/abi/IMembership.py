
class IMembership:
    def __init__(self, contract_address, web3):
        """
        Initialize the contract instance.

        :param contract_address: The Ethereum address of the contract.
        :type contract_address: str
        :param web3: The Web3 instance for interacting with Ethereum.
        :type web3: Web3
        """
        self.contract:Web3.eth.contract = web3.eth.contract(address=contract_address, abi=[{'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'approved', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'ApprovalForAll', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'approve', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'currentPool', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'getApproved', 'outputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'getDefaultMembership', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getPoolLists', 'outputs': [{'internalType': 'address[]', 'name': '', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'getPreviousPool', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'getRank', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'pool', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'getRank', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'getReferrer', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'operator', 'type': 'address'}], 'name': 'isApprovedForAll', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'referalId', 'type': 'uint256'}], 'name': 'mint', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'ownerOf', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'pause', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'safeTransferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'safeTransferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'bool', 'name': '_approved', 'type': 'bool'}], 'name': 'setApprovalForAll', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'string', 'name': 'baseTokenURI', 'type': 'string'}], 'name': 'setBaseURI', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'setDefaultMembership', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'newPool', 'type': 'address'}], 'name': 'setNewPool', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'index', 'type': 'uint256'}], 'name': 'tokenByIndex', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'uint256', 'name': 'index', 'type': 'uint256'}], 'name': 'tokenOfOwnerByIndex', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'unpause', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'newRank', 'type': 'uint8'}], 'name': 'updateRank', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'usableTokenId', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}])
        self.web3:Web3 = web3
        self.address = contract_address

    # Generated functions
    
    def eventApproval(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.Approval().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def eventApprovalForAll(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.ApprovalForAll().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def eventTransfer(self, fromBlock:int=0, toBlock:int=0):
        return self.contract.events.Transfer().get_logs(fromBlock=self.web3.eth.block_number if fromBlock == 0 else fromBlock, toBlock=self.web3.eth.block_number if toBlock == 0 else toBlock)

    def approve(self, to: str, tokenId: int):
        return self.contract.functions.approve(to, tokenId).call()

    def balanceOf(self, owner: str):
        return self.contract.functions.balanceOf(owner).call()

    def currentPool(self, ):
        return self.contract.functions.currentPool().call()

    def getApproved(self, tokenId: int):
        return self.contract.functions.getApproved(tokenId).call()

    def getDefaultMembership(self, owner: str):
        return self.contract.functions.getDefaultMembership(owner).call()

    def getPoolLists(self, ):
        return self.contract.functions.getPoolLists().call()

    def getPreviousPool(self, ):
        return self.contract.functions.getPreviousPool().call()

    def getRank(self, tokenId: int):
        return self.contract.functions.getRank(tokenId).call()

    def getRank(self, pool: str, tokenId: int):
        return self.contract.functions.getRank(pool, tokenId).call()

    def getReferrer(self, tokenId: int):
        return self.contract.functions.getReferrer(tokenId).call()

    def isApprovedForAll(self, owner: str, operator: str):
        return self.contract.functions.isApprovedForAll(owner, operator).call()

    def mint(self, referalId: int):
        return self.contract.functions.mint(referalId).call()

    def ownerOf(self, arg0: int):
        return self.contract.functions.ownerOf(arg0).call()

    def pause(self, ):
        return self.contract.functions.pause().call()

    def safeTransferFrom(self, _from: str, to: str, tokenId: int):
        return self.contract.functions.safeTransferFrom(_from, to, tokenId).call()

    def safeTransferFrom(self, _from: str, to: str, tokenId: int, data: str):
        return self.contract.functions.safeTransferFrom(_from, to, tokenId, data).call()

    def setApprovalForAll(self, operator: str, _approved: str):
        return self.contract.functions.setApprovalForAll(operator, _approved).call()

    def setBaseURI(self, baseTokenURI: str):
        return self.contract.functions.setBaseURI(baseTokenURI).call()

    def setDefaultMembership(self, tokenId: int):
        return self.contract.functions.setDefaultMembership(tokenId).call()

    def setNewPool(self, newPool: str):
        return self.contract.functions.setNewPool(newPool).call()

    def supportsInterface(self, interfaceId: str):
        return self.contract.functions.supportsInterface(interfaceId).call()

    def tokenByIndex(self, index: int):
        return self.contract.functions.tokenByIndex(index).call()

    def tokenOfOwnerByIndex(self, owner: str, index: int):
        return self.contract.functions.tokenOfOwnerByIndex(owner, index).call()

    def totalSupply(self, ):
        return self.contract.functions.totalSupply().call()

    def transferFrom(self, _from: str, to: str, tokenId: int):
        return self.contract.functions.transferFrom(_from, to, tokenId).call()

    def unpause(self, ):
        return self.contract.functions.unpause().call()

    def updateRank(self, tokenId: int, newRank: int):
        return self.contract.functions.updateRank(tokenId, newRank).call()

    def usableTokenId(self, owner: str, tokenId: int):
        return self.contract.functions.usableTokenId(owner, tokenId).call()
