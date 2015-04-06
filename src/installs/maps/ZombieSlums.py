import time
from .WawMaps import WawMaps
from slack.Slack import Slack

class ZombieSlums(WawMaps):

	def install(self, output=None):
		if output == None:
			print('mapname = ' + self.mapname)
			print('homepage = ' + self.homepage)
			print('map_homepage = ' + self.map_homepage)
			## subprocess.call(["c:\\Desktop\nazi_zombie_slums.exe"])
			time.sleep(3)
			print('Installing Files/Scripts')
			time.sleep(2)
			print('Creating Images')
			time.sleep(2)
			print('Setting Weather and Time of Day')
			time.sleep(2)
			print('Zombie Slums succesfuly Installed')
		else:
			output.delete(1.0, END)
			output.insert(INSERT, 'mapname = ' + self.mapname + '\n')
			output.update_idletasks()
			output.insert(END, 'homepage = ' + self.homepage + '\n')
			output.update_idletasks()
			output.insert(END, 'map_homepage = ' + self.map_homepage + '\n')
			output.update_idletasks()
			## subprocess.call(["c:\\Desktop\nazi_zombie_slums.exe"])
			time.sleep(3)
			output.insert(END, 'Installing Files/Scripts\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Creating Images\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Setting Weather and Time of Day\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Zombie Slums Successfuly Installed')
			output.update_idletasks()
			Slack.send_message('#coding', 'Map Installed through UI: Zombie Slums')

	def uninstall(self):
		print('Removing Files/Scripts')
		time.sleep(2)
		print('Zombie Slums Map Uninstaled with No Errors')

	def reset(self):
		print('mapname = ' + self.mapname)
		time.sleep(2)
		print('Reversing Files and Zombies')
		time.sleep(2)
		print('Zombie Slums Reset Complete')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- 10 Perks')
		print('- No Easter Egg')
		print('- Custom Wonder Weapon: Raygun Mark 3 (Fully-Auto)')