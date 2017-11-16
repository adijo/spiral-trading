from __future__ import absolute_import

from trading.sources.kite_data import KiteData
from trading.constants.strategy_constants import PRICE, QUANTITY

NET = "net"


class Validator(object):
    def validate(self, plan, budget):
        # get remaining money
        kite_data = KiteData()
        balance = kite_data.get_account_information(NET)
        expenditure = self.plan_expenditure(plan)
        print "total expenditure is", expenditure
        print "total budget is", budget
        print expenditure <= budget
        return expenditure <= budget

    def plan_expenditure(self, plan):
        total_cost = 0
        for p in plan:
            total_cost += (p[PRICE] * p[QUANTITY])
            p.pop(PRICE, None)
        return total_cost




