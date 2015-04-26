import time
from .WawMaps import WawMaps
from slack.Slack import Slack

class zombie_minecraft(WawMaps):

	def install(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('Installing Files')
		## subproccess.call([C://Desktop/nazi_zombie_minecraft.exe])
		time.sleep(2)
		print('Creating Custom Zombie Models')
		time.sleep(2)
		print('Creating Custom Textures')
		time.sleep(2)
		print('Creating Custom Weapons')
		time.sleep(2)
		print('Zombie Minecraft Successfuly Installed')

	def uninstall(self):
		print('mapname = ' + self.mapname)
		print('Removing Files')
		time.sleep(2)
		print('Removing Custom Zombie Models')
		time.sleep(2)
		print('Removing Custom Textures')
		time.sleep(2)
		print('Removing Custom Weapons')
		time.sleep(2)
		print('Zombie Minecraft Uninstalled with No Errors')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Minecraft Textures')
		print('- Custom Weapons')
		print('- Custom Zombie Models')
		print('- George Boss')