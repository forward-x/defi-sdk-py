from decimal import Decimal
from web3 import Web3

def parseEther(web3:Web3,value, decimal:int=18):
    return web3.to_wei(Decimal(value * (10**decimal)), 'wei')