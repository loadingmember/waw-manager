import time
from slack.Slack import Slack
from .WawMaps import WawMaps

class annihilation(WawMaps):

	def install(self, output=None):
		if output == None:
			print('mapname = ' + self.mapname)
			print('homepage = ' + self.homepage)
			print('map_homepage = ' + self.map_homepage)
			print('Installing Scripts')
			## subprocess.call(["c:\\Desktop\annihilation(3).exe"])
			time.sleep(2)
			print('Creating Custom Weapons')
			time.sleep(2)
			print('Creating Full-Auto Colt')
			time.sleep(2)
			print('Creating Box')
			time.sleep(2)
			print('Annihilation Sucessfuly Installed')
			Slack.send_message('#coding', 'Map Installed through UI: Annihilation')
		else:
			output.delete(1.0, END)
			output.insert(INSERT, 'mapname = ' + self.mapname + '\n')
			output.update_idletasks()
			output.insert(END, 'homepage = ' + self.homepage + '\n')
			output.update_idletasks()
			output.insert(END, 'map_homepage = ' + self.map_homepage + '\n')
			output.update_idletasks()
			## subprocess.call(["c:\\Desktop\Zombie/ Cargo.exe"])
			time.sleep(2)
			output.insert(END, 'Installing Scripts\n')
			output.update_idletasks()
			time.sleep(4)
			output.insert(END, 'Creating Custom Weapons\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Creating Full-Auto Colt\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Creating Box\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Annihilation Successfuly Installed')
			output.update_idletasks()
			Slack.send_message('#coding', 'Map Installed through UI: Annihilation')

		def uninstall(self):
			print('mapname = ' + self.mapname)
			print('homepage = ' + self.homepage)
			print('map_homepage =' + self.map_homepage)
			print('Removing Scripts')
			time.sleep(2)
			print('Remvoing Custom Weapons')
			time.sleep(2)
			print('Removing Full-Auto Colt')
			time.sleep(2)
			print('Removing Box')
			time.sleep(2)
			print('Annihilation Uninstalled with No Errors')

		def description(self):
			print('mapname = ' + self.mapname)
			print('homepage = ' + self.homepage)
			print('map_homepage =' + self.map_homepage)
			print('- Box Map')
			print('- Full Auto Colt')
			print('- Custom Weapons')


