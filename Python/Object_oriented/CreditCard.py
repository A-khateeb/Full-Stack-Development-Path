class CreditCard:
    def __init__(self, customer, bank, account, limit, status):
        self._customer = customer
        self._bank= bank
        self._account= account
        self._limit= limit
        self._status= status
        self._balance = 0
    def get_customer(self):
        return self._customer
    def get_account(self):
        return self._account
    def get_bank(self):
        return self._bank
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    def get_status(self):
        return self._status
    def charge(self, price):
        if price+ self._balance > self._limit:
            return False
        else:
            self._balance+=price
            return True

    def make_payment(self, amount):
        self._balance=amount

cc= CreditCard('Afeef', '1st bank', '12345678910', 1000, "status")


if __name__ == '__main__':
    wallet = []
    print("What is your password")
    print("Keep it Secret")
    passwd = input()
    wallet.append(CreditCard('John Adams','Arab_Bank','123456789',200,"Open" ))
    wallet.append(CreditCard('Afeef Khateeb','Quds_bank','7894561230',200000 ,"Closed" ))
    wallet.append(CreditCard('Moh Ahamd','TNB','45612358',7800,"Closed"))
    wallet.append(CreditCard('Ahmad Ahmad','Palestine_Bank','456123789',200 ,"Open"))
    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(val*2)
        wallet[2].charge(val*3)
        for c in range(3):
            print("Customer:", wallet[c].get_customer())
            print("Bank:", wallet[c].get_bank())
            print("Account Number:", wallet[c].get_account())
            print("Account Limit:" , wallet[c].get_limit())
            print("Account Balance:" , wallet[c].get_balance())
            print("Account Status:" , wallet[c].get_status())
            while wallet[c].get_balance() > 100:
                wallet[c].make_payment(100)
                print("New Balance", wallet[c].get_balance())
                print()
