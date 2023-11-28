from defi_sdk_py.fwx_provider import FwxWeb3
from store_fixture import fwx_trading_client


def test_open_position_long(fwx_trading_client):
    client = fwx_trading_client
    result = None
    while result is None:
        try:
            result = client.depositCollateral(
                "USDC", "ETH", client.getNftId(), 100)
        except ValueError:
            if client.getCollateralBalance("USDC", "ETH", client.getNftId()) == 100:
                result = (None, 100)
            pass
    result = None
    while result is None:
        try:
            result = client.openPosition(
                True, "USDC", "ETH", client.getNftId(), 1640, 0.01, 1, 20)
        except ValueError:
            positionInfo = client.getPositionInfo(
                client.getNftId(), "USDC", "ETH")
            if positionInfo[FwxWeb3.ID] != 0:
                result = (None, positionInfo)
    assert result[1][FwxWeb3.CONTRACT_SIZE] > 0


def test_open_position_short(fwx_trading_client):
    client = fwx_trading_client
    result = None
    while result is None:
        try:
            result = client.depositCollateral(
                "USDC", "ETH", client.getNftId(), 100)
        except ValueError:
            if client.getCollateralBalance("USDC", "ETH", client.getNftId()) == 100:
                result = (None, 100)
            pass
    result = None
    while result is None:
        try:
            result = client.openPosition(
                False, "USDC", "ETH", client.getNftId(), 1640, 0.01, 1, 20)
        except ValueError:
            positionInfo = client.getPositionInfo(
                client.getNftId(), "USDC", "ETH")
            if positionInfo[FwxWeb3.ID] != 0:
                result = (None, positionInfo)
    assert result[1][FwxWeb3.CONTRACT_SIZE] > 0


def test_close_position(fwx_trading_client):
    client = fwx_trading_client
    result = None
    while result is None:
        try:
            result = client.depositCollateral(
                "USDC", "ETH", client.getNftId(), 100)
        except ValueError:
            if client.getCollateralBalance("USDC", "ETH", client.getNftId()) == 100:
                result = (None, 100)
            pass
    result = None
    while result is None:
        try:
            result = client.openPosition(
                True, "USDC", "ETH", client.getNftId(), 1640, 0.01, 1, 20)
        except ValueError:
            positionInfo = client.getPositionInfo(
                client.getNftId(), "USDC", "ETH")
            if positionInfo[FwxWeb3.ID] != 0:
                result = (None, positionInfo)
    posId = result[1][FwxWeb3.ID]
    result = None
    while result is None:
        try:
            result = client.closePosition(client.getNftId(), posId, 0.01)
        except ValueError:
            positionInfo = client.getPositionInfo(
                client.getNftId(), "USDC", "ETH")
            if positionInfo[FwxWeb3.ID] == 0:
                result = (None, positionInfo)
    assert result[1][FwxWeb3.CONTRACT_SIZE] == 1


def test_deposit_collateral(fwx_trading_client):
    client = fwx_trading_client
    result = None
    while result is None:
        try:
            result = client.depositCollateral(
                "USDC", "ETH", client.getNftId(), 100)
        except ValueError:
            if client.getCollateralBalance("USDC", "ETH", client.getNftId()) == 100:
                result = (None, 100)
    assert result[1] == 100


def test_withdraw_collateral(fwx_trading_client):
    client = fwx_trading_client
    result = None
    while result is None:
        try:
            result = client.depositCollateral(
                "USDC", "ETH", client.getNftId(), 100)
        except ValueError:
            if client.getCollateralBalance("USDC", "ETH", client.getNftId()) == 100:
                result = (None, 100)
    result = None
    while result is None:
        try:
            result = client.withdrawCollateral(
                "USDC", "ETH", client.getNftId(), 10)
        except ValueError:
            if client.getCollateralBalance("USDC", "ETH", client.getNftId()) == 90:
                result = (None, 90)
    assert result[1] == 90


def test_get_position_info(fwx_trading_client):
    client = fwx_trading_client
    result = None
    while result is None:
        try:
            result = client.depositCollateral(
                "USDC", "ETH", client.getNftId(), 100)
        except ValueError:
            if client.getCollateralBalance("USDC", "ETH", client.getNftId()) == 100:
                result = (None, 100)
            pass
    result = None
    while result is None:
        try:
            result = client.openPosition(
                True, "USDC", "ETH", client.getNftId(), 1640, 0.01, 2, 20)
        except ValueError:
            positionInfo = client.getPositionInfo(
                client.getNftId(), "USDC", "ETH")
            if positionInfo[FwxWeb3.ID] != 0:
                result = (None, positionInfo)
    result = client.getPositionInfo(
        client.getNftId(), "USDC", "ETH")
    assert result[FwxWeb3.ID] != 0
    assert result[FwxWeb3.CONTRACT_SIZE] > 0
    assert result[FwxWeb3.BORROW_AMOUNT] > 0

