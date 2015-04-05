import time
from .WawMaps import WawMaps
from slack.Slack import Slack

class Familyguy(WawMaps):

	def install(self, output=None):
		if output == None:
			print('mapname = ' + self.mapname)
			print('homepage = ' + self.homepage)
			print('map_homepage = ' + self.map_homepage)
			print('Installing Files/Scripts')
			## subprocess.call([C:\\Desktop\nzai_zombie_familyguy.exe])
			time.sleep(2)
			print('Creating Ported Weapons')
			time.sleep(2)
			print('Creating Gas Pump Prefabs')
			time.sleep(2)
			print('Finishing Up...')
			time.sleep(2)
			print('Family Guy Zombies Successfuly Installed')
			Slack.send_message('#coding', 'Map Installed: Family Guy Zombies')
		else:
			output.delete(1.0, END)
			output.insert(INSERT, 'mapname = ' + self.mapname + '\n')
			output.update_idletasks()
			output.insert(END, 'homepage = ' + self.homepage + '\n')
			output.update_idletasks()
			output.insert(END, 'map_homepage = ' + self.map_homepage + '\n')
			output.update_idletasks()
			## subprocess.call(["c:\\Desktop\Zombie/ Cargo.exe"])
			output.insert(END, 'Installing Files/Scripts\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Creating Ported Weapons\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Creating Gas Pump Prefabs\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Family Guy Zombies Successfuly Installed')
			output.update_idletasks()
			Slack.send_message('#coding', 'Map Installed through UI: Family Guy Zombies')

	def uninstall(self):
		print('mapname  = ' + self.mapname)
		print('Removing Files/Scripts')
		time.sleep(2)
		print('Removing Ported Weapons')
		time.sleep(2)
		print('Removing Gas Pump Prefabs')
		time.sleep(2)
		print('Family Guy Zombies Uninstalled with No Errors')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Gas Pump Perk Prefabs')
		print('- Custom Zombie Models')
		print('- Teleporters')
		print('- Custom Mystery Box Prefab')
		print('- Custom Perk')
		print('- Custom Wonder Weapons')