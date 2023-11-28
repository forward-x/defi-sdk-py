import defi_sdk_py
from store_fixture import fwx_lending_borrowing_client
from brownie.network.state import Chain


def test_borrow(fwx_lending_borrowing_client):
    client = fwx_lending_borrowing_client
    result = None

    while result is None:
        try:
            result = client.approveToken(
                defi_sdk_py.ADDRESSES["AVAX"]["CORE"], "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.borrow("ETH", client.getNftId(
            ), 0, 0.01, 100, "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    assert result[1]["borrowTokenAddress"] == defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"]["ETH"]
    assert result[1]["collateralTokenAddress"] == defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"]["USDC"]


def test_repay(fwx_lending_borrowing_client):
    client = fwx_lending_borrowing_client

    result = None
    while result is None:
        try:
            result = client.approveToken(
                defi_sdk_py.ADDRESSES["AVAX"]["CORE"], "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.approveToken(
                defi_sdk_py.ADDRESSES["AVAX"]["CORE"], "ETH", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.borrow("ETH", client.getNftId(
            ), 0, 0.01, 100, "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.repay(client.getNftId(
            ), 2, 0.001, nonce=client.getAndAddNonce())
        except ValueError:
            pass

    assert result[1]["borrowPaid"] > 0.0005
    assert result[1]["interestPaid"] > 0


def test_repay_interest(fwx_lending_borrowing_client):
    client = fwx_lending_borrowing_client
    result = None

    while result is None:
        try:
            result = client.approveToken(
                defi_sdk_py.ADDRESSES["AVAX"]["CORE"], "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.approveToken(
                defi_sdk_py.ADDRESSES["AVAX"]["CORE"], "ETH", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.borrow("ETH", client.getNftId(
            ), 0, 0.01, 100, "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    chain = Chain()
    chain.sleep(86400)
    result = None
    while result is None:
        try:
            result = client.repayInterest(client.getNftId(
            ), 2, 10, nonce=client.getAndAddNonce())
        except ValueError:
            pass

    assert result[1]["interestPaid"] > 0


def test_add_collateral(fwx_lending_borrowing_client):
    client = fwx_lending_borrowing_client

    result = None
    while result is None:
        try:
            result = client.approveToken(
                defi_sdk_py.ADDRESSES["AVAX"]["CORE"], "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.approveToken(
                defi_sdk_py.ADDRESSES["AVAX"]["CORE"], "ETH", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.borrow("ETH", client.getNftId(
            ), 0, 0.01, 100, "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.addCollateral(client.getNftId(
            ), 2, 10, nonce=client.getAndAddNonce())
        except ValueError:
            pass

    assert result[1]["collateralAmount"] > 100


def test_remove_collateral(fwx_lending_borrowing_client):
    client = fwx_lending_borrowing_client

    result = None
    while result is None:
        try:
            result = client.approveToken(
                defi_sdk_py.ADDRESSES["AVAX"]["CORE"], "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.approveToken(
                defi_sdk_py.ADDRESSES["AVAX"]["CORE"], "ETH", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.borrow("ETH", client.getNftId(
            ), 0, 0.01, 100, "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.removeCollateral(client.getNftId(
            ), 2, 10, nonce=client.getAndAddNonce())
        except ValueError:
            pass

    assert result[1]["collateralAmount"] < 100


def test_rollover(fwx_lending_borrowing_client):
    client = fwx_lending_borrowing_client
    result = None

    while result is None:
        try:
            result = client.approveToken(
                defi_sdk_py.ADDRESSES["AVAX"]["CORE"], "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.approveToken(
                defi_sdk_py.ADDRESSES["AVAX"]["CORE"], "ETH", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.borrow("ETH", client.getNftId(
            ), 0, 0.01, 100, "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    chain = Chain()
    chain.sleep(86400 * 30)
    result = None
    while result is None:
        try:
            result = client.rollover(client.getNftId(
            ), 2, nonce=client.getAndAddNonce())
        except ValueError:
            pass

    assert result[1]["delayInterest"] > 0
    assert result[1]["bountyReward"] > 0


def test_get_loan_info(fwx_lending_borrowing_client):
    client = fwx_lending_borrowing_client

    result = None
    while result is None:
        try:
            result = client.approveToken(
                defi_sdk_py.ADDRESSES["AVAX"]["CORE"], "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.approveToken(
                defi_sdk_py.ADDRESSES["AVAX"]["CORE"], "ETH", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = None
    while result is None:
        try:
            result = client.borrow("ETH", client.getNftId(
            ), 0, 0.01, 100, "USDC", nonce=client.getAndAddNonce())
        except ValueError:
            pass
    result = client.getLoanInfo(client.getNftId(), 2)
    assert result["active"]
    assert result["startTimestamp"] > 0
    assert result["borrowTokenAddress"] == defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"]["ETH"]
    assert result["collateralTokenAddress"] == defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"]["USDC"]
    assert result["lastSettleTimestamp"] > 0
    assert result["rolloverTimestamp"] > 0
    assert result["borrowAmount"] > 0
    assert result["collateralAmount"] > 0
    assert result["owedPerDay"] > 0
    assert result["minInterest"] > 0
    assert result["interestOwed"] > -1
    assert result["interestPaid"] > -1


def test_borrowing_interest_rate(fwx_lending_borrowing_client):
    client = fwx_lending_borrowing_client
    result = client.getBorrowingInterestRate("WAVAX", 100)

    assert result["interestRate"] > 0
    assert result["interestOwedPerDay"] > 0
