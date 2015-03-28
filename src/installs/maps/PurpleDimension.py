import time
from WawMaps import WawMaps

class PurpleDimension(WawMaps):

	def install(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		## subprocess.call(["c:\\Desktop\PurpleDimension.exe"])
		print('Installing Files')
		time.sleep(2)
		print('Creating FX')
		time.sleep(3)
		print('Creating Images')
		time.sleep(2)
		print('Determing Size')
		time.sleep(3)
		print('Purple Dimension Sucsesfuly Installed')

	def uninstall(self):
		print('Removing Files/Scripts')
		time.sleep(2)
		print('Purple Dimension Map Uninstalled with No Errors')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Nuke Town Zombies')
		print('- Origins Mid-Evil Zombies')
		print('- Five Teleporters')
		print('- Kino Teleporter')
		print('- All Black Ops 1 Perks')
		print('- Buildables')
		print('- BUYABLE ENDING')
		print('- Purple Snow')
		print('- Different Players')
		print('- Change of Viewhands')
		print('- Moving Textures')
		print('- BOB')
		print('- Imported Weapons')
		print('- Spinning Stuff')
		print('- Music Box')
		print('- Solo Revive')
		print('- FX')
		print('- All WaW Weapons Removed Except for Ray Guns')
		print('- Fire Sale Powerup')
		print('- Moving Perks')
		print('and More...')