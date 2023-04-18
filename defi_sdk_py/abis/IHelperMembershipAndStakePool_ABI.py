IHELPERMEMBERSHIPANDSTAKEPOOL_ABI=[
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "getNFTList",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "count",
        "type": "uint256"
      },
      {
        "internalType": "uint256[]",
        "name": "nftList",
        "type": "uint256[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getRankInfoList",
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
        "internalType": "struct StakePoolBase.RankInfo[]",
        "name": "rankInfos",
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
        "name": "stakeInfo",
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
        "name": "stakePoolAddress",
        "type": "address"
      }
    ],
    "name": "getStakePoolNextSettleTimeStamp",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]