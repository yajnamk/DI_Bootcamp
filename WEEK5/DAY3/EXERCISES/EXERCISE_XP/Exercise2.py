class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __call__(self):
        print('currency:{}, amount: {}'.format(self.currency, self.amount))

c1 = Currency('dollar', 5)

print(c1)