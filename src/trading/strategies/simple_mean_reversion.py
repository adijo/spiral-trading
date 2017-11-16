from __future__ import absolute_import

import math

from trading.sources.quandl_data_fetcher import QuandlDataFetcher
from trading.constants.strategy_constants import DAYS_BACK, \
                                            STD_THRESHOLD, SINGLE_STOCK_LIMIT, \
                                            PRICE, QUANTITY, \
                                            TRADING_SYMBOL
from trading.sources.kite_data import KiteData


class SimpleMeanReversion(object):
    def __init__(self):
        self.data_fetcher = QuandlDataFetcher()
        self.kite_data = KiteData()

    def get_plan(self, filename, exchange, props):
        
        plan = []

        # get the data.
        data = self.data_fetcher.get(filename, exchange, 
            props[DAYS_BACK])

        # TODO: calculate what to sell

        # calculate what to buy.
        # when the current price is lower
        # than the mean by some amount
        for symbol, series in data.iteritems():
            try:
                last_price = self.kite_data.get_last_price(symbol, 
                    exchange)
            except:
                print "Failed to get last price for", symbol, "from Kite."
                continue
            std_dev = series.std()
            mean = series.mean()
            std_threshold = props[STD_THRESHOLD]
            distance_from_mean = last_price - mean
            print symbol, distance_from_mean
            if distance_from_mean < 0:
                # this means that the
                # last price is lesser than
                # the mean.
                z_score = math.fabs(distance_from_mean) / std_dev
                if z_score >= std_threshold:
                    # buy this stock.
                    order_qty = self.calculate_qty(last_price, props)
                    order =  {
                        TRADING_SYMBOL: symbol,
                        "exchange": exchange,
                        "transaction_type": "BUY",
                        QUANTITY: order_qty,
                        "order_type": "MARKET",
                        "product": "NRML",
                        PRICE: last_price
                    }
                    plan.append(order)
        return plan

    def calculate_qty(self, last_price, props):
        single_stock_limit = props[SINGLE_STOCK_LIMIT]
        return int(single_stock_limit / last_price)
