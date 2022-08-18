class Currency:
    def __init__(self, currency, amount):
        self.currency = str(currency)
        self.amount = amount
        print(f"{self.currency} {self.amount}")

    def __str__(self):
        return f'{self.currency} {self.amount}
        
