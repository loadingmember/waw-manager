import http.client, urllib.parse

class Slack():

	def send_message(self, slack_channel, message):
		conn = http.client.HTTPSConnection('zalukfamily.slack.com')

		conn.connect()

		conn.request('POST', '/services/hooks/slackbot?' + urllib.parse.urlencode({'token': 'ibQkhDVPikVUZGJVunjcifrs', 'channel': slack_channel}), message)
