import time
from .WawMaps import WawMaps
from slack.Slack import Slack

class Domesnow(WawMaps):

	def install(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('Installing Files/Scripts')
		## subproccess.call([C:\\Desktop\dome_snow.exe])
		time.sleep(2)
		print('Creating Prefabs')
		time.sleep(2)
		print('Creating Snow')
		time.sleep(2)
		print('Creating Ported Weapons')
		time.sleep(2)
		print('Dome Snow Successfuly Installed')

	def uninstall(self):
		print('mapname = ' + self.mapname)
		print('Removing Files/Scripts')
		time.sleep(2)
		print('Removing Prefabs')
		time.sleep(2)
		print('Removing Snow')
		time.sleep(2)
		print('Removing Ported Weapons')
		time.sleep(2)
		print('Dome Snow Uninstalled with No Errors')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Exact Copy of Modern Warefare 3 Dome')
		print('- Modern Warfare 3 Ported Weapons')
		print('- Black Ops 2 Ported Weapons')
		print('- All Perks')
		print('- Double Tap 2.0')
		print('- Snow')
		print('- Great Wall Weapons and Training Area')