IAPHCORE_ABI=[
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "lossAmount",
        "type": "uint256"
      }
    ],
    "name": "addLossInUSD",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "loanId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "collateralAdjustAmount",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "isAdd",
        "type": "bool"
      }
    ],
    "name": "adjustCollateral",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "interestPaid",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "borrowTokenAddress",
            "type": "address"
          },
          {
            "internalType": "uint64",
            "name": "rolloverTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint64",
            "name": "lastSettleTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "address",
            "name": "collateralTokenAddress",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "borrowAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "collateralAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "owedPerDay",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "minInterest",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "interestOwed",
            "type": "uint256"
          }
        ],
        "internalType": "struct CoreBase.Loan",
        "name": "loan",
        "type": "tuple"
      }
    ],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "advancedInterestDuration",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "assetToPool",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "auctionSpread",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
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
        "name": "loanId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "borrowAmount",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "borrowTokenAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "collateralSentAmount",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "collateralTokenAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "newOwedPerDay",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "interestRate",
        "type": "uint256"
      }
    ],
    "name": "borrow",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "interestPaid",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "borrowTokenAddress",
            "type": "address"
          },
          {
            "internalType": "uint64",
            "name": "rolloverTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint64",
            "name": "lastSettleTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "address",
            "name": "collateralTokenAddress",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "borrowAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "collateralAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "owedPerDay",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "minInterest",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "interestOwed",
            "type": "uint256"
          }
        ],
        "internalType": "struct CoreBase.Loan",
        "name": "loan",
        "type": "tuple"
      }
    ],
    "stateMutability": "payable",
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
        "name": "newAmount",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "tokenAddress",
        "type": "address"
      }
    ],
    "name": "checkStakingAmountSufficient",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
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
        "internalType": "uint256",
        "name": "posId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_closingSize",
        "type": "uint256"
      }
    ],
    "name": "closePosition",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "coreBorrowingAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "coreFutureClosingAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "coreFutureOpeningAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "coreSettingAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "coreSwappingAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "currentLoanIndex",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
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
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "currentPositionIndex",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
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
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "depositCollateral",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "feeSpread",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "feeVaultAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "forwAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "forwLendingDistributionPerBlock",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "forwLendingVaultAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "forwStakingMultiplier",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "forwTradingVaultAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bool",
        "name": "isExactOutput",
        "type": "bool"
      },
      {
        "internalType": "bool",
        "name": "extractSwapFee",
        "type": "bool"
      },
      {
        "internalType": "uint256",
        "name": "routerIndex",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "amountInput",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "src",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "dst",
        "type": "address"
      }
    ],
    "name": "getAmounts",
    "outputs": [
      {
        "internalType": "uint256[]",
        "name": "amounts",
        "type": "uint256[]"
      },
      {
        "internalType": "uint256",
        "name": "swapFee",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "router",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bool",
        "name": "isExactOutput",
        "type": "bool"
      },
      {
        "internalType": "bytes32",
        "name": "pairByte",
        "type": "bytes32"
      },
      {
        "internalType": "uint256",
        "name": "amountInput",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "src",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "dst",
        "type": "address"
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
    "name": "getAmountsWithRouterSelection",
    "outputs": [
      {
        "internalType": "uint256[]",
        "name": "amounts",
        "type": "uint256[]"
      },
      {
        "internalType": "uint256",
        "name": "swapFee",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "router",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "loanId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      }
    ],
    "name": "getLoanCurrentLTV",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getPoolList",
    "outputs": [
      {
        "internalType": "address[]",
        "name": "",
        "type": "address[]"
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
        "name": "isLiquidate",
        "type": "bool"
      }
    ],
    "name": "getPositionMargin",
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
    "inputs": [],
    "name": "getRouters",
    "outputs": [
      {
        "internalType": "address[5]",
        "name": "",
        "type": "address[5]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "poolAddress",
        "type": "address"
      }
    ],
    "name": "isPool",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "lastSettleForw",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
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
        "name": "loanId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      }
    ],
    "name": "liquidate",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "repayBorrow",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "repayInterest",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "bountyReward",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "leftOverCollateral",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
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
    "name": "liquidatePosition",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "liquidationFee",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "loanConfigs",
    "outputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "borrowTokenAddress",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "collateralTokenAddress",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "safeLTV",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "maxLTV",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "liquidationLTV",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "bountyFeeRate",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "penaltyFeeRate",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "maxOraclePriceDiffPercent",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "maxLiquidationOraclePriceDiffPercent",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "minimumCollateralInUSD",
            "type": "uint256"
          }
        ],
        "internalType": "struct CoreBase.LoanConfig",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "loanDuration",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
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
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "loanExts",
    "outputs": [
      {
        "components": [
          {
            "internalType": "bool",
            "name": "active",
            "type": "bool"
          },
          {
            "internalType": "uint64",
            "name": "startTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint256",
            "name": "initialBorrowTokenPrice",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "initialCollateralTokenPrice",
            "type": "uint256"
          }
        ],
        "internalType": "struct CoreBase.LoanExt",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "loans",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "interestPaid",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "borrowTokenAddress",
            "type": "address"
          },
          {
            "internalType": "uint64",
            "name": "rolloverTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint64",
            "name": "lastSettleTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "address",
            "name": "collateralTokenAddress",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "borrowAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "collateralAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "owedPerDay",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "minInterest",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "interestOwed",
            "type": "uint256"
          }
        ],
        "internalType": "struct CoreBase.Loan",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "maximumLeverage",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "membershipAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "nextForwLendingDistributionPerBlock",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "amount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "targetBlock",
            "type": "uint256"
          }
        ],
        "internalType": "struct CoreBase.NextForwLendingDistributionPerBlock",
        "name": "",
        "type": "tuple"
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
      }
    ],
    "name": "nftsLossInUSD",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
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
            "internalType": "uint256",
            "name": "borrowAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "interestOwePerDay",
            "type": "uint256"
          },
          {
            "internalType": "bool",
            "name": "newLong",
            "type": "bool"
          }
        ],
        "internalType": "struct APHLibrary.OpenPositionParams",
        "name": "params",
        "type": "tuple"
      },
      {
        "components": [
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
          }
        ],
        "internalType": "struct APHLibrary.TokenAddressParams",
        "name": "addressParams",
        "type": "tuple"
      }
    ],
    "name": "openPosition",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      }
    ],
    "name": "pairs",
    "outputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "pair0",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "pair1",
            "type": "address"
          }
        ],
        "internalType": "struct CoreBase.Pair",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes4",
        "name": "_func",
        "type": "bytes4"
      }
    ],
    "name": "pause",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "poolList",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "poolStats",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "totalBorrowAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "borrowInterestOwedPerDay",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "totalInterestPaid",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "totalBorrowAmountFromTrading",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "borrowInterestOwedPerDayFromTrading",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "totalInterestPaidFromTrading",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "updatedTimestamp",
            "type": "uint256"
          }
        ],
        "internalType": "struct CoreBase.PoolStat",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "poolToAsset",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      }
    ],
    "name": "positionConfigs",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "maintenanceMargin",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "minimumMargin",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "bountyFeeRateToProtocol",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "bountyFeeRateToLiquidator",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "forwRewardAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "positionSizeTargetInUSD",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "minOpenPositionSize",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "maxOpenPositionSize",
            "type": "uint256"
          }
        ],
        "internalType": "struct CoreBase.PositionConfig",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "positionStates",
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
        "internalType": "struct CoreBase.PositionState",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      }
    ],
    "name": "positions",
    "outputs": [
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
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "priceFeedAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "loanId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "repayAmount",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "isOnlyInterest",
        "type": "bool"
      }
    ],
    "name": "repay",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "borrowPaid",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "interestPaid",
        "type": "uint256"
      }
    ],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "loanId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      }
    ],
    "name": "rollover",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "delayInterest",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "collateralBountyReward",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "routers",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "loanId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      }
    ],
    "name": "settleBorrowInterest",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "settleForwInterest",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      },
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      }
    ],
    "name": "swapConfigs",
    "outputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "token0",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "maxSwapSize",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "maxPriceImpact",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "maxOraclePriceDiffPercent",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "maxLiquidationOraclePriceDiffPercent",
            "type": "uint256"
          }
        ],
        "internalType": "struct CoreBase.SwapConfig",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "swapFeeRates",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "swapableToken",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "tokenPrecisionUnit",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "totalCollateralHold",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "totalLossInUSD",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "tradingCollateralWhitelist",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "tradingFeeToLender",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes4",
        "name": "_func",
        "type": "bytes4"
      }
    ],
    "name": "unPause",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      }
    ],
    "name": "wallets",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "wethHandler",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
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
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "withdrawCollateral",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]