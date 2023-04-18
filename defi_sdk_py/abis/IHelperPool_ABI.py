IHELPERPOOL_ABI=[
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "poolAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "daySecond",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "borrowingAmount",
        "type": "uint256"
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
    "name": "calculateBorrowingInterest",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "ltv",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "interest",
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
        "name": "poolAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      }
    ],
    "name": "claimableInterest",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "tokenInterest",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "forwInterest",
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
        "name": "poolAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      }
    ],
    "name": "claimableInterestMembership",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "tokenInterest",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "forwInterest",
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
        "name": "poolAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "interestAmount",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "daySecond",
        "type": "uint256"
      }
    ],
    "name": "getDepositAmountByInterestAmount",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "depositAmount",
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
        "name": "poolAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "depositAmount",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "daySecond",
        "type": "uint256"
      }
    ],
    "name": "getInterestAmountByDepositAmount",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "interestAmount",
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
        "name": "poolAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      }
    ],
    "name": "getLendingInfo",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "lendingBalance",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "interestTokenGained",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "interestForwGained",
        "type": "uint256"
      },
      {
        "internalType": "uint8",
        "name": "rank",
        "type": "uint8"
      },
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "interestBonusLending",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "forwardBonusLending",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "minimumStakeAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "maxLTVBonus",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "tradingFee",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "tradingBonus",
            "type": "uint256"
          }
        ],
        "internalType": "struct StakePoolBase.RankInfo",
        "name": "rankInfo",
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
        "name": "poolAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "newDepositAmount",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "forwPriceRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "forwPricePrecision",
        "type": "uint256"
      }
    ],
    "name": "getNextLendingForwInterest",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "interestRate",
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
        "name": "poolAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "depositAmount",
        "type": "uint256"
      }
    ],
    "name": "getNextLendingInterest",
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
        "internalType": "address",
        "name": "poolAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "forwPriceRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "forwPricePrecision",
        "type": "uint256"
      }
    ],
    "name": "getPoolInfo",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "borrowingInterest",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "lendingTokenInterest",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "lendingForwInterest",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "utilizationRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "pTokenTotalSupply",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "currentSupply",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]