from store_fixture import fwx_client


def test_approve(fwx_client):
    client = fwx_client
    amount = 10
    client.approve("USDC", "CORE", amount)
    allowance = client.getProtocolAllowance("USDC", "CORE", amount)
    assert allowance == amount
    client.approve("USDC", "USDC", amount)
    allowance = client.getProtocolAllowance("USDC", "USDC", amount)
    assert allowance == amount
