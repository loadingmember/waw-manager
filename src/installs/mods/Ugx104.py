import time
from WawMods import WawMods

class Ugx104(WawMods):

	def install(self):
		print('modname = ' + self.modname)
		print('homepage = ' + self.homepage)
		print('mod_homepage = ' + self.mod_homepage)
		print('Copying Files to Root Directory')
		time.sleep(2)
		print('WARNING: IT IS NOT OUR FAULT IF YOU DO NOT BACK UP YOUR ROOT!')
		raw_input("Press Enter to Continue: ")
		time.sleep(3)
		print('UGX Mod Version 1.0.4 Installed')

	def description(self):
		print('modname = ' + self.modname)
		print('homepage = ' + self.homepage)
		print('mod_homepage = ' + self.mod_homepage)
		print('UGX Mod adds so many features for map developers')
		print('It adds over 70+ Weapons, a ranking system, over 6 new game modes')
		print('and other features like the black ops fire sale, and much more')