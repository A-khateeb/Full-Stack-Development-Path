class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank= bank
        self._acnt= acnt
        self._limit= limit
        self._balance= 0
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_acnt(self):
        return self._acnt
    def get_balance(self):
        return self.balance

    def charge(self, price):
        if price+ self._balance > self._limit:
            return False
        else:
            self._balance+=price
            return True

    def make_payment(self, amount):
        self._balance=amount

cc= CreditCard('Afeef', '1st bank', '12345678910', 1000)
