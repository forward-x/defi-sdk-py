from store_fixture import fwx_client


def test_get_next_settle_timestamp(fwx_client):
    assert fwx_client.getNextSettleTimestamp() > 26674016


def test_get_nft_list(fwx_client):
    nftId = fwx_client.mint(0)[1]
    result = fwx_client.getNftList(fwx_client.getSigner().address)
    assert nftId == result[0]


def test_get_rank_infos(fwx_client):
    result = fwx_client.getRankInfos()
    assert len(result) == 5
    for i in range(len(result)):
        assert result[i]["interestBonusLending"] > -1
        assert result[i]["forwardBonusLending"] > -1
        assert result[i]["minimumStakeAmount"] > -1
        assert result[i]["maxLTVBonus"] > -1
        assert result[i]["tradingFee"] > -1


def test_get_stake_info(fwx_client):
    nftId = fwx_client.mint(0)[1]
    result = fwx_client.getStakeInfo(nftId)
    assert result["stakeBalance"] == 0
    assert result["claimableAmount"] == 0
    assert result["startTimestamp"] == 0
    assert result["endTimestamp"] == 0
    assert result["lastSettleTimestamp"] == 0
