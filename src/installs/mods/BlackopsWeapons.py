import time
from WawMods import WawMods

class BlackopsWeapons(WawMods):

	def install(self):
		print 'modname = ' + self.modname
		print 'homepage = ' + self.homepage
		print 'mod_homepage = ' + self.mod_homepage
		print 'WARNING: IT IS NOT OUR FAULT IF YOU DO NOT BACKUP YOUR DIRECTORY!'
		raw_input("Press Enter to Continue: ")
		time.sleep(3)
		print 'Copying Files to Root Directory'
		time.sleep(2)
		print 'Creating Prefabs'
		time.sleep(3)
		print 'Black Ops Weapons Successfuly Installed'
