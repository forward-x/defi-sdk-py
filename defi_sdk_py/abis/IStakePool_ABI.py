ISTAKEPOOL_ABI=[
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      }
    ],
    "name": "deprecateStakeInfo",
    "outputs": [],
    "stateMutability": "nonpayable",
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
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      }
    ],
    "name": "getMaxLTVBonus",
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
      }
    ],
    "name": "getStakeInfo",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "stakeBalance",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "claimableAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint64",
            "name": "startTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint64",
            "name": "endTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint64",
            "name": "lastSettleTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint256[]",
            "name": "payPattern",
            "type": "uint256[]"
          }
        ],
        "internalType": "struct StakePoolBase.StakeInfo",
        "name": "",
        "type": "tuple"
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
        "internalType": "uint256",
        "name": "nftId",
        "type": "uint256"
      }
    ],
    "name": "migrate",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "stakeBalance",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "claimableAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint64",
            "name": "startTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint64",
            "name": "endTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint64",
            "name": "lastSettleTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint256[]",
            "name": "payPattern",
            "type": "uint256[]"
          }
        ],
        "internalType": "struct StakePoolBase.StakeInfo",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "nextPoolAddress",
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
    "inputs": [],
    "name": "poolStartTimestamp",
    "outputs": [
      {
        "internalType": "uint64",
        "name": "",
        "type": "uint64"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint8",
        "name": "",
        "type": "uint8"
      }
    ],
    "name": "rankInfos",
    "outputs": [
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
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "rankLen",
    "outputs": [
      {
        "internalType": "uint8",
        "name": "",
        "type": "uint8"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_address",
        "type": "address"
      }
    ],
    "name": "setNextPool",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint64",
        "name": "timestamp",
        "type": "uint64"
      }
    ],
    "name": "setPoolStartTimestamp",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256[]",
        "name": "_interestBonusLending",
        "type": "uint256[]"
      },
      {
        "internalType": "uint256[]",
        "name": "_forwardBonusLending",
        "type": "uint256[]"
      },
      {
        "internalType": "uint256[]",
        "name": "_minimumStakeAmount",
        "type": "uint256[]"
      },
      {
        "internalType": "uint256[]",
        "name": "_maxLTVBonus",
        "type": "uint256[]"
      },
      {
        "internalType": "uint256[]",
        "name": "_tradingFee",
        "type": "uint256[]"
      },
      {
        "internalType": "uint256[]",
        "name": "_tradingBonus",
        "type": "uint256[]"
      }
    ],
    "name": "setRankInfo",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "interval",
        "type": "uint256"
      }
    ],
    "name": "setSettleInterval",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "settleInterval",
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
    "name": "settlePeriod",
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
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "stake",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "stakeBalance",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "claimableAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint64",
            "name": "startTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint64",
            "name": "endTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint64",
            "name": "lastSettleTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint256[]",
            "name": "payPattern",
            "type": "uint256[]"
          }
        ],
        "internalType": "struct StakePoolBase.StakeInfo",
        "name": "stakeInfo",
        "type": "tuple"
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
    "name": "stakeInfos",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "stakeBalance",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "claimableAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint64",
            "name": "startTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint64",
            "name": "endTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint64",
            "name": "lastSettleTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint256[]",
            "name": "payPattern",
            "type": "uint256[]"
          }
        ],
        "internalType": "struct StakePoolBase.StakeInfo",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "stakeVaultAddress",
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
    "name": "totalStakeAmount",
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
        "name": "nftId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "unstake",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "stakeBalance",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "claimableAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint64",
            "name": "startTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint64",
            "name": "endTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint64",
            "name": "lastSettleTimestamp",
            "type": "uint64"
          },
          {
            "internalType": "uint256[]",
            "name": "payPattern",
            "type": "uint256[]"
          }
        ],
        "internalType": "struct StakePoolBase.StakeInfo",
        "name": "stakeInfo",
        "type": "tuple"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]