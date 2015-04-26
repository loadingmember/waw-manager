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
		print('mapname = ' + self.mapname)
		print('Removing Files...')\
		# subproccess.call([C://Program /Files /x86/steam/steamapps/common/Call /of /Duty/ World/ at/ War/mods/])
		# subproccess.call(rm -rf nazi_zombie_lorkeep)
		print('Removing Box')
		time.sleep(2)
		print('Removing Custom Models')
		time.sleep(2)
		print('Lorkeep Uninstalled with No Errors')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Box Map')
		print('- Custom Weapons')
		print('- Crazy Zombies')
		print('- Origin Staffs')
		print('- Subway Theme')
		print('- Black Ops 2 Ported Weapons and Perks')
		print('- Black Ops 1 Ported Weapons and Perks')