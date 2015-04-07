from .BaseTheme import BaseTheme
import time

class Cheesecubetheme(BaseTheme):

	def install(self):
		print('theme_name = ' + self.theme_name)
		print('Getting Background Colors')
		time.sleep(2)
		print('Creating Custom Color Scheme')
		time.sleep(2)
		print('Get Font')
		time.sleep(2)
		print('Cheese Cube Theme Successfuly Installed')

	def set_theme(self):
		print('color_scheme = ' + self.color_scheme)
		print('background = ' + self.background)
		print('font = ' + self.font)
		print('theme_name = ' + self.theme_name)
		time.sleep(2)
		print('Theme set to Cheese Cube. Please Restart for the Theme to Apply')