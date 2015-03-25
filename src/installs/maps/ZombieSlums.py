import time
from WawMaps import WawMaps

class ZombieSlums(WawMaps):

	def install(self):
		print 'mapname = ' + self.mapname
		print 'homepage = ' + self.homepage
		print 'map_homepage = ' + self.map_homepage
		## subprocess.call(["c:\\Desktop\nazi_zombie_slums.exe"])
		time.sleep(3)
		print 'Installing Files/Scripts'
		time.sleep(2)
		print 'Creating Images'
		time.sleep(2)
		print 'Setting Weather and Time of Day'
		time.sleep(2)
		print 'Zombie Slums succesfuly Installed'
		