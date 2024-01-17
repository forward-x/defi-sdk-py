# from .chain_client import ChainClient
from .fwx_chain import FWXChainClient
from .fwx_chain import ADDRESS as FWX_ADDRESS
from .avax_fuji_chain import AVAXFUJIChainClient
from .avax_fuji_chain import ADDRESS as FUJI_ADDRESS

"""
Example
```
clientAVAX = AVAXChainClient(
    rpc_url=AVAX_RPC_URL,
    private_key=PK,
    address_const=AVAX_ADDRESS,
    maxFeePerGas=3000000,
    maxPriorityFeePerGas=2000000,
)

# approve to some address
approve_token = clientAVAX.approve(clientAVAX.TOKEN.AVAX, clientAVAX.stakepool.address, 1000000)

# mint NFT
# mint = clientAVAX.mint(nft_id)

# 
# deposit = clientAVAX.deposit(clientAVAX.POOLS.AVAX, nft_id, 1000)
```
"""