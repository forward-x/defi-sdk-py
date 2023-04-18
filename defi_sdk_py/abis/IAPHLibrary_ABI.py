IAPHLIBRARY_ABI=[
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "a",
        "type": "uint256"
      },
      {
        "internalType": "int256",
        "name": "b",
        "type": "int256"
      }
    ],
    "name": "addIntToUint",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "wallet",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "swappedCollateral",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "interestOwed",
        "type": "uint256"
      },
      {
        "internalType": "int256",
        "name": "PNL",
        "type": "int256"
      },
      {
        "internalType": "uint256",
        "name": "positionSize",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "feeAmount",
        "type": "uint256"
      }
    ],
    "name": "calculateMargin",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "result",
        "type": "uint256"
      }
    ],
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "firstValue",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "secondValue",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "multiplier",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "divisor",
        "type": "uint256"
      }
    ],
    "name": "calculatePNL",
    "outputs": [
      {
        "internalType": "int256",
        "name": "",
        "type": "int256"
      }
    ],
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "collateralTokenAddress",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "underlyingTokenAddress",
        "type": "address"
      }
    ],
    "name": "hashPair",
    "outputs": [
      {
        "internalType": "bytes32",
        "name": "pairByte",
        "type": "bytes32"
      }
    ],
    "stateMutability": "pure",
    "type": "function"
  }
]