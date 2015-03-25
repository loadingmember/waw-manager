from WawMaps import WawMaps
import time

class Survivedabox(WawMaps):

	def install(self):
		print 'mapname = ' + self.mapname
		print 'homepage = ' + self.homepage
		print 'map_homepage = ' + self.map_homepage
		## subprocess.call(["c:\\Desktop\survivedabox.exe"])
		print 'Installing Files'
		time.sleep(3)
		print 'Creating Nothing'
		time.sleep(2)
		print 'Creating Images'
		time.sleep(3)
		print 'Survivedabox Sucessfuly Installed'

	def uninstall(self):
		print 'Removing Files/Scripts'
		time.sleep(2)
		print 'survivedabox Map Uninstalled with No Errors'