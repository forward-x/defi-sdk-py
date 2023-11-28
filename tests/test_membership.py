import defi_sdk_py
from store_fixture import fwx_client


def test_mint_nft(fwx_client):
    membership = fwx_client.getMembership()
    supply = membership.functions.totalSupply().call()
    result = fwx_client.mint(0)
    assert (supply + 1 == result[1])


def test_get_rank(fwx_client):
    tokenId = fwx_client.mint(0)[1]
    rank = fwx_client.getRank(tokenId)
    assert rank == 0


def test_get_rank_with_stak_pool(fwx_client):
    tokenId = fwx_client.mint(0)[1]
    rank = fwx_client.getRank(
        tokenId, defi_sdk_py.ADDRESSES["AVAX"]["STAKEPOOL"])
    assert rank == 0


def test_owner_of(fwx_client):
    tokenId = fwx_client.mint(0)[1]
    owner_of = fwx_client.ownerOf(tokenId)
    assert owner_of == fwx_client.getSigner().address


def test_usable_token(fwx_client):
    tokenId = fwx_client.mint(0)[1]
    result = fwx_client.usableToken(fwx_client.getSigner().address, tokenId)
    assert result == tokenId
