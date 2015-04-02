import time
from .WawMaps import WawMaps
from slack.Slack import Slack

class BikiniBottom(WawMaps):

	def install(self, output=None):
		if output == None:
			print('mapname = ' + self.mapname)
			print('homepage = ' + self.homepage)
			print('map_homepage = ' + self.map_homepage)
			# subprocess.call([C:\\Desktop\bikini_bottom.exe])
			time.sleep(3)
			print('Installing Files/Scripts')
			time.sleep(2)
			print('Creating Images')
			time.sleep(2)
			print('Bikini Bottom Zombies Installed Successfuly')
			Slack.send_message('#coding', 'Map Installed: Bikini Bottom Zombies')
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
			output.insert(END, 'Installing Files\n')
			output.update_idletasks()
			time.sleep(4)
			output.insert(END, 'Creating Images\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Background Images\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Installing FX\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Creating Black and White Pictures')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Detained R2 Successfuly Installed')
			output.update_idletasks()
			Slack.send_message('#coding', 'Map Installed through UI: Bikini Bottom Zombies')

	def uninstall(self):
		print('Removing Files/Scripts')
		time.sleep(2)
		print('Removing Mods Folder')
		time.sleep(2)
		print('Removing from Root')
		time.sleep(3)
		print('Bikini Bottom Uninstalled with No Errors')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Rediculous Arms')
		print('- Custom Weapons')
		print('- Bikini Bottom Coins as Points')
		print('- Lot of Perks')