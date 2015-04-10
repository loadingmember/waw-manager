import time
from slack.Slack import Slack
from .WawMaps import WawMaps

class Zombielibrary(WawMaps):

	def install(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' = self.map_homepage)
		print('Installing Files/Scripts')
		## subproccess.call([C:\\Desktop\zombie_library.exe])
		time.sleep(2)
		print('Creating Prefabs')
		time.sleep(2)
		print('Creating Custom Perks')
		time.sleep(2)
		print('Zombie Library Successfuly Installed')
		Slack.send_message('#coding', 'Map Installed: Zombie Library')

	def uninstall(self):
		print('mapname = ' + self.mapname)
		print('Removing Files/Scripts')
		time.sleep(2)
		print('Removing Prefabs')
		time.sleep(2)
		print('Removing Custom Perks')
		time.sleep(2)
		print('Zombie Library Uninstalled with No Errors')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' = self.map_homepage)