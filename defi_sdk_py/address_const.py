class AddressConst:
    def __init__(self, json_data):
        self.token_addresses = json_data.get("TOKEN", {})
        self.library = json_data.get("LIBRARY", "")
        self.membership = json_data.get("MEMBERSHIP", "")
        self.stakepool = json_data.get("STAKEPOOL", "")
        self.core = json_data.get("CORE", "")
        self.pool_wbnb = json_data.get("POOL_WBNB", {}).get("PROXY", "")
        self.pool_eth = json_data.get("POOL_ETH", {}).get("PROXY", "")
        self.pool_btc = json_data.get("POOL_BTC", {}).get("PROXY", "")
        self.pool_usdt = json_data.get("POOL_USDT", {}).get("PROXY", "")
        self.pool_busd = json_data.get("POOL_BUSD", {}).get("PROXY", "")

    def get_token_address(self, symbol):
        return self.token_addresses.get(symbol, "")

    def get_library_address(self):
        return self.library

    def get_membership_address(self):
        return self.membership

    def get_stakepool_address(self):
        return self.stakepool

    def get_core_address(self):
        return self.core

    def get_pool_wbnb_proxy_address(self):
        return self.pool_wbnb

    def get_pool_eth_proxy_address(self):
        return self.pool_eth

    def get_pool_btc_proxy_address(self):
        return self.pool_btc

    def get_pool_usdt_proxy_address(self):
        return self.pool_usdt

    def get_pool_busd_proxy_address(self):
        return self.pool_busd
