import time
from WawMaps import WawMaps

class ProjectViking(WawMaps):

	def install(self):
		print 'mapname = ' + self.mapname
		print 'homepage = ' + self.homepage
		print 'map_homepage = ' + self.map_homepage
		## subprocess.call(["c:\\Desktop\ProjectVikingV1.0.2.exe"])
		print 'Installing File/Scripts'
		time.sleep(2)
		print 'Creating Images'
		time.sleep(3)
		print 'Setting Weather/FX'
		time.sleep(2)
		print 'Project Viking Beta 1.0.2 Installed Successfuly'

	def uninstall(self):
		print 'Removing Files/Scripts'
		time.sleep(2)
		print 'Removing from Mods Folder'
		time.sleep(2)
		print 'Removing from Root'
		time.sleep(4)
		print 'Project Viking Beta 1.0.2 Uninstalled with No Errors'