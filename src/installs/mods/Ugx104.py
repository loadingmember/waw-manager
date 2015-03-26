import time
from WawMods import WawMods

class Ugx104(WawMods):

	def install(self):
		print 'modname = ' + self.modname
		print 'homepage = ' + self.homepage
		print 'mod_homepage = ' + self.mod_homepage
		print 'Copying Files to Root Directory'
		time.sleep(2)
		print 'WARNING: IT IS NOT OUR FAULT IF YOU DO NOT BACK UP YOUR ROOT!'
		raw_input("Press Enter to Continue: ")
		time.sleep(3)
		print 'UGX Mod Version 1.0.4 Installed'

		