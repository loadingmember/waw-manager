import time
from WawMaps import WawMaps

class OneWindow(WawMaps):

	def install(self):
		print 'mapname = ' + self.mapname
		print 'homepage = ' + self.homepage
		print 'map_homepage = ' + self.map_homepage
		## subprocess.call(["c:\\Desktop\zm_owc.exe"])
		print 'Installing File/Scripts'
		time.sleep(2)
		print 'Creating Box'
		time.sleep(2)
		print 'One Window Challange Installed Succesfully'

	def uninstall(self):
		print 'Removing Files/Scripts'
		time.sleep(2)
		print 'One Window Challange Uninstalled with No Errors'