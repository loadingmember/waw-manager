from .BaseTheme import BaseTheme
import time

class Default(BaseTheme):

	def set_theme(self):
		print('color_scheme = ' + self.color_scheme)
		print('background = ' + self.background)
		print('font = ' + self.font)
		print('theme_name = ' + self.theme_name)
		time.sleep(2)
		print('Theme set as Default. Please Restart WaW Mod Manager, and give it time to update')
