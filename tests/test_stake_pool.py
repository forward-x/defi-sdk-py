from store_fixture import fwx_client


def test_get_next_settle_timestamp(fwx_client):
    assert fwx_client.getNextSettleTimestamp() == 1697068800


def test_get_nft_list(fwx_client):
    nftId = fwx_client.mint(0)[1]
    result = fwx_client.getNftList(fwx_client.getSigner().address)
    assert nftId == result[0]


def test_get_rank_infos(fwx_client):
    result = fwx_client.getRankInfos()
    assert len(result["interestBonusLending"]) == 6
    assert len(result["forwardBonusLending"]) == 6
    assert len(result["minimumStakeAmount"]) == 6
    assert len(result["maxLTVBonus"]) == 6
    assert len(result["tradingFee"]) == 6


def test_get_stake_info(fwx_client):
    nftId = fwx_client.mint(0)[1]
    result = fwx_client.getStakeInfo(nftId)
    assert result["stakeBalance"] == 0
    assert result["claimableAmount"] == 0
    assert result["startTimestamp"] == 0
    assert result["endTimestamp"] == 0
    assert result["lastSettleTimestamp"] == 0
