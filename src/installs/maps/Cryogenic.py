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

	def description(self):
		print 'mapname = ' + self.mapname
		print 'homepage = ' + self.homepage
		print 'map_homepage = ' + self.map_homepage
		print '- 9 Perks'
		print '- Custom Voice Overs'
		print '- Mob of the Dead Cutom Zombies'
		print '- Halo Weapons'
		print '- Nuketown 2025 Player Models'
		print '- Snowing Blood'
		print '- Buyable Ending'
		print '- Buyable Max Ammo and Double Points'
		print '- Double Tap 2.0'
		print '- Zombie Counter'
		print '- Verrukt Sprinters'
		print '- Five Style Teleporters'
		print '- Laser Trap'
		print '- Ride-able Centrifuge'
		print '- Fan Blade List'
		print ''
		print 'Weapons List:'
		print 'Thundergun'
		print 'Scavanger'
		print 'Blundergat'
		print 'Acidgat'
		print 'Commando'
		print 'FAL'
		print 'Galil'
		print 'Honeybadger'
		print 'AE4'
		print 'Ray Gun'
		print 'PPSH'
		print 'M2 Flamethrower'
		print 'Wudnerwaffe'
		print 'Halo Energy Sword'
		print 'Halo Battle Rifle'
		print 'Halo DMR'
		print 'Halo Magnum'