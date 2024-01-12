from decimal import Decimal
from web3 import Web3

class TransactionReceipt:
    def __init__(self, transactionHash, transactionIndex, blockHash, blockNumber, fromAddress, toAddress, cumulativeGasUsed, gasUsed, contractAddress, logs, status, logsBloom):
        self.transactionHash = transactionHash
        self.transactionIndex = transactionIndex
        self.blockHash = blockHash
        self.blockNumber = blockNumber
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.cumulativeGasUsed = cumulativeGasUsed
        self.gasUsed = gasUsed
        self.contractAddress = contractAddress
        self.logs = logs
        self.status = status
        self.logsBloom = logsBloom

    def __repr__(self):
        return (
            f"TransactionReceipt("
            f"transactionHash={self.transactionHash!r}, "
            f"transactionIndex={self.transactionIndex!r}, "
            f"blockHash={self.blockHash!r}, "
            f"blockNumber={self.blockNumber!r}, "
            f"fromAddress={self.fromAddress!r}, "
            f"toAddress={self.toAddress!r}, "
            f"cumulativeGasUsed={self.cumulativeGasUsed!r}, "
            f"gasUsed={self.gasUsed!r}, "
            f"contractAddress={self.contractAddress!r}, "
            f"logs={self.logs!r}, "
            f"status={self.status!r}, "
            f"logsBloom={self.logsBloom!r})"
        )

def parseEther(web3:Web3,value, decimal:int=18):
    return web3.to_wei(Decimal(value * (10**decimal)), 'wei')