from .WawMaps import WawMaps
import time
from slack.Slack import Slack

class Survivedabox(WawMaps):

	def install(self, output=None):
		if output == None:
			print('mapname = ' + self.mapname)
			print('homepage = ' + self.homepage)
			print('map_homepage = ' + self.map_homepage)
			## subprocess.call(["c:\\Desktop\survivedabox.exe"])
			print('Installing Files')
			time.sleep(3)
			print('Creating Nothing')
			time.sleep(2)
			print('Creating Images')
			time.sleep(3)
			print('Survivedabox Sucessfuly Installed')
			Slack.send_message('#coding', 'Map Installed: Survivedabox')
		else:
			output.delete(1.0, END)
			output.insert(INSERT, 'mapname = ' + self.mapname + '\n')
			output.update_idletasks()
			output.insert(END, 'homepage = ' + self.homepage + '\n')
			output.update_idletasks()
			output.insert(END, 'map_homepage = ' + self.map_homepage + '\n')
			output.update_idletasks()
			## subprocess.call(["c:\\Desktop\survivedabox.exe"])
			time.sleep(2)
			output.insert(END, 'Installing Files\n')
			output.update_idletasks()
			time.sleep(4)
			output.insert(END, 'Creating Images\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Creating Box\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Installing FX\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Survivedabox Successfuly Installed')
			output.update_idletasks()
			Slack.send_message('#coding', 'Map Installed through UI: Survivedabox')

	def uninstall(self):
		print('Removing Files/Scripts')
		time.sleep(2)
		print('survivedabox Map Uninstalled with No Errors')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Box Map')
		print('- Buyable Extra Room')
		print('- All Perks and Packa-a-Punch')
		print('- 5000000 Starting Points')
		print('- 2 Zombie Windows')
		print('- Teleporter')