import time
from WawMods import WawMods

class BlackopsPerks(WawMods):

	def install(self):
		print 'modname = ' + self.modname
		print 'homepage = ' + self.homepage
		print 'map_homepage = ' + self.mod_homepage
		print 'WARNING: IT IS NOT OUR FAULT IF YOU DO NOT BACKUP YOUR ROOT!'
		raw_input("Press Enter to Continue: ")
		time.sleep(2)
		print 'Copying Files'
		time.sleep(2)
		print 'Copying Prefabs'
		time.sleep(2)
		print 'Black Ops Perks Successfuly Installed'