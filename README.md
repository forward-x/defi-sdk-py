# defi-sdk-py

# Installation

```bash
pip install git+https://github.com/forward-x/defi-sdk-py
```

# Usage

## Deposit Collateral

```python
import web3
import defi_sdk_py

client = fwx_provider.getClient(web3.provider.endpoint_uri)
client.setSigner(PRIVATE_KEY)

client.approveToken(defi_sdk_py.ADDRESSES["AVAX"]["CORE"], "USDC", nonce=client.getAndAddNonce())

client.depositCollateral("USDC", "ETH", client.getNftId(), 100)
```

## Withdraw Collateral

```python
import web3
import defi_sdk_py

client = fwx_provider.getClient(web3.provider.endpoint_uri)
client.setSigner(PRIVATE_KEY)

client.withdrawCollateral("USDC", "ETH", client.getNftId(), 10)
```

# Development

## Prerequire

- poetry
- ganache-cli

```bash
npm i -g ganache-cli
```

- set node env

## Install

```bash
poetry update
```

# Test

```bash
poetry run brownie test
```

If you have error with install `yaml 5.4.1`, [This solution](https://github.com/eth-brownie/brownie/issues/1701#issuecomment-1667707955) might help.
