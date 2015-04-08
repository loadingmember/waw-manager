import time
from .WawMods import WawMods

class CModernweapons(WawMods):

	def install(self):
		print('modname = ' + self.modname)
		print('homepage = ' + self.homepage)
		print('mod_homepage = ' + self.mod_homepage)
		print('WARNING: IT IS NOT OUR FAULT IF YOU DO NOT BACK UP YOUR ROOT:')
		input("Press Enter to Continue: ")
		time.sleep(3)
		print('Copying Files to Root Directory')
		time.sleep(2)
		print('Creating Prefabs')
		time.sleep(2)
		print('Combat Modern Weapons Successfuly Installed')

	def description(self):
		print('modname = ' + self.modname)
		print('homepage = ' + self.homepage)
		print('mod_homepage = ' + self.mod_homepage)
		print('Combat Modern Weapons brings all your favorite')
		print('new weapons to Call of Duty World at War')