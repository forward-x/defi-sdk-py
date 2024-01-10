class AddressConst:

    def __init__(self, config_data):
        for key, value in config_data.items():
            if key == "token":
                token:dict = {}
                for token_key, token_address in key.items():
                    token[token_key] = token_address
                setattr(self, key.lower(), token)
            elif key == "pool":
                pool:dict = {}
                for pool_key, pool_address in key.items():
                    pool[pool_key] = pool_address
                setattr(self, key.lower(), pool)
            else:
                setattr(self, key.lower(), value)

    def get_library_address(self)->str:
        return self.library

    def get_membership_address(self)->str:
        return self.membership

    def get_stakepool_address(self)->str:
        return self.stakepool

    def get_core_address(self)->str:
        return self.core

    def get_tokens_address(self)->dict:
        return self.token

    def get_pools_address(self)->dict:
        return self.pool
