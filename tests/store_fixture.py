import pytest

from brownie import accounts, web3

from defi_sdk_py import fwx_provider
import defi_sdk_py
import random


class SeedCounter():
    seed = 39276531

    @staticmethod
    def getAndAddSeed():
        currentSeed = SeedCounter.seed
        SeedCounter.seed += 1
        return currentSeed


def __fwx_client():
    # Replace '1' with your seed value
    random.seed(SeedCounter.getAndAddSeed())
    random_int = random.getrandbits(256)
    PRIVATE_KEY = hex(random_int)
    accounts.add(PRIVATE_KEY)
    accounts[0].transfer(accounts[len(accounts)-1], "1000 ether", gas_price=0)
    client = fwx_provider.getClient(web3.provider.endpoint_uri)
    client.setSigner(PRIVATE_KEY)
    return client


class TestClient(fwx_provider.FwxWeb3):
    def __init__(self, client):
        self.w3 = client.getW3()
        self.signer = client.getSigner()
        self.nonce = 0

    def getAndAddNonce(self, increaseVaule=1):
        nonce = self.nonce
        self.nonce += increaseVaule
        return nonce

    def setNftId(self, nftId):
        self.nftId = nftId

    def getNftId(self):
        return self.nftId


@pytest.fixture
def fwx_client():
    return __fwx_client()


@pytest.fixture
def fwx_lending_borrowing_client():
    client = TestClient(__fwx_client())

    # mint nft
    nftId = client.mint(0, nonce=client.getAndAddNonce())[1]
    client.setNftId(nftId)

    # borrow USDC
    result = None
    while result is None:
        try:
            result = client.borrow(
                "USDC", nftId, 0, 1000, 200, "WAVAX", nonce=client.getAndAddNonce())
        except ValueError:
            pass

    # approve pool
    result = None
    while result is None:
        try:
            result = client.approveToken(
                defi_sdk_py.ADDRESSES["AVAX"]["POOL"]["USDC"], "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    return client


@pytest.fixture
def fwx_trading_client():
    client = TestClient(__fwx_client())

    # mint nft
    nftId = client.mint(0, nonce=client.getAndAddNonce())[1]
    client.setNftId(nftId)

    result = None
    # borrow USDC
    while result is None:
        try:
            result = client.borrow(
                "USDC", nftId, 0, 1000, 200, "WAVAX", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.approveToken(
                defi_sdk_py.ADDRESSES["AVAX"]["CORE"], "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    return client
