import time
from .BaseTheme	import BaseTheme

class Playstationtheme(BaseTheme):

	def install(self):
		print('theme_name = ' + self.theme_name)
		print('Getting Background Colors: Blue\White')
		time.sleep(2)
		print('Creating Color Scheme')
		time.sleep(2)
		print('Creating Playstation Font')
		time.sleep(2)
		print('Playstation Theme Now installed. Use "wawmanager -theme playstation_theme" to enable')

	def set_theme(self):
		print('color_scheme = ' + self.color_scheme)
		print('background = ' + self.background)
		print('font = ' + self.font)
		print('theme_name = ' + self.theme_name)
		time.sleep(2)
		print('Theme set to Playstation Theme. Please Restart for the theme to Apply')