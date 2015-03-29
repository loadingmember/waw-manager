import http.client, urllib.parse

class Slack():

	@staticmethod
	def send_message(slack_channel, message):
		conn = http.client.HTTPSConnection('zalukfamily.slack.com')

		conn.connect()

		conn.request('POST', '/services/hooks/slackbot?' + urllib.parse.urlencode({'token': 'ibQkhDVPikVUZGJVunjcifrs', 'channel': slack_channel}), message)
