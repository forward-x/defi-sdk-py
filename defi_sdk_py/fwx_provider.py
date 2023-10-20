import web3

import defi_sdk_py


class FwxWeb3:

    POSITIONS = "positions"
    ID = "id"
    ENTRY_PRICE = "entryPrice"
    CONTRACT_SIZE = "contractSize"
    BORROW_AMOUNT = "borrowAmount"
    COLLATERAL_USED = "collateralUsed"
    COLLATERAL_SWAPPED_AMOUNT = "collateralSwappedAmount"
    INTEREST_OWED = "interestOwed"
    INTEREST_OWED_PER_DAY = "interestOwedPerDay"
    INTEREST_OWE_PER_DAY = "interestOwePerDay"
    LAST_SETTLE_TIMESTAMP = "lastSettleTimestamp"

    POSITION_STATES = "positionStates"
    ACTIVE = "active"
    ISLONG = "isLong"
    PNL = "PNL"
    AVERAGE_ENTRY_PRICE = "averageEntryPrice"
    START_TIMESTAMP = "startTimestamp"
    INTEREST_PAID = "interestPaid"
    TOTAL_SWAP_FEE_PAID = "totalSwapFeePaid"
    TOTAL_SWAP_FEE = "totalSwapFee"
    TOTAL_TRADING_FEE_PAID = "totalTradingFeePaid"
    TOTAL_TRADING_FEE = "totalTradingFee"
    PAIR_BYTE = "pairByte"

    MINTED_P = "mintedP"
    MINTED_ATP = "mintedAtp"
    MINTED_ITP = "mintedItp"
    MINTED_IFP = "mintedIfp"

    PRINCIPLE = "principle"
    TOKEN_INTEREST = "tokenInterest"
    FORW_INTEREST = "forwInterest"
    P_TOKEN_BURN = "pTokenBurn"
    ATP_TOKEN_BURN = "atpTokenBurn"
    LOSS_BURN = "lossBurn"
    ITP_TOKEN_BURN = "itpTokenBurn"
    IFP_TOKEN_BURN = "ifpTokenBurn"
    TOKEN_INTEREST_BONUS = "tokenInterestBonus"
    FORW_INTEREST_BONUS = "forwInterestBonus"

    GET_LENDING_INFO = "getLendingInfo"

    INTEREST_TOKEN_GAINED = "interestTokenGained"
    INTEREST_FORW_GAINED = "interestForwGained"
    INTEREST_OBTAINED = "interestObtained"
    INTEREST_FWX_OBTAINED = "interestFwxObtained"

    LENDING_BALANCE = "lendingBalance"
    RANK = "rank"
    RANK_INFO = "rankInfo"
    INTEREST_BONUS_LENDING = "interestBonusLending"
    FORWARD_BONUS_LENDING = "forwardBonusLending"
    MINIMUM_STAKE_AMOUNT = "minimumStakeAmount"
    MAX_LTV_BONUS = "maxLTVBonus"
    TRADING_FEE = "tradingFee"
    TRADING_BONUS = "tradingBonus"

    ATP_PRICE = "atpPrice"
    ITP_PRICE = "itpPrice"
    IFP_PRICE = "ifpPrice"
    TOTAL_SUPPLY = "totalSupply"
    AVAILABLE_SUPPLY = "availableSupply"
    UTILIZATION_RATE = "utilizationRate"
    INTEREST_RATE = "interestRate"
    INTEREST_FWX_RATE = "interestFwxRate"

    ACTIVE_LOAN = "activeLoan"
    ACTIVE_LOAN_INFO = "activeLoanInfo"

    LOANS = "loans"
    INTEREST_PAID = "interestPaid"
    BORROW_TOKEN_ADDRESS = "borrowTokenAddress"
    ROLLOVER_TIMESTAMP = "rolloverTimestamp"
    LAST_SETTLE_TIMESTAMP = "lastSettleTimestamp"
    COLLATERAL_TOKEN_ADDRESS = "collateralTokenAddress"
    BORROW_AMOUNT = "borrowAmount"
    COLLATERAL_AMOUNT = "collateralAmount"
    OWED_PER_DAY = "owedPerDay"
    MIN_INTEREST = "minInterest"
    INTEREST_OWED = "interestOwed"

    BORROW_PAID = "borrowPaid"

    LOAN_EXTS = "loanExts"

    DELAY_INTEREST = "delayInterest"
    BOUNTY_REWARD = "bountyReward"

    FREE_BALANCE = "freeBalance"
    USED_BALANCE = "usedBalance"
    TOTAL_BALANCE = "totalBalance"

    COLLATERAL_ADDRESS = "collateralAddress"
    UNDERLYING_ADDRESS = "underlyingAddress"

    def __init__(self, url):
        self.w3 = web3.Web3(web3.HTTPProvider(url))

    def setSigner(self, privateKey):
        self.signer = web3.Account.privateKeyToAccount(privateKey)

    # Membership

    # mint
    # - **Instance**: Membership
    # - **Parameters**
    #     - referral: BigNumberish
    # - **Output**
    #     - tokenId: BigNumberish
    def mint(self, referral, gas=220000, gasPrice=25, nonce=0):
        membership = self.__getMembership()

        tx = membership.functions.mint(
            referral
        ).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
            }
        )
        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        txReceipt = self.w3.eth.wait_for_transaction_receipt(txHash)
        if txReceipt["status"] == 0:
            return (txHash, -1)
        helperMembershipAndStakePool = self.__getHelperMembershipAndStakePool()
        result = helperMembershipAndStakePool.functions.getNFTList(
            self.signer.address).call()
        return (txHash, result[1][len(result[1])-1])

    # Lending

    # deposit
    # - **Instance**: APHPool
    # - **Parameters**
    #     - pool: TokenSymbols
    #     - nftId: BigNumberish
    #     - depositAmount: BigNumberish
    # - **Output**
    #     - mintedP: BigNumberish
    #     - mintedAtp: BigNumberish
    #     - mintedItp: BigNumberish
    #     - mintedIfp: BigNumberish
    def deposit(self, poolTokenSymbol, nftId, depositAmount, gas=500000, gasPrice=25, nonce=0):
        validateToken(poolTokenSymbol)
        poolTokenDecimal = self.__getTokenDecimal(poolTokenSymbol)
        depositAmount = int(depositAmount * 10**poolTokenDecimal)
        pool = self.__getPool(poolTokenSymbol)
        tx = pool.functions.deposit(nftId, depositAmount).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
                'value': depositAmount if self.__isTokenSymbolNative(poolTokenSymbol) else 0
            }
        )
        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        txReceipt = self.w3.eth.wait_for_transaction_receipt(txHash)

        result = {}
        for log in txReceipt["logs"]:
            if log["topics"][0].hex() == "0x55e1b84deec6eefe49c2c96afe1d5b43ca37768907f7388696c6009e7bbe3b54":
                data = log["data"][2:]
                result[FwxWeb3.MINTED_P] = int(
                    data[32:64], 16) / 10**poolTokenDecimal
                result[FwxWeb3.MINTED_ATP] = int(
                    data[64:96], 16) / 10**poolTokenDecimal
                result[FwxWeb3.MINTED_ITP] = int(
                    data[96:128], 16) / 10**poolTokenDecimal
                result[FwxWeb3.MINTED_IFP] = int(data[128:160], 16) / 10**18

        return (txHash, result)

    # withdraw
    # - **Instance**: APHPool
    # - **Parameters**
    #     - token: TokenSymbols
    #     - nftId: BigNumberish
    #     - withdrawAmount: BigNumberish
    # - **Output**
    #     - result: WithdrawResult (struct from solidity)
    def withdraw(self, poolTokenSymbol, nftId, withdrawAmount, gas=700000, gasPrice=25, nonce=0):
        validateToken(poolTokenSymbol)
        poolTokenDecimal = self.__getTokenDecimal(poolTokenSymbol)
        withdrawAmount = int(withdrawAmount * 10**poolTokenDecimal)
        pool = self.__getPool(poolTokenSymbol)
        tx = pool.functions.withdraw(nftId, withdrawAmount).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei')
            }
        )
        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        txReceipt = self.w3.eth.wait_for_transaction_receipt(txHash)
        result = {
            FwxWeb3.PRINCIPLE: 0.0,
            FwxWeb3.TOKEN_INTEREST: 0.0,
            FwxWeb3.FORW_INTEREST: 0.0,
            FwxWeb3.P_TOKEN_BURN: 0.0,
            FwxWeb3.ATP_TOKEN_BURN: 0.0,
            FwxWeb3.LOSS_BURN: 0.0,
            FwxWeb3.ITP_TOKEN_BURN: 0.0,
            FwxWeb3.IFP_TOKEN_BURN: 0.0,
            FwxWeb3.TOKEN_INTEREST_BONUS: 0,
            FwxWeb3.FORW_INTEREST_BONUS: 0.0
        }

        for log in txReceipt["logs"]:
            if log["topics"][0].hex() == "0x25dd09722d1e76ffb961a71292eafb472dcb7453dd24aafe730779e6d6cf7190":
                data = log["data"][2:]
                result[FwxWeb3.PRINCIPLE] += int(data[0:32], 16) / \
                    10**poolTokenDecimal
                result[FwxWeb3.P_TOKEN_BURN] += int(
                    data[32:64], 16) / 10**poolTokenDecimal
                result[FwxWeb3.ATP_TOKEN_BURN] += int(
                    data[64:96], 16) / 10**poolTokenDecimal
                result[FwxWeb3.LOSS_BURN] += int(data[96:128],
                                                 16) / 10**poolTokenDecimal
                result[FwxWeb3.ITP_TOKEN_BURN] += int(
                    data[128:160], 16) / 10**poolTokenDecimal
                result[FwxWeb3.IFP_TOKEN_BURN] += int(
                    data[160:192], 16) / 10**18
            elif log["topics"][0].hex() == "0x199a7a8ae450da3700d2c3bd80f41a0f29b853dbde55f79199d8956ec3267dd6":
                data = log["data"][2:]
                result[FwxWeb3.TOKEN_INTEREST] += int(
                    data[0:32], 16) / 10**poolTokenDecimal
                result[FwxWeb3.TOKEN_INTEREST_BONUS] += int(
                    data[32:64], 16) / 10**poolTokenDecimal
                result[FwxWeb3.ITP_TOKEN_BURN] += int(
                    data[64:96], 16) / 10**poolTokenDecimal
            elif log["topics"][0].hex() == "0x7306e65aafc988ed7e1a7a3546c7a79dace207c76c10db147dc0e3a1a218e0af":
                data = log["data"][2:]
                result[FwxWeb3.FORW_INTEREST] += int(data[0:32], 16) / 10**18
                result[FwxWeb3.FORW_INTEREST_BONUS] += int(
                    data[32:64], 16) / 10**18
                result[FwxWeb3.IFP_TOKEN_BURN] += int(data[64:96], 16) / 10**18
        return (txHash, result)

    # claimAllInterest
    # - **Instance**: APHPool
    # - **Parameters**
    #     - pool: TokenSymbols
    #     - nftId: BigNumberish
    # - **Output**
    #     - result: WithdrawResult (struct from solidity)
    def claimAllInterest(self, poolTokenSymbol, nftId, gas=700000, gasPrice=25, nonce=0):
        validateToken(poolTokenSymbol)
        poolTokenDecimal = self.__getTokenDecimal(poolTokenSymbol)
        pool = self.__getPool(poolTokenSymbol)
        tx = pool.functions.claimAllInterest(nftId).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei')
            }
        )
        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        txReceipt = self.w3.eth.wait_for_transaction_receipt(txHash)
        result = {
            FwxWeb3.PRINCIPLE: 0.0,
            FwxWeb3.TOKEN_INTEREST: 0.0,
            FwxWeb3.FORW_INTEREST: 0.0,
            FwxWeb3.P_TOKEN_BURN: 0.0,
            FwxWeb3.ATP_TOKEN_BURN: 0.0,
            FwxWeb3.LOSS_BURN: 0.0,
            FwxWeb3.ITP_TOKEN_BURN: 0.0,
            FwxWeb3.IFP_TOKEN_BURN: 0.0,
            FwxWeb3.TOKEN_INTEREST_BONUS: 0.0,
            FwxWeb3.FORW_INTEREST_BONUS: 0.0
        }

        for log in txReceipt["logs"]:
            if log["topics"][0].hex() == "0x25dd09722d1e76ffb961a71292eafb472dcb7453dd24aafe730779e6d6cf7190":
                data = log["data"][2:]
                result[FwxWeb3.PRINCIPLE] += int(data[0:32], 16) / \
                    10**poolTokenDecimal
                result[FwxWeb3.P_TOKEN_BURN] += int(
                    data[32:64], 16) / 10**poolTokenDecimal
                result[FwxWeb3.ATP_TOKEN_BURN] += int(
                    data[64:96], 16) / 10**poolTokenDecimal
                result[FwxWeb3.LOSS_BURN] += int(data[96:128],
                                                 16) / 10**poolTokenDecimal
                result[FwxWeb3.ITP_TOKEN_BURN] += int(
                    data[128:160], 16) / 10**poolTokenDecimal
                result[FwxWeb3.IFP_TOKEN_BURN] += int(
                    data[160:192], 16) / 10**18
            elif log["topics"][0].hex() == "0x199a7a8ae450da3700d2c3bd80f41a0f29b853dbde55f79199d8956ec3267dd6":
                data = log["data"][2:]
                result[FwxWeb3.TOKEN_INTEREST] += int(
                    data[0:32], 16) / 10**poolTokenDecimal
                result[FwxWeb3.TOKEN_INTEREST_BONUS] += int(
                    data[32:64], 16) / 10**poolTokenDecimal
                result[FwxWeb3.ITP_TOKEN_BURN] += int(
                    data[64:96], 16) / 10**poolTokenDecimal
            elif log["topics"][0].hex() == "0x7306e65aafc988ed7e1a7a3546c7a79dace207c76c10db147dc0e3a1a218e0af":
                data = log["data"][2:]
                result[FwxWeb3.FORW_INTEREST] += int(data[0:32], 16) / 10**18
                result[FwxWeb3.FORW_INTEREST_BONUS] += int(
                    data[32:64], 16) / 10**18
                result[FwxWeb3.IFP_TOKEN_BURN] += int(data[64:96], 16) / 10**18
        return (txHash, result)

    # getLendingInfo
    # - **Instance**: APHPool
    # - **Parameters**
    #     - pool: TokenSymbols
    #     - nftId: BigNumberish
    # - **Output**
    #     - lendingBalance: BigNumberish
    #     - interestObtained: BigNumberish
    #     - interestFwxObtained: BigNumberish
    #     - rank: BigNumberish
    #     - rankInfo: StakePool.RankInfo (struct from solidity)
    def getLendingInfo(self, poolTokenSymbol, nftId):
        helper = self.__getHelperPool()
        poolTokenDecimal = self.__getTokenDecimal(poolTokenSymbol)
        info = helper.functions.getLendingInfo(
            defi_sdk_py.ADDRESSES["AVAX"]["POOL"][poolTokenSymbol], nftId).call()
        abi = next(filter(lambda abis: FwxWeb3.filterFunctionABI(
            abis, FwxWeb3.GET_LENDING_INFO), helper.abi))
        result = FwxWeb3.tupleOutputDecode(info, abi)[FwxWeb3.GET_LENDING_INFO]

        result[FwxWeb3.INTEREST_OBTAINED] = result[FwxWeb3.INTEREST_TOKEN_GAINED] / \
            10**poolTokenDecimal
        result[FwxWeb3.INTEREST_FWX_OBTAINED] = result[FwxWeb3.INTEREST_FORW_GAINED] / 10**18
        result.pop(FwxWeb3.INTEREST_TOKEN_GAINED)
        result.pop(FwxWeb3.INTEREST_FORW_GAINED)

        result[FwxWeb3.LENDING_BALANCE] /= 10**poolTokenDecimal
        result[FwxWeb3.RANK_INFO][FwxWeb3.INTEREST_BONUS_LENDING] /= 10**20
        result[FwxWeb3.RANK_INFO][FwxWeb3.FORWARD_BONUS_LENDING] /= 10**20
        result[FwxWeb3.RANK_INFO][FwxWeb3.MINIMUM_STAKE_AMOUNT] /= 10**18
        result[FwxWeb3.RANK_INFO][FwxWeb3.MAX_LTV_BONUS] /= 10**20
        result[FwxWeb3.RANK_INFO][FwxWeb3.TRADING_FEE] /= 10**20
        result[FwxWeb3.RANK_INFO][FwxWeb3.TRADING_BONUS] /= 10**20
        return result

    # getLendingInfoPlatform
    # - **Instance**: APHPool
    # - **Parameters**
    #     - pool: TokenSymbols
    # - **Output**
    #     - atpPrice: BigNumberish
    #     - itpPrice: BigNumberish
    #     - ifpPrice: BigNumberish
    #     - totalSupply: BigNumberish
    #     - availableSupply: BigNumberish
    #     - utilizationRate: BigNumberish
    #     - interestRate: BigNumberish (current rate)
    #     - interestFwxRate: BigNumberish (current rate)
    def getLendingInfoPlatform(self, poolTokenSymbol, forwPriceRate=15000000000000000000, forwPricePrecision=10000000000000000000):
        validateToken(poolTokenSymbol)
        helper = self.__getHelperPool()
        poolTokenDecimal = self.__getTokenDecimal(poolTokenSymbol)
        pool = self.__getPool(poolTokenSymbol)
        aptPrice = pool.functions.getActualTokenPrice().call()
        itpPrice = pool.functions.getInterestTokenPrice().call()
        ifpPrice = pool.functions.getInterestForwPrice().call()
        totalSupply = pool.functions.pTokenTotalSupply().call()
        availableSupply = pool.functions.currentSupply().call()
        utilizationRate = pool.functions.utilizationRate().call()
        interestRate = helper.functions.getNextLendingInterest(
            defi_sdk_py.ADDRESSES["AVAX"]["POOL"][poolTokenSymbol], 0).call()
        interestFwxRate = helper.functions.getNextLendingForwInterest(
            defi_sdk_py.ADDRESSES["AVAX"]["POOL"][poolTokenSymbol], 0, forwPriceRate, forwPricePrecision).call()

        result = {
            FwxWeb3.ATP_PRICE: aptPrice / 10**poolTokenDecimal,
            FwxWeb3.ITP_PRICE: itpPrice / 10**poolTokenDecimal,
            FwxWeb3.IFP_PRICE: ifpPrice / 10**18,
            FwxWeb3.TOTAL_SUPPLY: totalSupply / 10**poolTokenDecimal,
            FwxWeb3.AVAILABLE_SUPPLY: availableSupply / 10**poolTokenDecimal,
            FwxWeb3.UTILIZATION_RATE: utilizationRate / 10**18,
            FwxWeb3.INTEREST_RATE: interestRate / 10**18,
            FwxWeb3.INTEREST_FWX_RATE: interestFwxRate / 10**18,
        }
        return result

    # getInterestRate
    # - **Instance**: APHPool
    # - **Parameters**
    #     - pool: TokenSymbols
    #     - depositAmount?: BigNumberish
    # - **Output**
    #     - interestRate: BigNumberish
    def getInterestRate(self, poolTokenSymbol, depositAmount):
        validateToken(poolTokenSymbol)
        helper = self.__getHelperPool()
        poolTokenDecimal = self.__getTokenDecimal(poolTokenSymbol)
        depositAmount = int(depositAmount * 10**poolTokenDecimal)
        return helper.functions.getNextLendingInterest(
            defi_sdk_py.ADDRESSES["AVAX"]["POOL"][poolTokenSymbol], depositAmount).call() / 10**18

    # getFwxInterestRate
    # - **Instance**: APHPool
    # - **Parameters**
    #     - pool: TokenSymbols
    #     - depositAmount?: BigNumberish
    # - **Output**
    #     - fwxInterestRate: BigNumberish
    def getFwxInterestRate(self, poolTokenSymbol, depositAmount, forwPriceRate=15000000000000000000, forwPricePrecision=10000000000000000000):
        validateToken(poolTokenSymbol)
        helper = self.__getHelperPool()
        poolTokenDecimal = self.__getTokenDecimal(poolTokenSymbol)
        depositAmount = int(depositAmount * 10**poolTokenDecimal)
        return helper.functions.getNextLendingForwInterest(
            defi_sdk_py.ADDRESSES["AVAX"]["POOL"][poolTokenSymbol], 0, forwPriceRate, forwPricePrecision).call() / 10**18

    # Borrowing

    # borrow
    # - **Instance**: APHPool
    # - **Parameters**
    #     - pool: TokenSymbols
    #     - nftId: BigNumberish
    #     - loanId: BigNumberish
    #     - borrowAmount: BigNumberish
    #     - collateralAmount: BigNumberish
    #     - collateralToken: TokenSymbols
    # - **Output**
    #     - result: CoreBase.Loan (struct from solidity)
    def borrow(self, poolTokenSymbol, nftId, loanId, borrowAmount, collateralAmount, collateralTokenSymbol, gas=800000, gasPrice=25, nonce=0):
        validatePair(collateralTokenSymbol, poolTokenSymbol)
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        poolTokenDecimal = self.__getTokenDecimal(poolTokenSymbol)
        pool = self.__getPool(poolTokenSymbol)
        collateralAmount = int(collateralAmount * 10**collateralDecimal)
        borrowAmount = int(borrowAmount * 10**poolTokenDecimal)
        tx = pool.functions.borrow(
            loanId,
            nftId,
            borrowAmount,
            collateralAmount,
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol]
        ).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
                'value': collateralAmount if self.__isTokenSymbolNative(collateralTokenSymbol) else 0
            }
        )
        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        txReceipt = self.w3.eth.wait_for_transaction_receipt(txHash)
        result = {}
        for log in txReceipt["logs"]:
            if log["topics"][0].hex() == "0xdc7693ea123824cbf513f8d942f777f8ae0b41e557aa4317e938c087b5483ef7":
                loanId = int(log["topics"][3].hex(), 16)

                loanInfo = self.getLoanInfo(nftId, loanId)
                loanInfo.pop(FwxWeb3.ACTIVE)
                loanInfo.pop(FwxWeb3.START_TIMESTAMP)
                result = loanInfo
        return (txHash, result)

    # repay
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - loanId: BigNumberish
    #     - repayAmount: BigNumberish
    # - **Output**
    #     - borrowPaid: BigNumberish
    #     - interestPaid: BigNumberish
    def repay(self, nftId, loanId, repayAmount, gas=800000, gasPrice=25, nonce=0):
        return self.__repay(nftId, loanId, repayAmount, False, gas, gasPrice, nonce)

    # repayInterest
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - loanId: BigNumberish
    #     - repayAmount: BigNumberish
    # - **Output**
    #     - interestPaid: BigNumberish
    def repayInterest(self, nftId, loanId, repayAmount, gas=800000, gasPrice=25, nonce=0):
        repayResult = self.__repay(
            nftId, loanId, repayAmount, True, gas, gasPrice, nonce)
        repayResult[1].pop(FwxWeb3.BORROW_PAID)
        return repayResult

    def __repay(self, nftId, loanId, repayAmount, isOnlyInterest, gas, gasPrice, nonce):
        loanInfo = self.__getLoanInfo(nftId, loanId)
        txHash = None
        result = {
            FwxWeb3.BORROW_PAID: 0,
            FwxWeb3.INTEREST_PAID: 0,
        }
        if loanInfo[FwxWeb3.ACTIVE]:
            borrowTokenDecimal = self.__getTokenDecimalFromAddress(
                loanInfo[FwxWeb3.BORROW_TOKEN_ADDRESS])
            repayAmount = int(repayAmount * 10 ** borrowTokenDecimal)
            core = self.__getCore()
            tx = core.functions.repay(
                loanId,
                nftId,
                repayAmount,
                isOnlyInterest,
            ).buildTransaction(
                {
                    'from': self.signer.address,
                    'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                    'gas': gas,
                    'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
                    'value': repayAmount if self.__isTokenAddressNative(loanInfo[FwxWeb3.BORROW_TOKEN_ADDRESS]) else 0
                }
            )
            # Sign tx
            signedTx = self.w3.eth.account.sign_transaction(
                tx, self.signer.key)

            # Send tx
            txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
            txReceipt = self.w3.eth.wait_for_transaction_receipt(txHash)

            for log in txReceipt["logs"]:
                if log["topics"][0].hex() == "0x4cabfc094acff5e29e506e4b4123342242cb3c366bc94779f4cc5459a3a2ab2f":
                    data = log["data"][2:]
                    result[FwxWeb3.BORROW_PAID] = int(
                        data[41:73], 16) / 10 ** borrowTokenDecimal
                    result[FwxWeb3.INTEREST_PAID] = int(
                        data[73:105], 16) / 10 ** borrowTokenDecimal

        return (txHash, result)

    # addCollateral
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - loanId: BigNumberish
    #     - collateralAmount: BigNumberish
    # - **Output**
    #     - result: CoreBase.Loan (struct from solidity)
    def addCollateral(self, nftId, loanId, collateralAmount, gas=800000, gasPrice=25, nonce=0):
        return self.__adjustCollateral(nftId, loanId, collateralAmount, True, gas, gasPrice, nonce)

    # removeCollateral
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - loanId: BigNumberish
    #     - collateralAmount: BigNumberish
    # - **Output**
    #     - result: CoreBase.Loan (struct from solidity)
    def removeCollateral(self, nftId, loanId, collateralAmount, gas=800000, gasPrice=25, nonce=0):
        return self.__adjustCollateral(nftId, loanId, collateralAmount, False, gas, gasPrice, nonce)

    def __adjustCollateral(self, nftId, loanId, collateralAmount, isAdd, gas, gasPrice, nonce):
        loanInfo = self.__getLoanInfo(nftId, loanId)
        txHash = None
        if loanInfo[FwxWeb3.ACTIVE]:
            collateralTokenDecimal = self.__getTokenDecimalFromAddress(
                loanInfo[FwxWeb3.COLLATERAL_TOKEN_ADDRESS])
            collateralAmount = collateralAmount * 10 ** collateralTokenDecimal
            core = self.__getCore()
            tx = core.functions.adjustCollateral(
                loanId,
                nftId,
                collateralAmount,
                isAdd,
            ).buildTransaction(
                {
                    'from': self.signer.address,
                    'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                    'gas': gas,
                    'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
                    'value': collateralAmount if self.__isTokenAddressNative(loanInfo[FwxWeb3.COLLATERAL_TOKEN_ADDRESS]) else 0
                }
            )
            # Sign tx
            signedTx = self.w3.eth.account.sign_transaction(
                tx, self.signer.key)

            # Send tx
            txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
            self.w3.eth.wait_for_transaction_receipt(txHash)

        result = self.getLoanInfo(nftId, loanId)
        result.pop(FwxWeb3.ACTIVE)
        result.pop(FwxWeb3.START_TIMESTAMP)
        return (txHash, result)

    # rollover
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - loanId: BigNumberish
    # - **Output**
    #     - delayInterest: BigNumberish
    #     - bountyReward: BigNumberish
    def rollover(self, nftId, loanId, gas=800000, gasPrice=25, nonce=0):
        loanInfo = self.__getLoanInfo(nftId, loanId)
        txHash = None
        result = {
            FwxWeb3.DELAY_INTEREST: 0.0,
            FwxWeb3.BOUNTY_REWARD: 0.0
        }
        if loanInfo[FwxWeb3.ACTIVE]:
            borrowTokenDecimal = self.__getTokenDecimalFromAddress(
                loanInfo[FwxWeb3.BORROW_TOKEN_ADDRESS])
            collateralTokenDecimal = self.__getTokenDecimalFromAddress(
                loanInfo[FwxWeb3.COLLATERAL_TOKEN_ADDRESS])
            core = self.__getCore()
            tx = core.functions.rollover(
                loanId,
                nftId
            ).buildTransaction(
                {
                    'from': self.signer.address,
                    'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                    'gas': gas,
                    'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
                }
            )
            # Sign tx
            signedTx = self.w3.eth.account.sign_transaction(
                tx, self.signer.key)

            # Send tx
            txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
            txReceipt = self.w3.eth.wait_for_transaction_receipt(txHash)
            for log in txReceipt["logs"]:
                if log["topics"][0].hex() == "0xa0ae618c42c745519d96383f66c106adaa07218816e5d7cdeb6fa33ecfaeac38":
                    data = log["data"][2:]
                    result[FwxWeb3.DELAY_INTEREST] = int(
                        data[40:72], 16) / 10**borrowTokenDecimal
                    result[FwxWeb3.BOUNTY_REWARD] = int(
                        data[72:104], 16) / 10**collateralTokenDecimal
        return (txHash, result)

    # getLoanInfo
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - loanId: BigNumberish
    # - **Output**
    #     - active: bool
    #     - startTimestamp: BigNumberish
    #     - borrowToken: address -> borrowTokenAddress
    #     - collateralToken: address -> collateralTokenAddress
    #     - lastSettleTimestamp: BigNumberish
    #     - rolloverTimestamp: BigNumberish
    #     - borrowAmount: BigNumberish
    #     - collateralAmount: BigNumberish
    #     - owedPerDay: BigNumberish
    #     - minInterest: BigNumberish
    #     - interestOwed: BigNumberish
    #     - interestPaid: BigNumberish
    def getLoanInfo(self, nftId, loanId):
        loanInfo = self.__getLoanInfo(nftId, loanId)
        borrowTokenDecimal = self.__getTokenDecimalFromAddress(
            loanInfo[FwxWeb3.BORROW_TOKEN_ADDRESS])
        collateralTokenDecimal = self.__getTokenDecimalFromAddress(
            loanInfo[FwxWeb3.COLLATERAL_TOKEN_ADDRESS])
        loanInfo[FwxWeb3.BORROW_AMOUNT] = loanInfo[FwxWeb3.BORROW_AMOUNT] / \
            10 ** borrowTokenDecimal
        loanInfo[FwxWeb3.COLLATERAL_AMOUNT] = loanInfo[FwxWeb3.COLLATERAL_AMOUNT] / \
            10 ** collateralTokenDecimal
        loanInfo[FwxWeb3.OWED_PER_DAY] = loanInfo[FwxWeb3.OWED_PER_DAY] / \
            10 ** borrowTokenDecimal
        loanInfo[FwxWeb3.MIN_INTEREST] = loanInfo[FwxWeb3.MIN_INTEREST] / \
            10 ** borrowTokenDecimal
        loanInfo[FwxWeb3.INTEREST_OWED] = loanInfo[FwxWeb3.INTEREST_OWED] / \
            10 ** borrowTokenDecimal
        loanInfo[FwxWeb3.INTEREST_PAID] = loanInfo[FwxWeb3.INTEREST_PAID] / \
            10 ** borrowTokenDecimal
        return loanInfo

    def __getLoanInfo(self, nftId, loanId):
        core = self.__getCore()
        abi = next(filter(lambda abis: FwxWeb3.filterFunctionABI(
            abis, FwxWeb3.LOANS), core.abi))
        loan = core.functions.loans(nftId, loanId).call()
        loan = FwxWeb3.tupleOutputDecode(loan, abi)[FwxWeb3.LOANS]

        abi = next(filter(lambda abis: FwxWeb3.filterFunctionABI(
            abis, FwxWeb3.LOAN_EXTS), core.abi))
        loanExt = core.functions.loanExts(nftId, loanId).call()
        loanExt = FwxWeb3.tupleOutputDecode(loanExt, abi)[FwxWeb3.LOAN_EXTS]
        result = {
            FwxWeb3.ACTIVE: loanExt[FwxWeb3.ACTIVE],
            FwxWeb3.START_TIMESTAMP: loanExt[FwxWeb3.START_TIMESTAMP],
            FwxWeb3.BORROW_TOKEN_ADDRESS: loan[FwxWeb3.BORROW_TOKEN_ADDRESS],
            FwxWeb3.COLLATERAL_TOKEN_ADDRESS: loan[FwxWeb3.COLLATERAL_TOKEN_ADDRESS],
            FwxWeb3.LAST_SETTLE_TIMESTAMP: loan[FwxWeb3.LAST_SETTLE_TIMESTAMP],
            FwxWeb3.ROLLOVER_TIMESTAMP: loan[FwxWeb3.ROLLOVER_TIMESTAMP],
            FwxWeb3.BORROW_AMOUNT: loan[FwxWeb3.BORROW_AMOUNT],
            FwxWeb3.COLLATERAL_AMOUNT: loan[FwxWeb3.COLLATERAL_AMOUNT],
            FwxWeb3.OWED_PER_DAY: loan[FwxWeb3.OWED_PER_DAY],
            FwxWeb3.MIN_INTEREST: loan[FwxWeb3.MIN_INTEREST],
            FwxWeb3.INTEREST_OWED: loan[FwxWeb3.INTEREST_OWED],
            FwxWeb3.INTEREST_PAID: loan[FwxWeb3.INTEREST_PAID],
        }
        return result

    # getBorrowingInterestRate
    # - **Instance**: APHPool
    # - **Parameters**
    #     - pool: TokenSymbols
    #     - borrowAmount?: BigNumberish
    # - **Output**
    #     - interestRate: BigNumberish
    #     - interestOwedPerDay: BigNumberish
    def getBorrowingInterestRate(self, poolTokenSymbol, borrowAmount):
        validateToken(poolTokenSymbol)
        pool = self.__getPool(poolTokenSymbol)
        borrowTokenDecimal = self.__getTokenDecimal(poolTokenSymbol)
        borrowAmount = int(borrowAmount * 10**borrowTokenDecimal)

        interestInfo = pool.functions.calculateInterest(borrowAmount).call()
        result = {
            FwxWeb3.INTEREST_RATE: interestInfo[0] / 10**borrowTokenDecimal,
            FwxWeb3.INTEREST_OWED_PER_DAY: interestInfo[1] / 10**borrowTokenDecimal,
        }
        return result

    def __getActiveLoan(self, nftId):
        helperCore = self.__getHelperCore()
        core = self.__getCore()
        currentLoanIndex = core.functions.currentLoanIndex(nftId).call()
        newCursor = 1
        resultPerPage = 10
        results = []
        abi = next(filter(lambda abis: FwxWeb3.filterFunctionABI(
            abis, FwxWeb3.LOANS), core.abi))

        while newCursor <= currentLoanIndex:
            helperReturn = helperCore.functions.getActiveLoans(
                nftId, newCursor, resultPerPage).call()
            results += list(
                map(
                    lambda lst: dict(
                        (key, v) for key, v in zip(
                            [FwxWeb3.ACTIVE_LOAN, FwxWeb3.ACTIVE_LOAN_INFO,
                             FwxWeb3.INTEREST_OWE_PER_DAY],
                            [FwxWeb3.tupleOutputDecode(
                                lst[0], abi)[FwxWeb3.LOANS], lst[1], lst[2]]
                        )
                    ),
                    [[helperReturn[0][i], helperReturn[1][i], helperReturn[2][i]]
                        for i in range(len(helperReturn[0]))]
                )
            )
            newCursor = helperReturn[3]
        return results

    # Trading

    # openPosition
    # - **Instance**: APHPool
    # - **Note**: The user doesn’t have to know borrow token and swap token, just choose collateral and underlying then trade.
    # - **Parameters**
    #     - isLong: boolean
    #     - collateral: TokenSymbols
    #     - underlying: TokenSymbols
    #     - nftId: BigNumberish
    #     - entryPrice: BigNumberish
    #     - contractSize: BigNumberish
    #     - leverage: BigNumberish
    #     - slippage: BigNumberish
    # - **Output**
    #     - result: CoreBase.Position (struct from solidity)
    def openPosition(self, isLong, collateralTokenSymbol, underlyingTokenSymbol, nftId, entryPrice, contractSize, leverage, slippage, gas=1300000, gasPrice=25, nonce=0):
        validatePair(collateralTokenSymbol, underlyingTokenSymbol)
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        underlyingDecimal = self.__getTokenDecimal(underlyingTokenSymbol)

        tx = None
        contractSize = int(contractSize * 10**underlyingDecimal)
        leverage = int(leverage * 10**18)
        slippage = int(slippage * 10**18)
        entryPrice = entryPrice * 10**collateralDecimal
        if isLong:
            pool = self.__getPool(collateralTokenSymbol)
            tx = pool.functions.openPosition(
                nftId,
                defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
                defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol],
                entryPrice,
                contractSize,
                leverage,
                slippage
            ).buildTransaction(
                {
                    'from': self.signer.address,
                    'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                    'gas': gas,
                    'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
                }
            )
        else:
            pool = self.__getPool(underlyingTokenSymbol)
            tx = pool.functions.openPosition(
                nftId,
                defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
                defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
                entryPrice,
                contractSize,
                leverage,
                slippage
            ).buildTransaction(
                {
                    'from': self.signer.address,
                    'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                    'gas': gas,
                    'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
                }
            )
        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(txHash)
        position = self.__getPosition(
            nftId, collateralTokenSymbol, underlyingTokenSymbol)
        return (txHash, position)

    # closePosition
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - posId: BigNumberish
    #     - closingSize: BigNumberish
    # - **Output**
    #     - result: CoreBase.Position (struct from solidity)
    def closePosition(self, nftId, posId, closingSize, gas=1300000, gasPrice=25, nonce=0):
        positionState = self.__getPositionState(nftId, posId)
        pair = self.__getPair(
            positionState[FwxWeb3.PAIR_BYTE])
        underlyingDecimal = self.__getTokenDecimalFromAddress(
            pair[FwxWeb3.UNDERLYING_ADDRESS])
        closingSize = int(closingSize * 10**underlyingDecimal)
        core = self.__getCore()
        tx = core.functions.closePosition(
            nftId,
            posId,
            closingSize
        ).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
            }
        )

        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(txHash)
        position = self.__getPositionFromAddress(
            nftId, pair[FwxWeb3.COLLATERAL_ADDRESS], pair[FwxWeb3.UNDERLYING_ADDRESS])
        return (txHash, position)

    # depositCollateral
    # - **Instance**: APHCore
    # - **Parameters**
    #     - collateral: TokenSymbols
    #     - underlying: TokenSymbols
    #     - nftId: BigNumberish
    #     - amount: BigNumberish
    # - **Output**
    #     - balance: BigNumberish
    def depositCollateral(self, collateralTokenSymbol, underlyingTokenSymbol, nftId, amount, gas=1300000, gasPrice=25, nonce=0):
        validatePair(collateralTokenSymbol, underlyingTokenSymbol)
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        amount = int(amount * 10 ** collateralDecimal)
        core = self.__getCore()
        library = self.__getLibrary()
        tx = core.functions.depositCollateral(nftId, defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol], defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol], amount).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
            }
        )

        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(txHash)
        pairByte = library.functions.hashPair(
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol],
        ).call()
        balance = core.functions.wallets(nftId, pairByte).call()
        return (txHash, balance / 10 ** collateralDecimal)

    # withdrawCollateral
    # - **Instance**: APHCore
    # - **Parameters**
    #     - collateral: TokenSymbols
    #     - underlying: TokenSymbols
    #     - nftId: BigNumberish
    #     - amount: BigNumberish
    # - **Output**
    #     - balance: BigNumberish
    def withdrawCollateral(self, collateralTokenSymbol, underlyingTokenSymbol, nftId, amount, gas=1300000, gasPrice=25, nonce=0):
        validatePair(collateralTokenSymbol, underlyingTokenSymbol)
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        amount = int(amount * 10**collateralDecimal)
        core = self.__getCore()
        library = self.__getLibrary()
        tx = core.functions.withdrawCollateral(nftId, defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol], defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol], amount).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
            }
        )

        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(txHash)
        pairByte = library.functions.hashPair(
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol],
        ).call()
        balance = core.functions.wallets(nftId, pairByte).call()
        return (txHash, balance / 10 ** collateralDecimal)

    def getCollateralBalance(self, collateralTokenSymbol, underlyingTokenSymbol, nftId):
        validatePair(collateralTokenSymbol, underlyingTokenSymbol)
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        core = self.__getCore()
        library = self.__getLibrary()
        pairByte = library.functions.hashPair(
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol],
        ).call()
        balance = core.functions.wallets(nftId, pairByte).call()
        return balance / 10 ** collateralDecimal

    # getPositionInfo
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - collateral: TokenSymbols
    #     - underlying: TokenSymbols
    # - **Output**
    #     - id: BigNumberish
    #     - entryPrice: BigNumberish
    #     - contractSize: BigNumberish
    #     - borrowAmount: BigNumberish
    #     - collateralUsed: BigNumberish (collateral swapped)
    #     - interestOwed: BigNumberish
    #     - interestOwedPerDay: BigNumberish
    #     - lastSettleTimstamp: BigNumberish
    def getPositionInfo(self, nftId, collateralTokenSymbol, underlyingTokenSymbol):
        return self.__getPositionInfo(nftId, collateralTokenSymbol, underlyingTokenSymbol)

    #  getAllActivePosition
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - pairs: Array of object {collateral: TokenSymbols, underlying: TokenSymbols}
    # - **Output**
    #     - **Array** of Positions
    #         - id: BigNumberish
    #         - entryPrice: BigNumberish
    #         - contractSize: BigNumberish
    #         - borrowAmount: BigNumberish
    #         - collateralUsed: BigNumberish (collateral swapped)
    #         - interestOwed: BigNumberish
    #         - interestOwedPerDay: BigNumberish
    #         - lastSettleTimestamp: BigNumberish
    def getAllActivePosition(self, nftId, pairs):
        activePositions = []
        for pair in pairs:
            collateralTokenSymbol = pair["collateral"]
            underlyingTokenSymbol = pair["underlying"]
            validatePair(collateralTokenSymbol, underlyingTokenSymbol)
            position = self.__getPositionInfo(
                nftId, collateralTokenSymbol, underlyingTokenSymbol)
            if position["id"] != 0:
                activePositions.append(position)
        return activePositions

    # getPositionStateInfo
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - posId: BigNumberish
    # - **Output**
    #     - active: boolean
    #     - isLong: boolean
    #     - PNL: BigNumberish
    #     - averateEntryProce: BigNumberish
    #     - startTimstamp: BigNumberish
    #     - interestPaid: BigNumberish
    #     - totalSwapFeePaid: BigNumberish
    #     - totalTradingFeePaid: BigNumberish
    def getPositionStateInfo(self, nftId, posId):
        return self.__getPositionStateInfo(nftId, posId)

    # getCurrentMargin
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - collateral: TokenSymbols
    #     - underlying: TokenSymbols
    # - **Output**
    #     - PNL: BigNumberish (optional, can be separated to another function)
    #     - margin: BigNumberish
    def getCurrentMargin(self, nftId, collateralTokenSymbol, underlyingTokenSymbol):
        helperFutureTrade = self.__getHelperFutureTrade()
        library = self.__getLibrary()
        pairByte = library.functions.hashPair(
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol]
        ).call()

        return helperFutureTrade.functions.getPositionMargin(nftId, pairByte).call() / 10 ** 18

    # getAvailableCollateral
    # - **Instance**: APHCore
    # - **Parameters**
    #     - nftId: BigNumberish
    #     - collateral: TokenSymbols
    #     - underlying: TokenSymbols
    # - **Output**
    #     - freeBalance: BigNumberish
    #     - usedBalance: BigNumberish
    #     - totalBalance: BigNumberish
    def getAvailableCollateral(self, nftId, collateralTokenSymbol, underlyingTokenSymbol):
        helperFutureTrade = self.__getHelperFutureTrade()
        library = self.__getLibrary()
        pairByte = library.functions.hashPair(
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol],
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol]
        ).call()
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        balanceDetail = helperFutureTrade.functions.getBalanceDetails(
            nftId, pairByte).call()
        return {
            FwxWeb3.FREE_BALANCE: balanceDetail[0] / 10 ** collateralDecimal,
            FwxWeb3.USED_BALANCE: balanceDetail[1] / 10 ** collateralDecimal,
            FwxWeb3.TOTAL_BALANCE: balanceDetail[2] / 10 ** collateralDecimal,
        }

    def __getPositionInfo(self, nftId, collateralTokenSymbol, underlyingTokenSymbol):
        collateralDecimal = self.__getTokenDecimal(collateralTokenSymbol)
        underlyingDecimal = self.__getTokenDecimal(underlyingTokenSymbol)
        positionOutput = self.__getPosition(
            nftId, collateralTokenSymbol, underlyingTokenSymbol)
        positionState = self.__getPositionStateInfo(
            nftId, positionOutput[FwxWeb3.ID])
        if positionOutput[FwxWeb3.ID] == 0:
            return {
                FwxWeb3.ID: 0,
                FwxWeb3.ENTRY_PRICE: 0,
                FwxWeb3.CONTRACT_SIZE: 0,
                FwxWeb3.BORROW_AMOUNT: 0,
                FwxWeb3.COLLATERAL_USED: 0,
                FwxWeb3.INTEREST_OWED: 0,
                FwxWeb3.INTEREST_OWED_PER_DAY: 0,
                FwxWeb3.LAST_SETTLE_TIMESTAMP: 0,
            }
        borrowingDecimal = collateralDecimal if positionState[
            FwxWeb3.ISLONG] else underlyingDecimal
        position = {
            FwxWeb3.ID: positionOutput[FwxWeb3.ID],
            FwxWeb3.ENTRY_PRICE: positionOutput[FwxWeb3.ENTRY_PRICE] / 10**collateralDecimal,
            FwxWeb3.CONTRACT_SIZE: positionOutput[FwxWeb3.CONTRACT_SIZE] / 10**borrowingDecimal,
            FwxWeb3.BORROW_AMOUNT: positionOutput[FwxWeb3.BORROW_AMOUNT] / 10**borrowingDecimal,
            FwxWeb3.COLLATERAL_USED: positionOutput[FwxWeb3.COLLATERAL_SWAPPED_AMOUNT] / 10**collateralDecimal,
            FwxWeb3.INTEREST_OWED: positionOutput[FwxWeb3.INTEREST_OWED] / 10**borrowingDecimal,
            FwxWeb3.INTEREST_OWED_PER_DAY: positionOutput[FwxWeb3.INTEREST_OWE_PER_DAY] / 10**borrowingDecimal,
            FwxWeb3.LAST_SETTLE_TIMESTAMP: positionOutput[FwxWeb3.LAST_SETTLE_TIMESTAMP],
        }
        return position

    def __getPositionStateInfo(self, nftId, posId):
        positionStateOutput = self.__getPositionState(nftId, posId)
        pair = self.__getPair(
            positionStateOutput[FwxWeb3.PAIR_BYTE])
        if int.from_bytes(positionStateOutput[FwxWeb3.PAIR_BYTE], 'big') == 0:
            return {
                FwxWeb3.ACTIVE: False,
                FwxWeb3.ISLONG: False,
                FwxWeb3.PNL: 0,
                FwxWeb3.AVERAGE_ENTRY_PRICE: 0,
                FwxWeb3.START_TIMESTAMP: 0,
                FwxWeb3.INTEREST_PAID: 0,
                FwxWeb3.TOTAL_SWAP_FEE_PAID: 0,
                FwxWeb3.TOTAL_TRADING_FEE_PAID: 0,
            }

        collateralDecimal = self.__getTokenDecimalFromAddress(
            pair[FwxWeb3.COLLATERAL_ADDRESS])
        underlyingDecimal = self.__getTokenDecimalFromAddress(
            pair[FwxWeb3.UNDERLYING_ADDRESS])
        borrowingDecimal = collateralDecimal if positionStateOutput[
            FwxWeb3.ISLONG] else underlyingDecimal
        positionState = {
            FwxWeb3.ACTIVE: positionStateOutput[FwxWeb3.ACTIVE],
            FwxWeb3.ISLONG: positionStateOutput[FwxWeb3.ISLONG],
            FwxWeb3.PNL: positionStateOutput[FwxWeb3.PNL] / 10**18,
            FwxWeb3.AVERAGE_ENTRY_PRICE: positionStateOutput[FwxWeb3.AVERAGE_ENTRY_PRICE] / 10**collateralDecimal,
            FwxWeb3.START_TIMESTAMP: positionStateOutput[FwxWeb3.START_TIMESTAMP],
            FwxWeb3.INTEREST_PAID: positionStateOutput[FwxWeb3.INTEREST_PAID] / 10**borrowingDecimal,
            FwxWeb3.TOTAL_SWAP_FEE_PAID: positionStateOutput[FwxWeb3.TOTAL_SWAP_FEE] / 10**borrowingDecimal,
            FwxWeb3.TOTAL_TRADING_FEE_PAID: positionStateOutput[FwxWeb3.TOTAL_TRADING_FEE] / 10**collateralDecimal,
        }
        return positionState

    def __getPosition(self, nftId, collateralTokenSymbol, underlyingTokenSymbol):
        return self.__getPositionFromAddress(nftId, defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][collateralTokenSymbol], defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][underlyingTokenSymbol])

    def __getPositionFromAddress(self, nftId, collateralTokenAddress, underlyingTokenAddress):
        core = self.__getCore()
        library = self.__getLibrary()
        pairByte = library.functions.hashPair(
            collateralTokenAddress,
            underlyingTokenAddress,
        ).call()
        position = core.functions.positions(nftId, pairByte).call()

        abi = next(filter(lambda abis: FwxWeb3.filterFunctionABI(
            abis, FwxWeb3.POSITIONS), core.abi))
        return FwxWeb3.tupleOutputDecode(position, abi)[FwxWeb3.POSITIONS]

    def __getPositionState(self, nftId, posId):
        core = self.__getCore()
        positionState = core.functions.positionStates(nftId, posId).call()
        abi = next(filter(lambda abis: FwxWeb3.filterFunctionABI(
            abis, FwxWeb3.POSITION_STATES), core.abi))
        return FwxWeb3.tupleOutputDecode(positionState, abi)[FwxWeb3.POSITION_STATES]

    def __getPair(self, pairByte):
        core = self.__getCore()
        pair = core.functions.pairs(pairByte).call()
        return {FwxWeb3.COLLATERAL_ADDRESS: pair[0], FwxWeb3.UNDERLYING_ADDRESS: pair[1]}

    def approve(self, tokenSymbol, spenderSymbol, amount, gas=1300000, gasPrice=25, nonce=0):
        spenderAddress = ""
        if spenderSymbol == "CORE":
            spenderAddress = defi_sdk_py.ADDRESSES["AVAX"][spenderSymbol]
        else:
            validateToken(spenderSymbol)
            spenderAddress = defi_sdk_py.ADDRESSES["AVAX"]["POOL"][spenderSymbol]

        token = self.__getToken(tokenSymbol)
        tokenDecimal = self.__getTokenDecimal(tokenSymbol)
        amount = amount * 10**tokenDecimal

        tx = token.functions.approve(spenderAddress, amount).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
            }
        )

        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(txHash)
        return True

    def getProtocolAllowance(self, tokenSymbol, spenderSymbol, amount):
        spenderAddress = ""
        if spenderSymbol == "CORE":
            spenderAddress = defi_sdk_py.ADDRESSES["AVAX"][spenderSymbol]
        else:
            validateToken(spenderSymbol)
            spenderAddress = defi_sdk_py.ADDRESSES["AVAX"]["POOL"][spenderSymbol]
        token = self.__getToken(tokenSymbol)
        tokenDecimal = self.__getTokenDecimal(tokenSymbol)
        return token.functions.allowance(self.signer.address, spenderAddress).call() / 10**tokenDecimal

    def approveToken(self, spenderAddress, tokenSymbol, gas=1300000, gasPrice=25, nonce=0):
        token = self.__getToken(tokenSymbol)

        amount = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        tx = token.functions.approve(spenderAddress, amount).buildTransaction(
            {
                'from': self.signer.address,
                'nonce': nonce if nonce else self.w3.eth.get_transaction_count(self.signer.address),
                'gas': gas,
                'gasPrice': self.w3.toWei(gasPrice, 'gwei'),
            }
        )

        # Sign tx
        signedTx = self.w3.eth.account.sign_transaction(tx, self.signer.key)

        # Send tx
        txHash = self.w3.eth.send_raw_transaction(signedTx.rawTransaction)
        txReceipt = self.w3.eth.wait_for_transaction_receipt(txHash)

        result = 0
        for log in txReceipt["logs"]:
            if log["topics"][0].hex() == "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925":
                result = int(log["data"][2:], 16)

        return (txHash, result)

    def getTokenDecimal(self, tokenSymbol):
        return self.__getTokenDecimal(tokenSymbol)

    def __getTokenDecimal(self, tokenSymbol):
        token = self.__getTokenFromAddress(
            defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][tokenSymbol])
        decimal = token.functions.decimals().call()
        return decimal

    def __getTokenDecimalFromAddress(self, tokenAddress):
        token = self.__getTokenFromAddress(tokenAddress)
        decimal = token.functions.decimals().call()
        return decimal

    def __getCore(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["CORE"], abi=defi_sdk_py.IAPHCORE_ABI)

    def __getPool(self, poolTokenSymbol):
        return self.__getPoolFromAddress(defi_sdk_py.ADDRESSES["AVAX"]["POOL"][poolTokenSymbol])

    def __getPoolFromAddress(self, poolAddress):
        return self.w3.eth.contract(address=poolAddress, abi=defi_sdk_py.IAPHPOOL_ABI)

    def getMembership(self):
        return self.__getMembership()

    def __getMembership(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["MEMBERSHIP"], abi=defi_sdk_py.IMEMBERSHIP_ABI)

    def __getHelperCore(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["HELPER_CORE"], abi=defi_sdk_py.IHELPERCORE_ABI)

    def __getHelperPool(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["HELPER_POOL"], abi=defi_sdk_py.IHELPERPOOL_ABI)

    def __getHelperMembershipAndStakePool(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["HELPER_MEMBERSHIP_AND_STAKEPOOL"], abi=defi_sdk_py.IHELPERMEMBERSHIPANDSTAKEPOOL_ABI)

    def __getHelperFutureTrade(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["HELPER_FUTURETRADE"], abi=defi_sdk_py.IHELPERFUTURETRADE_ABI)

    def __getLibrary(self):
        return self.w3.eth.contract(address=defi_sdk_py.ADDRESSES["AVAX"]["APH_LIBRARY"], abi=defi_sdk_py.IAPHLIBRARY_ABI)

    def getToken(self, tokenSymbol):
        return self.__getToken(tokenSymbol)

    def __getToken(self, tokenSymbol):
        return self.__getTokenFromAddress(defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][tokenSymbol])

    def getTokenFromAddress(self, tokenAddress):
        return self.__getTokenFromAddress(tokenAddress)

    def __getTokenFromAddress(self, tokenAddress):
        return self.w3.eth.contract(address=tokenAddress, abi=defi_sdk_py.IERC20_ABI)

    def __isTokenSymbolNative(self, tokenSymbol):
        return True if tokenSymbol in ["WAVAX"] else False

    def __isTokenAddressNative(self, tokenAddress):
        return tokenAddress in [defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"][symbol] for symbol in ["WAVAX"]]

    def getW3(self):
        return self.w3

    def getSigner(self):
        return self.signer

    @staticmethod
    def tupleOutputDecode(value, abi):
        """Decode tuple as dict."""
        abiOutputs = {}
        if "outputs" in abi:
            output = {}
            for index, abiOutputs in enumerate(abi.get("outputs", abi)):
                # complex value
                inner = {}
                if 'components' in abiOutputs:
                    for x, y in zip(value if type(value[index]) != list and type(value[index]) != tuple else value[index], abiOutputs["components"]):
                        inner.update(FwxWeb3.tupleOutputDecode(x, y))
                    if abiOutputs["name"] == "":
                        output.update(inner)
                    else:
                        output.update({abiOutputs["name"]: inner})
                else:
                    output.update({abiOutputs["name"]: value[index]})
            result = {abi["name"]: output}
            return result

        # basic value
        return {abi["name"]: value}

    @staticmethod
    def filterFunctionABI(abi, functionName):
        if abi["name"] == functionName:
            return True
        return False


def getClient(url):
    return FwxWeb3(url)


def validateToken(token):
    assert token in defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"], "token not allowed"


def validatePair(collateral, underlying):
    assert collateral != underlying, "same collateral and underlying token"
    assert collateral in defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"], "collateral not allowed"
    assert underlying in defi_sdk_py.ADDRESSES["AVAX"]["TOKEN"], "underlying not allowed"
