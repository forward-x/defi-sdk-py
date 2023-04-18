# defi-sdk-py

# Usage

## Deposit Collateral

```python
import web3
import defi_sdk_py

provider = web3.Web3.HTTPProvider(HOST)
w3 = web3.Web3(provider)
signer = web3.Account.privateKeyToAccount(PRIVATE_KEY)
IAPHCore = w3.eth.contract(address=CORE_ADDRESS, abi=defi_sdk_py.IAPHCORE_ABI)
IMembership = w3.eth.contract(address=MEMBERSHIP_ADDRESS, abi=defi_sdk_py.IMEMBERSHIP_ABI)
nftId = IMembership.functions.getDefaultMembership(signer.address).call()
amount =  10000 * 10**18
# create tx
tx = IAPHCore.functions.depositCollateral(nftId, TOKEN_ADDRESS["USDT"], TOKEN_ADDRESS["ETH"], amount).buildTransaction( 
    {
        'from': signer.address,
        'nonce': w3.eth.get_transaction_count(signer.address),
        'gas': 150000,
        'gasPrice': w3.toWei(5, 'gwei'),
    }
)

# Sign tx
signed_tx = w3.eth.account.sign_transaction(tx, signer.key)

# Send tx
w3.eth.send_raw_transaction(signed_tx.rawTransaction)
```

## Withdraw Collateral

```python
import web3
import defi_sdk_py

provider = web3.Web3.HTTPProvider(HOST)
w3 = web3.Web3(provider)
signer = web3.Account.privateKeyToAccount(PRIVATE_KEY)
print(signer.address)
IAPHCore = w3.eth.contract(address=CORE_ADDRESS, abi=defi_sdk_py.IAPHCORE_ABI)
IMembership = w3.eth.contract(address=MEMBERSHIP_ADDRESS, abi=defi_sdk_py.IMEMBERSHIP_ABI)
nftId = IMembership.functions.getDefaultMembership(signer.address).call()
amount =  10000 * 10**18
# create tx
tx = IAPHCore.functions.withdrawCollateral(nftId, TOKEN_ADDRESS["USDT"], TOKEN_ADDRESS["ETH"], amount).buildTransaction( 
    {
        'from': signer.address,
        'nonce': w3.eth.get_transaction_count(signer.address),
        'gas': 150000,
        'gasPrice': w3.toWei(5, 'gwei'),
    }
)

# Sign tx
signed_tx = w3.eth.account.sign_transaction(tx, signer.key)

# Send tx
w3.eth.send_raw_transaction(signed_tx.rawTransaction)
```
