import json
class AddressConst:

    def __init__(self, config_data):
        self.return_str = {}
        for key, value in config_data.items():
            if key == "token":
                token:dict = {}
                for token_key, token_address in key.items():
                    token[token_key] = token_address
                setattr(self, key.lower(), token)
                self.return_str[key.lower()] = token
            elif key == "pool":
                pool:dict = {}
                for pool_key, pool_address in key.items():
                    pool[pool_key] = pool_address
                setattr(self, key.lower(), pool)
                self.return_str[key.lower()] = pool
            else:
                self.return_str[key.lower()] = value
                setattr(self, key.lower(), value)
    
    def __str__(self):

        return json.dumps(self.return_str, indent=3)

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

    def get_helper_core_address(self)->dict:
        return self.helper_core

    def get_helper_pool_address(self)->dict:
        return self.helper_pool

    def get_helper_membership_and_stake_pool_address(self)->dict:
        return self.helper_membership_and_stakepool

    def get_helper_future_trade_address(self)->dict:
        return self.helper_futuretrade

