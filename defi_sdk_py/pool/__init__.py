from ..abi.IAPHPool import *
from ..abi.IERC20Metadata import IERC20Metadata
from ..utils import parseEther, TransactionReceipt
from typing import Union
class Pool:
    """
    Pool provides functionality to interact with the pool smart contracts.
    """
    def __init__(self):
        """
        Initializes the Pool class.
        """
        super().__init__()

    def token_address(self, pool:IAPHPool)->str:
        """
        Retrieves the token address of the specified pool.

        :param pool: The pool contract interface
        :return: The token address as a string
        """

        return pool.tokenAddress().call()

    def lenders(self, pool:IAPHPool, nft_id:int)->Lend:
        """
        Retrieves the lending details for a given NFT ID in the specified pool.

        :param pool: The pool contract interface
        :param nft_id: The NFT ID to query for lending details
        :return: A Lend object containing the lending details
        """
        return Lend(*(pool.lenders(nft_id).call()))

    def token_holders(self, pool:IAPHPool, nft_id:int)->PoolTokens:
        """
        Retrieves the token holder details for a given NFT ID in the specified pool.

        :param pool: The pool contract interface
        :param nft_id: The NFT ID to query for token holder details
        :return: A PoolTokens object containing the token holder details
        """

        return PoolTokens(*(pool.tokenHolders(nft_id).call()))

    def current_supply(self, pool:IAPHPool):
        """
        Retrieves the current supply of the specified pool.

        :param pool: The pool contract interface
        :return: The current supply as an integer
        """

        return pool.currentSupply().call()
    
    def get_next_borrowing_interest(self, pool:IAPHPool, borrow_amount:int)->int:
        """
        Calculates the next borrowing interest for a specified borrow amount in the pool.

        :param pool: The pool contract interface
        :param borrow_amount: The borrow amount to query for interest
        :return: The next borrowing interest as an integer
        """
        token:IERC20Metadata = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        borrow_amount = parseEther(self.web3, borrow_amount, token.decimals().call())
        return pool.getNextBorrowingInterest(borrow_amount).call()

    # ACTION
    def deposit(self, pool:IAPHPool, nft_id: int, amount: int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Deposits an amount into the specified pool.

        :param pool: The pool contract interface
        :param nft_id: The NFT ID associated with the deposit
        :param amount: The amount to deposit
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        token:IERC20Metadata = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        amount = parseEther(self.web3, amount, token.decimals().call())
        is_native = self.native.address == token.address
        contract_func = pool.deposit(nft_id, amount)
        return self.send_transaction(contract_func, value=amount if is_native else 0, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)


    def deposit_event_tx(self, pool:IAPHPool, tx_hash:str)->DepositEvent:
        """
        Retrieves the deposit event details by transaction hash.

        :param pool: The pool contract interface
        :param tx_hash: The transaction hash to query for deposit event
        :return: A DepositEvent object containing the deposit event details
        """
        return pool.event_deposit_by_tx(tx_hash)
        
    def deposit_event_block(self, pool:IAPHPool, from_block:int=0, to_block:int=0)->List[DepositEvent]:
        """
        Retrieves a list of deposit event details within a block range.

        :param pool: The pool contract interface
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of DepositEvent objects containing the deposit event details
        """
        return [DepositEvent(i) for i in pool.event_deposit_by_block(from_block, to_block)]

    def activate_rank_event_tx(self, pool:IAPHPool, tx_hash:str)->ActivateRankEvent:
        """ 
        Retrieves the activate rank event details by transaction hash.

        :param pool: The pool contract interface
        :param tx_hash: The transaction hash to query for activate rank event
        :return: An ActivateRankEvent object containing the activate rank event details
        """
        return pool.event_activaterank_by_tx(tx_hash)
        
    def activate_rank_event_block(self, pool:IAPHPool, from_block:int=0, to_block:int=0)->List[ActivateRankEvent]:
        """
        Retrieves a list of activate rank event details within a block range.

        :param pool: The pool contract interface
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of ActivateRankEvent objects containing the activate rank event details
        """
        return [ActivateRankEvent(i) for i in pool.event_activaterank_by_block(from_block, to_block)]

    def borrow_event_tx(self, pool:IAPHPool, tx_hash:str)->BorrowEvent:
        """
        Retrieves the borrow event details by transaction hash.

        :param pool: The pool contract interface
        :param tx_hash: The transaction hash to query for borrow event
        :return: A BorrowEvent object containing the borrow event details
        """

        return pool.event_borrow_by_tx(tx_hash)
        
    def borrow_event_block(self, pool:IAPHPool, from_block:int=0, to_block:int=0)->List[BorrowEvent]:
        """
        Retrieves a list of borrow event details within a block range.

        :param pool: The pool contract interface
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of BorrowEvent objects containing the borrow event details
        """
        return [BorrowEvent(i) for i in pool.event_borrow_by_block(from_block, to_block)]

    def claim_forw_interest_event_tx(self, pool:IAPHPool, tx_hash:str)->ClaimForwInterestEvent:
        """
        Retrieves the claim forward interest event details by transaction hash.

        :param pool: The pool contract interface
        :param tx_hash: The transaction hash to query for claim forward interest event
        :return: A ClaimForwInterestEvent object containing the claim forward interest event details
        """

        return pool.event_claimforwinterest_by_tx(tx_hash)
        
    def claim_forw_interest_event_block(self, pool:IAPHPool, from_block:int=0, to_block:int=0)->List[ClaimForwInterestEvent]:
        """
        Retrieves a list of claim forward interest event details within a block range.

        :param pool: The pool contract interface
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of ClaimForwInterestEvent objects containing the claim forward interest event details
        """
        return [ClaimForwInterestEvent(i) for i in pool.event_claimforwinterest_by_block(from_block, to_block)]

    def claim_token_interest_event_tx(self, pool:IAPHPool, tx_hash:str)->ClaimTokenInterestEvent:
        """
        Retrieves the claim token interest event details by transaction hash.

        :param pool: The pool contract interface
        :param tx_hash: The transaction hash to query for claim token interest event
        :return: A ClaimTokenInterestEvent object containing the claim token interest event details
        """

        return pool.event_claimtokeninterest_by_tx(tx_hash)
        
    def claim_token_interest_event_block(self, pool:IAPHPool, from_block:int=0, to_block:int=0)->List[ClaimTokenInterestEvent]:
        """
        Retrieves a list of claim token interest event details within a block range.

        :param pool: The pool contract interface
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of ClaimTokenInterestEvent objects containing the claim token interest event details
        """
        return [ClaimForwInterestEvent(i) for i in pool.event_claimtokeninterest_by_block(from_block, to_block)]

    def claim_withdraw_event_tx(self, pool:IAPHPool, tx_hash:str)->WithdrawEvent:
        """
        Retrieves the withdraw event details by transaction hash.

        :param pool: The pool contract interface
        :param tx_hash: The transaction hash to query for withdraw event
        :return: A WithdrawEvent object containing the withdraw event details
        """
        return pool.event_withdraw_by_tx(tx_hash)
        
    def claim_withdraw_event_block(self, pool:IAPHPool, from_block:int=0, to_block:int=0)->List[WithdrawEvent]:
        """
        Retrieves a list of withdraw event details within a block range.

        :param pool: The pool contract interface
        :param from_block: The starting block number
        :param to_block: The ending block number
        :return: A list of WithdrawEvent objects containing the withdraw event details
        """
        return [ClaimForwInterestEvent(i) for i in pool.event_withdraw_by_block(from_block, to_block)]

    def withdraw(self, pool:IAPHPool, nft_id: int, amount: int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Withdraws an amount from the specified pool.

        :param pool: The pool contract interface
        :param nft_id: The NFT ID associated with the withdrawal
        :param amount: The amount to withdraw
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        token:IERC20Metadata = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        amount = parseEther(self.web3, amount, token.decimals().call())
        contract_func = pool.withdraw(nft_id, amount)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)
    
    def active_rank(self, pool:IAPHPool, nft_id: int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Activates the rank for a given NFT ID in the specified pool.

        :param pool: The pool contract interface
        :param nft_id: The NFT ID for which to activate the rank
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        contract_func = pool.activateRank(nft_id)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def claim_all_interest(self, pool:IAPHPool, nft_id: int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Claims all interest for a given NFT ID in the specified pool.

        :param pool: The pool contract interface
        :param nft_id: The NFT ID for which to claim all interest
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        contract_func = pool.claimAllInterest(nft_id)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def claim_token_interest(self, pool:IAPHPool, nft_id: int, amount:int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Claims token interest for a given NFT ID in the specified pool.

        :param pool: The pool contract interface
        :param nft_id: The NFT ID for which to claim token interest
        :param amount: The amount of token interest to claim
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        token:IERC20Metadata = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        amount = parseEther(self.web3, amount, token.decimals().call())
        contract_func = pool.claimTokenInterest(nft_id, amount)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def claim_forw_interest(self, pool:IAPHPool, nft_id: int, amount:int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Claims forward interest for a given NFT ID in the specified pool.

        :param pool: The pool contract interface
        :param nft_id: The NFT ID for which to claim forward interest
        :param amount: The amount of forward interest to claim
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        forw_token:IERC20Metadata = IERC20Metadata(pool.forwAddress().call(), self.web3)
        amount = parseEther(self.web3, amount, forw_token.decimals().call())
        contract_func = pool.claimForwInterest(nft_id, amount)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def borrow(self, pool:IAPHPool, nft_id:int, loan_id:int, borrow_amount:int, collateral_sent_amount:int, collateral_token:IERC20Metadata, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        """
        Initiates a borrowing transaction in the specified pool.

        :param pool: The pool contract interface
        :param nft_id: The NFT ID associated with the borrowing
        :param loan_id: The loan ID for the borrowing
        :param borrow_amount: The amount to borrow
        :param collateral_sent_amount: The amount of collateral sent
        :param collateral_token: The collateral token metadata
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        borrow_token:IERC20Metadata = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        borrow_amount = parseEther(self.web3, borrow_amount, borrow_token.decimals().call())
        collateral_sent_amount = parseEther(self.web3, collateral_sent_amount, collateral_token.decimals().call())
        is_native = self.native.address == collateral_token.address
        contract_func = pool.borrow(loan_id, nft_id, borrow_amount, collateral_sent_amount, collateral_token.address)
        return self.send_transaction(contract_func, value=collateral_sent_amount if is_native else 0, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def open_position(self, nft_id:int, is_long:bool, collateral_token:IERC20Metadata, underlying_token:IERC20Metadata, entry_price:int, size:int, leverage:int, slip_page:int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0):
        """
        Opens a new position in the specified pool.

        :param nft_id: The NFT ID associated with the position
        :param is_long: A boolean indicating if the position is long (True) or short (False)
        :param collateral_token: The collateral token metadata
        :param underlying_token: The underlying token metadata
        :param entry_price: The entry price for the position
        :param size: The size of the position
        :param leverage: The leverage for the position
        :param slip_page: The slippage percentage
        :param is_estimate: If True, returns the estimated gas for the transaction
        :param gas: The gas limit for the transaction
        :param gas_price: The gas price for the transaction
        :param nonce: The nonce for the transaction
        :return: The transaction receipt if not estimating gas, otherwise the estimated gas
        """
        token_of_pool = collateral_token if is_long else underlying_token
        selected_pool = [getattr(self.POOLS, pool) for pool in [i for i in self.POOLS.__dir__() if "_" not in i]]
        if len(selected_pool) == 0:
            raise Exception("token-not-allow-in-collateral-whitelist")
        selected_pool = [i for i in selected_pool if i.tokenAddress().call() == token_of_pool.address]
        if len(selected_pool) == 0:
            raise Exception("token-not-allow-in-collateral-whitelist")
        pool:IAPHPool = selected_pool[0]
        entry_price = parseEther(self.web3, entry_price, collateral_token.decimals().call())
        size = parseEther(self.web3, size, underlying_token.decimals().call())
        leverage = parseEther(self.web3, leverage)
        slip_page = parseEther(self.web3, slip_page)
        contract_func = pool.openPosition(
            nftId=nft_id,
            collateralTokenAddress=collateral_token.address,
            swapTokenAddress=underlying_token.address if is_long else collateral_token.address,
            entryPrice=entry_price,
            contractSize=size,
            leverage=leverage,
            slippage=slip_page
        )
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)
    


    