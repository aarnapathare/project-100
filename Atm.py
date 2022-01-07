class atm(object):
    def __init__(self, CashWithdrawl, BalanceEnquiry, money):
        
        self.CashWithdrawl = CashWithdrawl
        self.BalanceEnquiry = BalanceEnquiry

    def CashWithdrawl(self, cash):
        self.CashWithdrawl = cash

    def BalanceEnquiry(self, amount):
        self.BalanceEnquiry = amount

    def amount(self):
        print("Balance:")



