import time
from slack.Slack import Slack
from .WawMaps import WawMaps

class Ubahn(WawMaps):

	def install(self, output=None):
		if output == None:
			print('mapname = ' + self.mapname)
			print('homepage = ' + self.homepage)
			print('map_homepage = ' + self.map_homepage)
			time.sleep(2)
			print('Installing Files/Scripts')
			## subprocess.call(["c:\\Desktop\nazi_zombie_ubahn.exe"])
			time.sleep(3)
			print('Creating Custom Weapons')
			time.sleep(2)
			print('Creating German Stuff')
			time.sleep(2)
			print('Zombie Ubahn Successfuly Installed')
			Slack.send_message('#coding', 'Map Installed: Zombie Ubahn')
		else:
			output.delete(1.0, END)
			output.insert(INSERT, 'mapname = ' + self.mapname + '\n')
			output.update_idletasks()
			output.insert(END, 'homepage = ' + self.homepage + '\n')
			output.update_idletasks()
			output.insert(END, 'map_homepage = ' + self.map_homepage + '\n')
			output.update_idletasks()
			## subprocess.call(["c:\\Desktop\nazi_zombie_ubahn.exe"])
			time.sleep(2)
			output.insert(END, 'Installing Files/Scripts\n')
			output.update_idletasks()
			time.sleep(4)
			output.insert(END, 'Creating Custom Weapons\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Creating German Stuff\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Zombie Ubahn Successfuly Installed')
			output.update_idletasks()
			Slack.send_message('#coding', 'Map Installed through UI: Zombie Ubahn')

		def uninstall(self):
			print('mapname = ' + self.mapname) 
			print('homepage = ' + self.homepage)
			print('map_homepage = ' + self.map_homepage)
			print('Uninstalling Files/Scripts')
			time.sleep(2)
			print('Uninstalling Custom Weapons')
			time.sleep(3)
			print('Removing German Stuff')
			time.sleep(2)
			print('Zombie Ubahn Uninstalled with No Errors')

		def description(self):
			print('mapname = ' + self.mapname)
			print('homepage = ' + self.homepage)
			print('map_homepage = ' + self.map_homepage)
			print('- Black Ops Weapons')
			print('- Black Ops Quick Revive') 
			print('- Buyable Ending')
			print('- End Game Location')
			print('- Pack a Punch Location')
			print('- Replaybale Music Boxes')
			print('- Fast Paced')
			print('- Secret Room')
			print('- Easter Eggs')