# getAllActivePosition(self, nftId, pairs)


def test_get_all_active_position(fwx_trading_client):
    client = fwx_trading_client
    result = None
    while result is None:
        try:
            result = client.depositCollateral(
                "USDC", "ETH", client.getNftId(), 100)
        except ValueError:
            if client.getCollateralBalance("USDC", "ETH", client.getNftId()) == 100:
                result = (None, 100)
            pass
    result = None
    while result is None:
        try:
            result = client.openPosition(
                True, "USDC", "ETH", client.getNftId(), 1640, 0.01, 1, 20)
        except ValueError:
            positionInfo = client.getPositionInfo(
                client.getNftId(), "USDC", "ETH")
            if positionInfo[FwxWeb3.ID] != 0:
                result = (None, positionInfo)
    result = client.getAllActivePosition(
        client.getNftId(), [{"collateral": "USDC", "underlying": "ETH"}, {"collateral": "USDC", "underlying": "WAVAX"}])
    assert len(result) > 0


def test_get_position_state_info_long(fwx_trading_client):
    client = fwx_trading_client
    result = None
    while result is None:
        try:
            result = client.depositCollateral(
                "USDC", "ETH", client.getNftId(), 100)
        except ValueError:
            if client.getCollateralBalance("USDC", "ETH", client.getNftId()) == 100:
                result = (None, 100)
            pass
    result = None
    while result is None:
        try:
            result = client.openPosition(
                True, "USDC", "ETH", client.getNftId(), 1640, 0.01, 1, 20)
        except ValueError:
            positionInfo = client.getPositionInfo(
                client.getNftId(), "USDC", "ETH")
            if positionInfo[FwxWeb3.ID] != 0:
                result = (None, positionInfo)
    posId = result[1][FwxWeb3.ID]
    result = client.getPositionStateInfo(client.getNftId(), posId)
    assert result[FwxWeb3.ACTIVE] == True
    assert result[FwxWeb3.ISLONG] == True


def test_get_position_state_info_short(fwx_trading_client):
    client = fwx_trading_client
    result = None
    while result is None:
        try:
            result = client.depositCollateral(
                "USDC", "ETH", client.getNftId(), 100)
        except ValueError:
            if client.getCollateralBalance("USDC", "ETH", client.getNftId()) == 100:
                result = (None, 100)
            pass
    result = None
    while result is None:
        try:
            result = client.openPosition(
                False, "USDC", "ETH", client.getNftId(), 1640, 0.01, 1, 20)
        except ValueError:
            positionInfo = client.getPositionInfo(
                client.getNftId(), "USDC", "ETH")
            if positionInfo[FwxWeb3.ID] != 0:
                result = (None, positionInfo)
    posId = result[1][FwxWeb3.ID]
    result = client.getPositionStateInfo(client.getNftId(), posId)
    assert result[FwxWeb3.ACTIVE] == True
    assert result[FwxWeb3.ISLONG] == False


def test_get_current_margin(fwx_trading_client):
    client = fwx_trading_client
    result = None
    while result is None:
        try:
            result = client.depositCollateral(
                "USDC", "ETH", client.getNftId(), 100)
        except ValueError:
            if client.getCollateralBalance("USDC", "ETH", client.getNftId()) == 100:
                result = (None, 100)
            pass
    result = None
    while result is None:
        try:
            result = client.openPosition(
                True, "USDC", "ETH", client.getNftId(), 1640, 0.01, 1, 20)
        except ValueError:
            positionInfo = client.getPositionInfo(
                client.getNftId(), "USDC", "ETH")
            if positionInfo[FwxWeb3.ID] != 0:
                result = (None, positionInfo)
    result = client.getCurrentMargin(client.getNftId(), "USDC", "ETH")
    assert result > 20


def test_get_available_collateral(fwx_trading_client):
    client = fwx_trading_client
    result = None
    while result is None:
        try:
            result = client.depositCollateral(
                "USDC", "ETH", client.getNftId(), 100)
        except ValueError:
            if client.getCollateralBalance("USDC", "ETH", client.getNftId()) == 100:
                result = (None, 100)
            pass
    result = client.getAvailableCollateral(client.getNftId(), "USDC", "ETH")
    assert result[FwxWeb3.FREE_BALANCE] == 100
    assert result[FwxWeb3.USED_BALANCE] == 0
    assert result[FwxWeb3.TOTAL_BALANCE] == 100
