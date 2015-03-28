import time
import os
import sys
from WawMaps import WawMaps

class Labyrinth(WawMaps):

	def install(self):
		print 'mapname = ' + self.mapname
		print 'homepage = ' + self.homepage
		print 'map_homepage = ' + self.map_homepage
		## subprocess.call([C:\\Desktop\labyrinth.exe])
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
		# os.rmtree(Labyrinth)
		time.sleep(2)
		print 'Removing from Root Directory'
		time.sleep(2)
		print 'Removing Images'
		time.sleep(2)
		print 'Labyrinth 1.2 Uninstalled with No Errors'

	def description(self):
		print 'mapname = ' + self.mapname
		print 'homepage = ' + self.homepage
		print 'map_homepage = ' + self.map_homepage
		print '- Black Ops Perks'
		print '- Black Ops Quick Revive'
		print '- Zombie or Freakbag Counter'
		print '- Custom Perks'
		print '- Custom Guns'
		print '- Nuketown Zombie Models'
		print '- Multiplayer Weapons'
		print '- Buildable Gun and Power'
		print '- Buyable Ending'