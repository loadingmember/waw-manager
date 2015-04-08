import time
from .WawMods import WawMods

class WawModtools(WawMods):

	def install(self):
		print('modname = ' + self.modname)
		print('homepage = ' + self.homepage)
		print('mod_homepage = ' + self.mod_homepage)
		time.sleep(3)
		print('Copying Files')
		time.sleep(1)
		print('WARNING: IT IS NOT OUR FAULT IF YOU DO NOT BACKUP YOUR ROOT!')
		input("Press Enter to Continue: ")
		print('Installing Lanuncher. Completed')
		time.sleep(2)
		print('Installing Script Placer. Completed')
		time.sleep(2)
		print('Installing WeaponsEditor++. Completed')
		time.sleep(2)
		print('Installing Map Manager. Completed')
		time.sleep(2)
		print('WaW Modtools Now Installed')

	def description(self):
		print('modname = ' + self.modname)
		print('homepage = ' + self.homepage)
		print('mod_homepage = ' + self.mod_homepage)
		print('WaW Mod Tools is a must have for mod developing.')
		print('It adds a whole ton of classes and prefabs')
		print('and installs Launcher.')
		print('If you download it from now it also adds Script Manager')
		print('and Map Manager')