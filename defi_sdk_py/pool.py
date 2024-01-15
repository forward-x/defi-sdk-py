from .abi.IAPHPool import *
from .abi.IERC20Metadata import IERC20Metadata
from .utils import parseEther, TransactionReceipt
from typing import Union
class Pool:

    def __init__(self):
        super().__init__()

    def token_address(self, pool:IAPHPool)->str:
        return pool.tokenAddress().call()

    def lenders(self, pool:IAPHPool, nft_id:int)->Lend:
        return Lend(*(pool.lenders(nft_id).call()))

    def token_holders(self, pool:IAPHPool, nft_id:int)->PoolTokens:
        return PoolTokens(*(pool.tokenHolders(nft_id).call()))

    def current_supply(self, pool:IAPHPool):
        return pool.currentSupply().call()
    
    def get_next_borrowing_interest(self, pool:IAPHPool, borrow_amount:int)->int:
        token:IERC20Metadata = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        borrow_amount = parseEther(self.web3, borrow_amount, token.decimals().call())
        return pool.getNextBorrowingInterest(borrow_amount).call()

    # ACTION
    def deposit(self, pool:IAPHPool, nft_id: int, amount: int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        token:IERC20Metadata = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        amount = parseEther(self.web3, amount, token.decimals().call())
        is_native = self.native.address == token.address
        contract_func = pool.deposit(nft_id, amount)
        return self.send_transaction(contract_func, value=amount if is_native else 0, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)


    def deposit_event(self, pool:IAPHPool, tx_hash:str)->DepositEvent:
        return pool.event_deposit_by_tx(tx_hash)

    def withdraw(self, pool:IAPHPool, nft_id: int, amount: int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        token:IERC20Metadata = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        amount = parseEther(self.web3, amount, token.decimals().call())
        contract_func = pool.withdraw(nft_id, amount)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)
    
    def active_rank(self, pool:IAPHPool, nft_id: int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        contract_func = pool.activateRank(nft_id)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def claim_all_interest(self, pool:IAPHPool, nft_id: int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        contract_func = pool.claimAllInterest(nft_id)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def claim_token_interest(self, pool:IAPHPool, nft_id: int, amount:int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        token:IERC20Metadata = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        amount = parseEther(self.web3, amount, token.decimals().call())
        contract_func = pool.claimTokenInterest(nft_id, amount)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def claim_forw_interest(self, pool:IAPHPool, nft_id: int, amount:int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        forw_token:IERC20Metadata = IERC20Metadata(pool.forwAddress().call(), self.web3)
        amount = parseEther(self.web3, amount, forw_token.decimals().call())
        contract_func = pool.claimForwInterest(nft_id, amount)
        return self.send_transaction(contract_func, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def borrow(self, pool:IAPHPool, nft_id:int, loan_id:int, borrow_amount:int, collateral_sent_amount:int, collateral_token:IERC20Metadata, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0)->Union[TransactionReceipt, int]:
        borrow_token:IERC20Metadata = IERC20Metadata(pool.tokenAddress().call(), self.web3)
        borrow_amount = parseEther(self.web3, borrow_amount, borrow_token.decimals().call())
        collateral_sent_amount = parseEther(self.web3, collateral_sent_amount, collateral_token.decimals().call())
        is_native = self.native.address == collateral_token.address
        contract_func = pool.borrow(loan_id, nft_id, borrow_amount, collateral_sent_amount, collateral_token.address)
        return self.send_transaction(contract_func, value=collateral_sent_amount if is_native else 0, is_estimate=is_estimate, gas=gas, gas_price=gas_price, nonce=nonce)

    def open_position(self, nft_id:int, is_long:bool, collateral_token:IERC20Metadata, underlying_token:IERC20Metadata, entry_price:int, size:int, leverage:int, slip_page:int, is_estimate=False, gas:int=0, gas_price:int=0, nonce:int=0):
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
    


    