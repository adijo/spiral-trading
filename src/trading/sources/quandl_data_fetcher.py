from __future__ import absolute_import

from datetime import datetime, timedelta
import os
import quandl
from trading.constants.app_constants import QUANDL_API_KEY

quandl.ApiConfig.api_key = os.environ[QUANDL_API_KEY]

DATA_FOLDER = "data"
QUANDL_RESPONSE_CLOSE = "Close"

class QuandlDataFetcher(object):

    def get(self, filename, exchange, days_back):
        """Main entry point of the QuandlDataFetcher for now.
        Gets the 'Close' price for the last 'days_back' days 
        for all the stocks in the given filename

        Args:
            filename (string): The name of the file to be 
                               processed.
            days_back (int): The number of days before the
                             current date for which we want data.

        Returns:
            Dictionary of (string -> Pandas Series)

        """
        folder = os.path.dirname(os.path.realpath(__file__)) + "/" + DATA_FOLDER
        file_path = os.path.join(folder, filename)
        f = open(file_path, "r")
        response = {}
        for line in f:
            symbol = exchange + "/" + line.strip().upper()
            print "Processing", symbol, "from Quandl."
            try:
                quandl_response = quandl.get(symbol, 
                start_date = self.calculate_data(days_back))
                response[line.strip()] = quandl_response[QUANDL_RESPONSE_CLOSE]
            except:
                print "Failed to get", symbol, "from Quandl."
                pass
        return response

    def calculate_data(self, days_back):
        date_n_days_ago = datetime.now() - timedelta(days = days_back)
        date_format = "%s-%s-%s" % (date_n_days_ago.year, 
            date_n_days_ago.month, date_n_days_ago.day)
        return date_format









