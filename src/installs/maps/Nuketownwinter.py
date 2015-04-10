import time
from slack.Slack import Slack
from .WawMaps import WawMaps

class Nuketownwinter(WawMaps):

	def install(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('Installing Files/Scripts')
		## subproccess.call([C:\\Desktop\nuketown_zombies_winter.exe])
		time.sleep(2)
		print('Creating Prefabs')
		time.sleep(2)
		print('Creating Snow')
		time.sleep(2)
		print('Nuketown Winter Successfuly Installed')
		Slack.send_message('#coding', 'Map Installed: Nuketown Winter Edition')

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