import time
from .WawMaps import WawMaps
from slack.Slack import Slack

class Zombiebridge(WawMaps):

	def install(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('Installing Files/Scripts')
		time.sleep(2)
		print('Creating Prefabs')
		time.sleep(2)
		print('Creating Black Ops Perfabs and Scripts and Weapons')
		time.sleep(2)
		print('Bridge v1.6 Successfuly Installed')
		Slack.send_message('#coding', 'Map Installed: Bridge v1.6')

	def uninstall(self):
		print('mapname = ' + self.mapname)
		print('Removing Files/Scripts')
		time.sleep(2)
		print('Removing Prefabs')
		time.sleep(2)
		print('Removing Black Ops Prefabs and Scripts and Weapons')
		time.sleep(2)
		print('Bridge v1.6 Uninstalled with No Errors')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Black Ops Quick Revive')
		print('- Black Ops Weapons and M1911')
		print('- Double Tap 2.0')