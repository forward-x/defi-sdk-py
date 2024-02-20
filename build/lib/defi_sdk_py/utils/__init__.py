from decimal import Decimal
from web3 import Web3

class TransactionReceipt:
    """
    A class representing a transaction receipt, containing details of a confirmed transaction.
    """
    def __init__(self, transactionHash, transactionIndex, blockHash, blockNumber, fromAddress, toAddress, cumulativeGasUsed, gasUsed, contractAddress, logs, status, logsBloom):
        """
        Initializes a TransactionReceipt object with transaction details.

        :param kwargs: A dictionary of transaction receipt details
        """
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
    """
    Parses the given value into its equivalent in wei, considering the token's decimals.

    :param web3: An instance of a Web3 connection
    :param value: The value to parse
    :param decimals: The number of decimals the token uses
    :return: The parsed value in wei as an integer
    """
    return web3.to_wei(Decimal(value * (10**decimal)), 'wei')

def MAX_UINT_256()->int:
    return (2**256) - 1

def Day()->int:
    return 86400

def Hour()->int:
    return 3600