from __future__ import absolute_import

from kiteconnect import KiteConnect
import os
from trading.constants.app_constants import KITE_API_KEY, \
                            KITE_SECRET_KEY, KITE_REQUEST_TOKEN
from trading.sources.utils.kite_utils import get_redirected_url

KITE_API_KEY_VAL = os.environ[KITE_API_KEY]
KITE_SECRET_KEY_VAL = os.environ[KITE_SECRET_KEY]

LAST_PRICE = "last_price"
ACCESS_TOKEN = "access_token"
RETRIES = 5
EQUITY = "equity"

class KiteData(object):
    def __init__(self):
        self.kite = KiteConnect(api_key = KITE_API_KEY_VAL)

        kite_request_token = get_redirected_url(self.kite.login_url())
        data = self.kite.request_access_token(kite_request_token, 
            secret = KITE_SECRET_KEY_VAL)
        
        self.kite.set_access_token(data[ACCESS_TOKEN])

    def get_last_price(self, symbol, exchange):
        return self.kite.quote(exchange, symbol)[LAST_PRICE]

    def get_account_information(self, param, retries = RETRIES):
        for i in xrange(retries):
            try:
                data = self.account_information_helper()
                return data[param]
            except:
                continue
        return None

        
    def account_information_helper(self):
        data = self.kite.margins(EQUITY)
        return data

    # move this somewhere else
    def execute_plan(self, plan):
        pass

       
