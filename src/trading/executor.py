from __future__ import absolute_import

import copy
import sys

from trading.strategies.simple_mean_reversion import SimpleMeanReversion
from trading.constants.strategy_constants import DAYS_BACK, \
                                            STD_THRESHOLD, SINGLE_STOCK_LIMIT
from trading.validator import Validator
from trading.sources.kite_data import KiteData
from trading.publishers.slack import Slack

def main():
    # FIXME: make arguments parsing better
    strategy = SimpleMeanReversion()
    
    # FIXME: this should be loaded
    props = {}
    props[DAYS_BACK] = 10
    props[STD_THRESHOLD] = 1.3
    props[SINGLE_STOCK_LIMIT] = 100

    dry_run = True

    budget = 3000

    filename = "nifty500.txt"
    exhange = "NSE"

    plan = strategy.get_plan(filename, exhange, props)
    print "Plan is", plan
    plan_copy = copy.deepcopy(plan)
    validator = Validator()
    if validator.validate(plan, budget):
        kite_data = KiteData()
        if not dry_run:
            kite_data.execute_plan(plan)
        slack = Slack()
        slack.send_notifications(plan_copy)

main()
