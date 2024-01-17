Welcome to Your Project's Documentation
=======================================

Example
-------

.. code-block:: python

   from defi_sdk_py import AVAXChainClient

   # Instantiate AVAX Chain Client
   clientAVAX = AVAXChainClient(
       rpc_url="https://avax.example.com/rpc",
       private_key="your_private_key",
       address_const=your_address_const_instance,
       maxFeePerGas=3000000,
       maxPriorityFeePerGas=2000000,
   )

   # approve to some address
   approve_token = clientAVAX.approve(clientAVAX.TOKEN.WAVAX, clientAVAX.stakepool.address, 1000000)

   # mint NFT
   mint = clientAVAX.mint(nft_id)

   # get default membership nft id
   nft_id = clientAVAX.get_default_membership(clientAVAX.address);

   # deposit AVAX into pool AVAX
   deposit = clientAVAX.deposit(clientAVAX.POOLS.AVAX, nft_id, 1000)

   # borrow USDC and collateral is AVAX
   borrow = clientAVAX.borrow(clientAVAX.POOLS.USDC, nft_id, 0, 1000, 10, clientAVAX.TOKEN.WAVAX)

   # open position
   open_position = clientAVAX.open_position(
       nft_id=nft_id,
       is_long=True,
       collateral_token=clientAVAX.TOKEN.USDC,
       underlying_token=clientAVAX.TOKEN.WAVAX,
       entry_price=38,
       size=5,
       leverage=5,
       slip_page=10,
   )

Indices and tables
===================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. toctree::
   :maxdepth: 7
   :caption: Contents:

   defi_sdk_py.rst
   defi_sdk_py.chain_client.rst
   defi_sdk_py.address_const.rst
   defi_sdk_py.core.rst
   defi_sdk_py.pool.rst
   defi_sdk_py.membership.rst
   defi_sdk_py.stake_pool.rst
   defi_sdk_py.utils.rst
   defi_sdk_py.helper_core.rst
   defi_sdk_py.helper_pool.rst
   defi_sdk_py.helper_future_trade.rst
   defi_sdk_py.helper_membership_and_stake_pool.rst
   # ... (include other relevant files)

