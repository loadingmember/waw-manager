import time
from WawMaps import WawMaps

class PurpleDimension(WawMaps):

	def install(self):
		print 'mapname = ' + self.mapname
		print 'homepage = ' + self.homepage
		print 'map_homepage = ' + self.map_homepage
		## subprocess.call(["c:\\Desktop\PurpleDimension.exe"])
		print 'Installing Files'
		time.sleep(2)
		print 'Creating FX'
		time.sleep(3)
		print 'Creating Images'
		time.sleep(2)
		print 'Determing Size'
		time.sleep(3)
		print 'Purple Dimension Sucsesfuly Installed'

	def uninstall(self):
		print 'Removing Files/Scripts'
		time.sleep(2)
		print 'Purple Dimension Map Uninstalled with No Errors'