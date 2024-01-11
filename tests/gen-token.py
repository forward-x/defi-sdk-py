json_data = {
    "TOKEN": {
        
    }
}

script_content = f"""\
from ..abi.IERC20Metadata import IERC20Metadata
from web3 import Web3

class Tokens:
    def __init__(self, web3: Web3, address_dict: dict):
        # Generate dynamic attributes based on the keys in the address_dict
"""

for token_name, token_address in json_data["TOKEN"].items():
    script_content += f"        self.{token_name}:IERC20Metadata = IERC20Metadata('{token_address}', web3)\n"

with open("tokens.py", "w") as file:
    file.write(script_content)
print("tokens.py script has been generated.")