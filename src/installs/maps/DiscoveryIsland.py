import time
from .WawMaps import WawMaps
from slack.Slack import Slack

class DiscoveryIsland(WawMaps):

	def install(self, output=None):
		if output == None:
			print('mapname = ' + self.mapname)
			print('homepage = ' + self.homepage)
			print('map_homepage = ' + self.map_homepage)
			print('Installing Scripts')
			time.sleep(2)
			print('Creating Water')
			time.sleep(2)
			print('Installing Custom Weapons and Custom Zombie Theme')
			time.sleep(3)
			print('Discovery Island Successfuly Installed')
			Slack.send_message('#coding', 'Map Installed: Discovery Island')
		else:
			output.delete(1.0, END)
			output.insert(INSERT, 'mapname = ' + self.mapname + '\n')
			output.update_idletasks()
			output.insert(END, 'homepage = ' + self.homepage + '\n')
			output.update_idletasks()
			output.insert(END, 'map_homepage = ' + self.map_homepage + '\n')
			output.update_idletasks()
			# subprocess.call([C:\\Desktop\bikini_bottom.exe])
			time.sleep(2)
			output.insert(END, 'Installing Scritps\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Installing Custom Weapons and Custom Zombie Theme\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Creating Custom Weapons and Zombie Models\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Dead Ship Successfuly Installed')
			output.update_idletasks()
			Slack.send_message('#coding', 'Map Installed through UI: Discovery Island')
	
	def uninstall(self):
		print('mapname = ' + self.mapname)
		print('Removing Scritps')
		time.sleep(2)
		print('Removing Custom Weapons and Custom Zombie Themes')
		time.sleep(2)
		print('Dead Ship Uninstall with No Error')

	def reset(self):
		print('mapname = ' + self.mapname)
		time.sleep(2)
		print('Reversing Files and Non Fun')
		time.sleep(2)
		print('Discovery Island Reset Complete')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Custom Weapons')
		print('- Custom Theme')
		print('- Custom Zombie Models')
		print('- Custom Perks')
		print('- DayZ Type Packages')