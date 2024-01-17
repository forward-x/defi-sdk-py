from web3 import Web3
from ..abi.APHLibrary import APHLibrary
from ..abi.IERC20Metadata import IERC20Metadata
from ..address_const import AddressConst
class Library:
    """
    Library provides utility functions and common logic for interacting with the blockchain.
    """

    def __init__(self):
        """
        Initializes the Library by setting up the library contract interface.
        """
        super(Library, self).__init__()
        self.library:APHLibrary = APHLibrary(self.address_const.get_library_address(), self.web3)

    def __str__(self)->str:
        """
        Returns the string representation of the library contract's address.

        :return: Library contract address as a string
        """
        return self.library.address
    
    def hash_pair(self, collateral_token_address:IERC20Metadata, underlying_token_address:IERC20Metadata)->str:
        """
        Computes the hash for a pair of tokens.

        :param collateral_token_address: The collateral token contract interface
        :param underlying_token_address: The underlying token contract interface
        :return: The hash of the token pair as a string
        """
        collateral_token_address = collateral_token_address.__str__()
        underlying_token_address = underlying_token_address.__str__()
        return "0x"+self.library.hashPair(collateral_token_address, underlying_token_address).call().hex()