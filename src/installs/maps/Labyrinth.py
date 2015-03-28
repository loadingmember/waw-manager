import time
from WawMaps import WawMaps

class Labyrinth(WawMaps):

	def install(self):
		print 'mapname = ' + self.mapname
		print 'homepage = ' + self.homepage
		print 'map_homepage = ' + self.map_homepage
		time.sleep(2)
		print 'Installing Files'
		time.sleep(2)
		print 'Creating Images'
		time.sleep(2)
		print 'Creating Box'
		time.sleep(2)
		print 'Labyrinth 1.2 Now Installed Successfuly'

	def uninstall(self):
		print 'mapname = ' + self.mapname
		print 'Removing Files/Scripts'
		time.sleep(2)
		print ''