import time
from installs.Themes.BaseTheme import BaseTheme

class Christmaswarehousetheme(BaseTheme):

		def install(self):
			print('theme_name = ' + self.theme_name)
			print('Getting Background Colors: Present')
			time.sleep(2)
			print('Creating Color Scheme')
			time.sleep(2)
			print('Creating Font')
			time.sleep(2)
			print('Christmas Warehouse Theme now installed. Use "wawmanager -theme christmas_warehouse_theme", to enable')

		def set_theme(self):
			print('color_scheme = ' + self.color_scheme)
			print('background = ' + self.background)
			print('font = ' + self.font)
			print('theme_name = ' + self.theme_name)
			time.sleep(2)
			print('Theme set to Christmas Warehouse Theme. Please Restart for the Theme to Apply')