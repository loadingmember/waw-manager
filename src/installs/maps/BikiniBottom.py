import time
from .WawMaps import WawMaps

class BikiniBottom(WawMaps):

	def install(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		# subprocess.call([C:\\Desktop\bikini_bottom.exe])
		time.sleep(3)
		print('Installing Files/Scripts')
		time.sleep(2)
		print('Creating Images')
		time.sleep(2)
		print('Bikini Bottom Zombies Installed Successfuly')

	def uninstall(self):
		print('Removing Files/Scripts')
		time.sleep(2)
		print('Removing Mods Folder')
		time.sleep(2)
		print('Removing from Root')
		time.sleep(3)
		print('Bikini Bottom Uninstalled with No Errors')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Rediculous Arms')
		print('- Custom Weapons')
		print('- Bikini Bottom Coins as Points')
		print('- Lot of Perks')