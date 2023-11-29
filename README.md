# defi-sdk-py

# Installation

```bash
pip install git+https://github.com/forward-x/defi-sdk-py
```

# Usage

## Mint NFT ID

```python
import web3
from defi_sdk_py import *

client = fwx_provider.getClient(NODE_URL)
client.setSigner(PRIVATE_KEY)

membership = client.getMembership()
supply = membership.functions.totalSupply().call()
nft_id = client.mint(0)[1]
```

## Mint and Deposit Collateral

```python
import web3
from defi_sdk_py import *

client = fwx_provider.getClient(NODE_URL)
client.setSigner(PRIVATE_KEY)

membership = client.getMembership()
supply = membership.functions.totalSupply().call()
nft_id = client.mint(0)[1]

client.approveToken(ADDRESSES["AVAX"]["CORE"], "USDC")

client.depositCollateral("USDC", "ETH", nft_id, 100)
```

## Mint, Deposit and Withdraw Collateral

```python
import web3
from defi_sdk_py import *

client = fwx_provider.getClient(NODE_URL)
client.setSigner(PRIVATE_KEY)

membership = client.getMembership()
supply = membership.functions.totalSupply().call()
nft_id = client.mint(0)[1]

client.approveToken(ADDRESSES["AVAX"]["CORE"], "USDC")

client.depositCollateral("USDC", "ETH", nft_id, 100)

client.withdrawCollateral("USDC", "ETH", nft_id, 10)
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
