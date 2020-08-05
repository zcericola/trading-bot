from consumer import consumer
import json
import os


class Stocks:
    def __init__(self):
        params = {'status': 'active'}
        self.active_stocks = consumer.get(False, 'v2/assets', params)
        self.save_tradable_stocks()

    def save_tradable_stocks(self):
        stocksFile = 'tradable_stocks.json'
        # checks that the file is empty
        if (os.stat(stocksFile).st_size == 0):
            # Writes the tradable_stocks data to a JSON file
            file = open(stocksFile, 'w')
            with file as f:
                json.dump(self.active_stocks, f)
            file.close()

    def get_tradable_stocks(self):
        print(f'active_stocks: {self.active_stocks}')

    def get_info_by_symbol(self, tickerSymbol):
        response = consumer.get(False, 'v2/assets', tickerSymbol)
        return response


stocks = Stocks()
stocks.get_info_by_symbol('TSLA')
