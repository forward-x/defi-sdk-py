IHELPERFUTURETRADEMARGIN_ABI=[
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "entryPrice",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "leverage",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "contractSize",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "slipPage",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "collateralTokenAddress",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "swapTokenAddress",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "borrowTokenAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "maintenanceMargin",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "routerIndex",
        "type": "uint256"
      }
    ],
    "name": "getDetailAfterAdjustPosition",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "margin",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "liqPrice",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "wallet",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "collateralTokenAddress",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "underlyingTokenAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "newAmount",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "isAdd",
        "type": "bool"
      },
      {
        "internalType": "uint256",
        "name": "routerIndex",
        "type": "uint256"
      }
    ],
    "name": "getMarginAfterAdjustCollateral",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "margin",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      },
      {
        "internalType": "bytes32",
        "name": "pairByte",
        "type": "bytes32"
      },
      {
        "internalType": "uint256",
        "name": "closingSize",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "routerIndex",
        "type": "uint256"
      }
    ],
    "name": "getMarginAfterClosePosition",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "margin",
        "type": "uint256"
      },
      {
        "internalType": "int256",
        "name": "realPNL",
        "type": "int256"
      },
      {
        "internalType": "int256",
        "name": "percentPNL",
        "type": "int256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]