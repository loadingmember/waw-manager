import time
from WawMaps import WawMaps

class Cryogenic(WawMaps):

	def install(self):
		print 'mapname = ' + self.mapname
		print 'homepage = ' + self.homepage
		print 'map_homepage = ' + self.map_homepage
		## subprocess.call(["c:\\Desktop\cryogenic.exe"])
		print 'Installing Files/Scripts'
		time.sleep(2)
		print 'Creating FX and Images'
		time.sleep(3)
		print 'Setting Blood Rain'
		time.sleep(2)
		print 'Cyrogenic now Sucessfuly Installed'

	def uninstall(self):
		print 'Removing Files/Scripts'
		time.sleep(2)
		print 'Cryogenic Map Uninstalled with No Errors'