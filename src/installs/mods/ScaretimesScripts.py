import time
from WawMods import WawMods

class ScaretimesScripts(WawMods):

	def install(self):
		print 'modname = ' + self.modname
		print 'homepage = ' + self.homepage
		print 'mod_homepage = ' + self.mod_homepage
		print 'WARNING: IT IS NOT OUR FAULT IF YOU DO NOT BACK UP YOUR ROOT'
		raw_input("Press Enter to Continue: ")
		print 'Copying Files to Root'
		time.sleep(3)
		print 'Copying Scripts'
		time.sleep(3)
		print 'Copying Prefabs'
		time.sleep(2)
		print 'Scaretimes Scripts Successfuly Installed'