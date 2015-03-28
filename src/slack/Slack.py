import httplib, urllib

class Slack():

	def send_message(self, slack_channel, message):
		conn = httplib.HTTPSConnection('zalukfamily.slack.com')

		conn.connect()

		print('/services/hooks/slackbot?' + urllib.urlencode({'token': 'ibQkhDVPikVUZGJVunjcifrs', 'channel': slack_channel}))

		conn.request('POST', '/services/hooks/slackbot?' + urllib.urlencode({'token': 'ibQkhDVPikVUZGJVunjcifrs', 'channel': slack_channel}), message)
