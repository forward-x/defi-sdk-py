IHELPERFUTURETRADE_ABI=[
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      }
    ],
    "name": "getAllActivePositions",
    "outputs": [
      {
        "components": [
          {
            "components": [
              {
                "internalType": "uint64",
                "name": "id",
                "type": "uint64"
              },
              {
                "internalType": "address",
                "name": "collateralTokenAddress",
                "type": "address"
              },
              {
                "internalType": "uint64",
                "name": "lastSettleTimestamp",
                "type": "uint64"
              },
              {
                "internalType": "address",
                "name": "borrowTokenAddress",
                "type": "address"
              },
              {
                "internalType": "address",
                "name": "swapTokenAddress",
                "type": "address"
              },
              {
                "internalType": "uint256",
                "name": "entryPrice",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "contractSize",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "borrowAmount",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "collateralSwappedAmount",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "interestOwed",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "interestOwePerDay",
                "type": "uint256"
              }
            ],
            "internalType": "struct CoreBase.Position",
            "name": "position",
            "type": "tuple"
          },
          {
            "internalType": "int256",
            "name": "PNL",
            "type": "int256"
          },
          {
            "internalType": "int256",
            "name": "ROE",
            "type": "int256"
          },
          {
            "internalType": "int256",
            "name": "margin",
            "type": "int256"
          },
          {
            "internalType": "uint256",
            "name": "rate",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "liqPrice",
            "type": "uint256"
          }
        ],
        "internalType": "struct HelperBase.PositionData[]",
        "name": "data",
        "type": "tuple[]"
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
        "internalType": "bool",
        "name": "isLong",
        "type": "bool"
      },
      {
        "internalType": "uint256",
        "name": "contractSize",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "expectedRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "slippage",
        "type": "uint256"
      }
    ],
    "name": "getAveragePrice",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "averagePrice",
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
        "internalType": "bool",
        "name": "isLong",
        "type": "bool"
      },
      {
        "internalType": "uint256",
        "name": "contractSize",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "expectedRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "slippage",
        "type": "uint256"
      }
    ],
    "name": "getBalanceAfterOpenPosition",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "balance",
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
      }
    ],
    "name": "getBalanceDetails",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "freeBalance",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "usedBalance",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "totalBalance",
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
        "name": "contractSize",
        "type": "uint256"
      }
    ],
    "name": "getClosingFee",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "swapFee",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "tradingFee",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "totalFee",
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
        "internalType": "bool",
        "name": "isLong",
        "type": "bool"
      },
      {
        "internalType": "uint256",
        "name": "contractSize",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "expectedRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "slippage",
        "type": "uint256"
      }
    ],
    "name": "getEntryPrice",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "entryPrice",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "swapFee",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "swapSize",
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
        "internalType": "bool",
        "name": "isLong",
        "type": "bool"
      },
      {
        "internalType": "uint256",
        "name": "contractSize",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "expectedRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "slippage",
        "type": "uint256"
      }
    ],
    "name": "getLiqPriceAfterOpenPosition",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "liquidationPrice",
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
      }
    ],
    "name": "getLiquidationPrice",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "liquidationPrice",
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
        "internalType": "bool",
        "name": "isAdd",
        "type": "bool"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "getMarginAfterAdjustCollateral",
    "outputs": [
      {
        "internalType": "int256",
        "name": "margin",
        "type": "int256"
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
      }
    ],
    "name": "getMarginAfterClosePosition",
    "outputs": [
      {
        "internalType": "int256",
        "name": "margin",
        "type": "int256"
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
        "internalType": "bool",
        "name": "isLong",
        "type": "bool"
      },
      {
        "internalType": "uint256",
        "name": "contractSize",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "expectedRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "slippage",
        "type": "uint256"
      }
    ],
    "name": "getMarginAfterOpenPosition",
    "outputs": [
      {
        "internalType": "int256",
        "name": "margin",
        "type": "int256"
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
        "internalType": "bool",
        "name": "isLong",
        "type": "bool"
      },
      {
        "internalType": "uint256",
        "name": "leverage",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "expectedRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "slippage",
        "type": "uint256"
      }
    ],
    "name": "getMaxContractSize",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "maxContractSize",
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
      }
    ],
    "name": "getMaxWithdrawal",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "maxWithdrawal",
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
        "internalType": "bool",
        "name": "isLong",
        "type": "bool"
      },
      {
        "internalType": "uint256",
        "name": "contractSize",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "expectedRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "slippage",
        "type": "uint256"
      }
    ],
    "name": "getOpeningFee",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "swapFee",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "tradingFee",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "totalFee",
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
      }
    ],
    "name": "getPNLAfterClosePosition",
    "outputs": [
      {
        "internalType": "int256",
        "name": "PNL",
        "type": "int256"
      },
      {
        "internalType": "int256",
        "name": "ROE",
        "type": "int256"
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
      }
    ],
    "name": "getPositionMargin",
    "outputs": [
      {
        "internalType": "int256",
        "name": "margin",
        "type": "int256"
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
        "internalType": "uint256",
        "name": "cursor",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "resultsPerPage",
        "type": "uint256"
      }
    ],
    "name": "getPositionStates",
    "outputs": [
      {
        "components": [
          {
            "internalType": "bool",
            "name": "active",
            "type": "bool"
          },
          {
            "internalType": "bool",
            "name": "isLong",
            "type": "bool"
          },
          {
            "internalType": "int128",
            "name": "PNL",
            "type": "int128"
          },
          {
            "internalType": "uint64",
            "name": "startTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "bytes32",
            "name": "pairByte",
            "type": "bytes32"
          },
          {
            "internalType": "uint128",
            "name": "averageEntryPrice",
            "type": "uint128"
          },
          {
            "internalType": "uint128",
            "name": "interestPaid",
            "type": "uint128"
          },
          {
            "internalType": "uint128",
            "name": "totalTradingFee",
            "type": "uint128"
          },
          {
            "internalType": "uint128",
            "name": "totalSwapFee",
            "type": "uint128"
          }
        ],
        "internalType": "struct CoreBase.PositionState[]",
        "name": "positionStates",
        "type": "tuple[]"
      },
      {
        "internalType": "uint256",
        "name": "newCursor",
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
        "internalType": "bool",
        "name": "isLong",
        "type": "bool"
      },
      {
        "internalType": "uint256",
        "name": "contractSize",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "leverage",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "expectedRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "slippage",
        "type": "uint256"
      }
    ],
    "name": "getRequiredCollateral",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "collateral",
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
      }
    ],
    "name": "getUnrealizedPNL",
    "outputs": [
      {
        "internalType": "int256",
        "name": "PNL",
        "type": "int256"
      },
      {
        "internalType": "int256",
        "name": "ROE",
        "type": "int256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]