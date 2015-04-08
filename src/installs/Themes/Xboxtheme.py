import time
from .BaseTheme import BaseTheme

class Xboxtheme(BaseTheme):

	def install(self):
		print('theme_name = ' + self.theme_name)
		print('Getting Background Colors: Light Grey')
		time.sleep(2)
		print('Creating Color Scheme')
		time.sleep(2)
		print('Creating Font')
		time.sleep(2)
		print('Xbox 360 Theme now installed. Use "wawmanager -theme xbox_theme", to enable')

	def set_theme(self):
		print('color_scheme = ' + self.color_scheme)
		print('background = ' + self.background)
		print('font = ' + self.font)
		print('theme_name = ' + self.theme_name)
		time.sleep(2)
		print('Theme set to Xbox 360 Theme. Please Restart for the theme to Apply')