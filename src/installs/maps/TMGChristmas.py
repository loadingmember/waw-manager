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

	def uninstall(self):
		print 'Removing Files'
		time.sleep(2)
		print 'TMG Christmas 1.1 Uninstalled with No Errors'

	def description(self):
		print 'mapname = ' + self.mapname
		print 'homepage = ' + self.homepage
		print 'map_homepage = ' + self.map_homepage
		print '- Soul Chests'
		print '- Snow'
		print '- MW2 Guns'
		print '- Black Ops 2 Weapons'
		print '- All Perks + Custom Perks'
		print '- All Wonder Weapons'