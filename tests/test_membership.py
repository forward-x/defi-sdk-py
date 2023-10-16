from store_fixture import fwx_client


def test_mint_nft(fwx_client):
    membership = fwx_client.getMembership()
    supply = membership.functions.totalSupply().call()
    result = fwx_client.mint(0)
    assert (supply + 1 == result[1])
