from consumer import consumer


class Account:
    def __init__(self):
        self.account = consumer.get(False, 'v2/account')

    def get_account(self):
        return self.account

    def get_daily_balance_change(self):
        balance_change = float(self.account["equity"]) - \
            float(self.account["last_equity"])

        print(f'Change from yesterday: {balance_change}')

        return balance_change


account = Account()

# account.get_account()
account.get_daily_balance_change()
