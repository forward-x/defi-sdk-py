IHELPERCORE_ABI=[
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "loanId",
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
        "name": "collateralAmount",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "collateralTokenAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "ltv",
        "type": "uint256"
      }
    ],
    "name": "calculateBorrowAmount",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "maxBorrowAmount",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "maxCollateralAmount",
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
        "name": "loanId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "isAdd",
        "type": "bool"
      }
    ],
    "name": "calculateLTVForAdjustColla",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "ltv",
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
        "name": "loanId",
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
        "name": "collateralAmount",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "collateralTokenAddress",
        "type": "address"
      }
    ],
    "name": "calculateLTVForBorrow",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "ltv",
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
        "name": "loanId",
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
    "name": "calculateLTVForRepay",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "ltv",
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
        "name": "loanId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "gapTimeBorrowInterestSecond",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "isOnlyInterest",
        "type": "bool"
      }
    ],
    "name": "calculateMaxRepay",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "maxRepay",
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
        "name": "cursor",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "resultsPerPage",
        "type": "uint256"
      }
    ],
    "name": "getActiveLoans",
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
        "internalType": "struct CoreBase.Loan[]",
        "name": "activeLoans",
        "type": "tuple[]"
      },
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "id",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "currentLTV",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "liquidationLTV",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "apr",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "minInterestOwed",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "actualInterestOwed",
            "type": "uint256"
          }
        ],
        "internalType": "struct HelperBase.ActiveLoanInfo[]",
        "name": "activeLoanInfos",
        "type": "tuple[]"
      },
      {
        "internalType": "uint256[]",
        "name": "interestOwedPerDays",
        "type": "uint256[]"
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
        "internalType": "uint256",
        "name": "loanId",
        "type": "uint256"
      }
    ],
    "name": "getLoanBorrowAmount",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "maximumBorrowAmount",
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
        "name": "loanId",
        "type": "uint256"
      }
    ],
    "name": "getLoanCollateralInfo",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "minimumCollateral",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "removableCollateral",
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
    "name": "getLoanCurrentLTV",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "ltv",
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
        "name": "loanId",
        "type": "uint256"
      }
    ],
    "name": "getPenaltyFee",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "penaltyFee",
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
        "name": "loanId",
        "type": "uint256"
      }
    ],
    "name": "getSettleBorrowInfo",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "settledBorrowAmount",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "settledLTV",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "rate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "precision",
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
        "name": "loanId",
        "type": "uint256"
      }
    ],
    "name": "isLoanLiquidable",
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
        "name": "poolAddess",
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
  }
]