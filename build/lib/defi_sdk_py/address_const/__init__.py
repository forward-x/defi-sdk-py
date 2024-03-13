import json

class AddressConst:
    """
    This class initializes address constants from a provided configuration dictionary.
    It allows retrieval of various blockchain-related addresses.

    Attributes:
        return_str (dict): A dictionary representation of all addresses.

    Args:
        config_data (dict): A dictionary containing configuration data with keys like
                            'token', 'pool', and other blockchain-related addresses.
    """

    def __init__(self, config_data):
        """Constructor method
        """
        self.return_str = {}
        for key, value in config_data.items():
            if key == "token":
                token = {}
                for token_key, token_address in value.items():
                    token[token_key] = token_address
                setattr(self, key.lower(), token)
                self.return_str[key.lower()] = token
            elif key == "pool":
                pool = {}
                for pool_key, pool_address in value.items():
                    pool[pool_key] = pool_address
                setattr(self, key.lower(), pool)
                self.return_str[key.lower()] = pool
            else:
                setattr(self, key.lower(), value)
                self.return_str[key.lower()] = value

    def __str__(self):
        """
        Returns a JSON string representation of the address constants.

        Returns:
            str: A JSON formatted string of address constants.
        """
        return json.dumps(self.return_str, indent=3)

    def get_library_address(self):
        """
        Retrieves the library address.

        Returns:
            str: The library address.
        """
        return self.library

    def get_membership_address(self):
        """
        Retrieves the membership address.

        Returns:
            str: The membership address.
        """
        return self.membership

    def get_stakepool_address(self):
        """
        Retrieves the stake pool address.

        Returns:
            str: The stake pool address.
        """
        return self.stakepool

    def get_core_address(self):
        """
        Retrieves the core address.

        Returns:
            str: The core address.
        """
        return self.core

    def get_tokens_address(self):
        """
        Retrieves all token addresses.

        Returns:
            dict: A dictionary of token addresses.
        """
        return self.token

    def get_pools_address(self):
        """
        Retrieves all pool addresses.

        Returns:
            dict: A dictionary of pool addresses.
        """
        return self.pool

    def get_helper_core_address(self):
        """
        Retrieves the helper core address.

        Returns:
            str: The helper core address.
        """
        return self.helper_core

    def get_helper_pool_address(self):
        """
        Retrieves the helper pool address.

        Returns:
            str: The helper pool address.
        """
        return self.helper_pool

    def get_helper_membership_and_stake_pool_address(self):
        """
        Retrieves the helper membership and stake pool address.

        Returns:
            str: The helper membership and stake pool address.
        """
        return self.helper_membership_and_stakepool

    def get_helper_future_trade_address(self):
        """
        Retrieves the helper future trade address.

        Returns:
            str: The helper future trade address.
        """
        return self.helper_futuretrade