import time
from slack.Slack import Slack
from .WawMaps import WawMaps

class Nuketownwinter(WawMaps):

	def install(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('Installing Files/Scripts')
		time.sleep(2)
		print('Creating Prefabs')
		time.sleep(2)
		print('Creating Snow')
		time.sleep(2)
		print('Nuketown Winter Successfuly Installed')

	def uninstall(self):
		print('mapname = ' + self.mapname)
		print('Removing Scripts and Files')
		time.sleep(2)
		print('Removing Prefabs')
		time.sleep(2)
		print('Removing Snow')
		time.sleep(2)
		print('Nuketown Winter Uninstalled with No Errors')

	def description(self):
			print('mapname = ' + self.mapname)
			print('homepage = ' + self.homepage)
			print('map_homepage = ' + self.map_homepage)
			print('- Winter Snow')
			print('- Nuketown Replica')
			print('- All Perks')