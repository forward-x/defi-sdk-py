# defi-sdk-py

# Installation

```bash
pip install git+https://github.com/forward-x/defi-sdk-py
```

# Usage

### Declare client for each chain, example AVAX-FUJI

```python
from defi_sdk_py.avax_fuji_chain import ADDRESS as FUJI_ADDRESS
from defi_sdk_py.avax_fuji_chain import AVAXFUJIChainClient
client = AVAXFUJIChainClient(
    rpc_url=FUJI_RPC_URL,
    private_key=<YOUR_PRIVATE_KEY>,
    address_const=FUJI_ADDRESS,
    maxFeePerGas=3000000,
    maxPriorityFeePerGas=2000000,
)

# other logic / function ...
```
