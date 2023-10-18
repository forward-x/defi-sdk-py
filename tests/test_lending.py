from defi_sdk_py.fwx_provider import FwxWeb3
from store_fixture import fwx_lending_borrowing_client

# def withdraw(self, poolTokenSymbol, nftId, withdrawAmount, gas=220000, gasPrice=25, nonce=0):
# def claimAllInterest(self, poolTokenSymbol, nftId, gas=220000, gasPrice=25, nonce=0):
# def getLendingInfoPlatform(self, poolTokenSymbol):
# def getInterestRate(self, poolTokenSymbol, depositAmount):
# def getFwxInterestRate(self, poolTokenSymbol, depositAmount):


def test_deposit(fwx_lending_borrowing_client):
    client = fwx_lending_borrowing_client
    result = None
    while result is None:
        try:
            result = client.deposit(
                "USDC", client.getNftId(), 10, nonce=client.getAndAddNonce())
        except ValueError:
            pass
    assert result[1]["mintedP"] > 0
    assert result[1]["mintedAtp"] > -1
    assert result[1]["mintedItp"] > 0
    assert result[1]["mintedIfp"] > -1


def test_withdraw(fwx_lending_borrowing_client):
    client = fwx_lending_borrowing_client
    result = None
    while result is None:
        try:
            result = client.deposit(
                "USDC", client.getNftId(), 100, nonce=client.getAndAddNonce())
        except ValueError:
            info = client.getLendingInfo("USDC", client.getNftId())
            if info["lendingBalance"] == 100:
                result = (None, 100)
            pass
    result = None
    while result is None:
        try:
            result = client.withdraw(
                "USDC", client.getNftId(), 10, nonce=client.getAndAddNonce())
        except ValueError:
            pass
    assert result[1]["principle"] > -1
    assert result[1]["tokenInterest"] > -1
    assert result[1]["forwInterest"] > -1
    assert result[1]["pTokenBurn"] > -1
    assert result[1]["atpTokenBurn"] > -1
    assert result[1]["lossBurn"] > -1
    assert result[1]["itpTokenBurn"] > -1
    assert result[1]["ifpTokenBurn"] > -1
    assert result[1]["tokenInterestBonus"] > -1
    assert result[1]["forwInterestBonus"] > -1


def test_claim_all_interest(fwx_lending_borrowing_client):
    client = fwx_lending_borrowing_client
    result = None
    while result is None:
        try:
            result = client.deposit(
                "USDC", client.getNftId(), 100, nonce=client.getAndAddNonce())
        except ValueError:
            info = client.getLendingInfo("USDC", client.getNftId())
            if info["lendingBalance"] == 100:
                result = (None, 100)
            pass
    result = None
    while result is None:
        try:
            result = client.claimAllInterest(
                "USDC", client.getNftId(), nonce=client.getAndAddNonce())
        except ValueError:
            pass
    assert result[1]["principle"] > -1
    assert result[1]["tokenInterest"] > -1
    assert result[1]["forwInterest"] > -1
    assert result[1]["pTokenBurn"] > -1
    assert result[1]["atpTokenBurn"] > -1
    assert result[1]["lossBurn"] > -1
    assert result[1]["itpTokenBurn"] > -1
    assert result[1]["ifpTokenBurn"] > -1
    assert result[1]["tokenInterestBonus"] > -1
    assert result[1]["forwInterestBonus"] > -1
    pass


def test_get_lending_info(fwx_lending_borrowing_client):
    client = fwx_lending_borrowing_client
    result = None
    while result is None:
        try:
            result = client.deposit(
                "USDC", client.getNftId(), 10, nonce=client.getAndAddNonce())
        except ValueError:
            pass

    result = client.getLendingInfo("USDC", client.getNftId())

    assert result["lendingBalance"] > -1
    assert result["interestObtained"] > -1
    assert result["interestFwxObtained"] > -1
    assert result["rank"] > -1
    assert result["rankInfo"]["interestBonusLending"] > -1
    assert result["rankInfo"]["forwardBonusLending"] > -1
    assert result["rankInfo"]["minimumStakeAmount"] > -1
    assert result["rankInfo"]["maxLTVBonus"] > -1
    assert result["rankInfo"]["tradingFee"] > -1
    assert result["rankInfo"]["tradingBonus"] > -1


def test_get_lending_info_platform(fwx_lending_borrowing_client):
    client = fwx_lending_borrowing_client
    result = client.getLendingInfoPlatform("USDC")
    assert result["atpPrice"] > -1
    assert result["itpPrice"] > -1
    assert result["ifpPrice"] > -1
    assert result["totalSupply"] > -1
    assert result["availableSupply"] > -1
    assert result["utilizationRate"] > -1
    assert result["interestRate"] > -1
    assert result["interestFwxRate"] > -1


def test_get_interest_rate(fwx_lending_borrowing_client):
    client = fwx_lending_borrowing_client
    assert client.getInterestRate("USDC", 100) > 0


def test_get_fwx_interest_rate(fwx_lending_borrowing_client):
    client = fwx_lending_borrowing_client
    assert client.getFwxInterestRate("USDC", 100) > -1
