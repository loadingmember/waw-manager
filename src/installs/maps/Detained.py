import time
from WawMaps import WawMaps

class Detained(WawMaps):

	def install(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		## subprocess.call([C:\\Desktop\detained.exe])
		time.sleep(2)
		print('Installing Files')
		time.sleep(2)
		print('Creating Images')
		time.sleep(2)
		print('Detained Successfuly Installed')

	def uninstall(self):
		print('mapname = ' + self.mapname)
		time.sleep(2)
		print('Removing Files/Scripts')
		time.sleep(2)
		print('Removing Images')
		time.sleep(2)
		print('Removing from Root')
		times.sleep(2)
		print(mapname + 'Removed with No Errors')

	def descritpion(self):
		