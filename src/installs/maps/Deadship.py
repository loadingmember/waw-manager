import time
from .WawMaps import WawMaps
from slack.Slack import Slack

class Deadship(WawMaps):

	def install(self, output=None):
		if output == None:
			print('mapname = ' + self.mapname)
			print('homepage = ' + self.homepage)
			print('map_homepage' + self.map_homepage)
			print('Installing Scripts... All of Them')
			time.sleep(2)
			print('Creating Pirate Theme')
			time.sleep(2)
			print('Installing Custom Weapons and Zombie Models')
			time.sleep(2)
			print('Dead Ship Successfuly Installed')
			Slack.send_message('#coding', 'Map Installed: Dead Ship')
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
			output.insert(END, 'Installing Scritps... All of Them\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Creating Pirate Themes\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Creating Custom Weapons and Zombie Models\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Dead Ship Successfuly Installed')
			output.update_idletasks()
			Slack.send_message('#coding', 'Map Installed through UI: Dead Ship')

	def uninstall(self):
		print('mapname = ' + self.mapname)
		print('Removing Scritps... All of Them')
		time.sleep(2)
		print('Removing Pirate Theme')
		time.sleep(2)
		print('Removing Custom Weapons and Zombie Models')
		time.sleep(2)
		print('Dead Ship Uninstall with No Error')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Custom Weapons')
		print('- Pirate Style Theme')
		print('- Custom Zombie Models')
		print('- Custom Perks')