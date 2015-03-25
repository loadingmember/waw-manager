import time
from WawMaps import WawMaps

class TMGChristmas(WawMaps):

	def install(self):
		print 'mapname = ' + self.mapname
		print 'homepage = ' + self.homepage
		print 'map_homepage = ' + self.map_homepage
		## subprocess.call(["c:\\Desktop\TMG_Christmas1.1.exe.exe"])
		print 'Installing Files/Scripts'
		time.sleep(3)
		print 'Creating Images'
		time.sleep(2)
		print 'Setting Weather'
		time.sleep(2)
		print 'Creating FX'
		time.sleep(3)
		print 'TMG Christmas Sucessfuly Installed'
		
