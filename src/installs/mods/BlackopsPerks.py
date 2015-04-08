import time
from .WawMods import WawMods

class BlackopsPerks(WawMods):

	def install(self):
		print('modname = ' + self.modname)
		print('homepage = ' + self.homepage)
		print('mod_homepage = ' + self.mod_homepage)
		print('WARNING: IT IS NOT OUR FAULT IF YOU DO NOT BACKUP YOUR ROOT!')
		input("Press Enter to Continue: ")
		time.sleep(2)
		print('Copying Files')
		time.sleep(2)
		print('Copying Prefabs')
		time.sleep(2)
		print('Black Ops Perks Successfuly Installed')

	def description(self):
		print('modname = ' + self.modname)
		print('homepage = ' + self.homepage)
		print('mod_homepage = ' + self.mod_homepage)
		print('Black Ops Perks Mod adds lots of new features for developers.')
		print('It adds many scripts for PHD Flopper, Stamin-Up, Mule Kick, and Dead Shot Daquiri')
		print('This also comes with the Prefabs so you do not have to create them yourself')