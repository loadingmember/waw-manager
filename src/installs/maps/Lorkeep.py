import time 
from .WawMaps import WawMaps
from slack.Slack import Slack

class Lorkeep(WawMaps):

	def install(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_ho')