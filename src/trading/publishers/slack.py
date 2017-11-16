from __future__ import absolute_import

import requests
import os
import json

from trading.constants.app_constants import SLACK_URL

from trading.constants.strategy_constants import PRICE, QUANTITY, \
												TRADING_SYMBOL

PAYLOAD = "payload"

class Slack(object):
	def send_notifications(self, plan):
		print "HELLO"
		print os.environ[SLACK_URL]
		for p in plan:
			r = requests.post(os.environ[SLACK_URL], data = self.construct_text(p))
			print r

	def construct_text(self, p):
		payload = {}
		string_builder = ["Symbol: %s" % p[TRADING_SYMBOL]]
		string_builder.append("Quantity: %s" % p[QUANTITY])
		string_builder.append("Cost: %s" % p[PRICE])
		string_builder.append("Total cost: %s" % (p[PRICE] * p[QUANTITY]))
		payload["text"] = "\n".join(string_builder)
		print payload
		return json.dumps(payload)