import time 
from .WawMaps import WawMaps
from slack.Slack import Slack

class Lorkeep(WawMaps):

	def install(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('Installing Files...')
		## subproccess.call([C://Dekstop/nazi_zombie_lorkeep.exe])
		time.sleep(2)
		print('Creating Box...')
		time.sleep(2)
		print('Downloading Custom Models')
		time.slep(2)
		print('Lorkeep Successfuly Installedd')

	def uninstall(self):
		print 