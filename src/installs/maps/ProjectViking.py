import time
from .WawMaps import WawMaps
from tkinter as tk
from tkinter import *
from slack.Slack import Slack

class ProjectViking(WawMaps):

	def install(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		## subprocess.call(["c:\\Desktop\ProjectVikingV1.0.2.exe"])
		print('Installing File/Scripts')
		time.sleep(2)
		print('Creating Images')
		time.sleep(3)
		print('Setting Weather/FX')
		time.sleep(2)
		print('Project Viking Beta 1.0.2 Installed Successfuly')
		Slack.send_message('#coding', 'Map Installed: Project Viking')

	def install(self,  output):
		output.delete(1.0, END)
		output.insert(INSERT, 'mapname = ' + self.mapname + '\n')
		output.update_idletasks()
		output.insert(END, 'homepage = ' + self.homepage + '\n')
		output.update_idletasks()
		output.insert(END, 'map_homepage = ' + self.map_homepage + '\n')
		output.update_idletasks()
		## subprocess.call(["c:\\Desktop\Zombie/ Cargo.exe"])
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
		output.insert(END, 'Project Viking Successfuly Installed')
		output.update_idletasks()
		Slack.send_message('#coding', 'Map Installed through UI: Project Viking')

	def uninstall(self):
		print('Removing Files/Scripts')
		time.sleep(2)
		print('Removing from Mods Folder')
		time.sleep(2)
		print('Removing from Root')
		time.sleep(4)
		print('Project Viking Beta 1.0.2 Uninstalled with No Errors')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Black Ops 2 Generators')
		print('- Black Ops 2 Wonder Weapons including the Paralizer, Blunder Gat and its variations, and the Ray Gun Mark 2')
		print('- Black Ops 2 Zombie Bosses including Brutus, crusaders and panzer soldat')
		print('- Black Ops 2 Buildables')
		print('- Black Ops 2 Die Rise Style Elevators')
		print('- Black Ops 2 Time Bomb from Buried')
		print('- Black Ops 1 Wonder Weapons including the Thunder Gun')
		print('- Black Ops 1 Kino Style Map PaP + 5 Switches to get to PaP')
		print('- Black Ops 1 Diving only with PHD Flopper')
		print('- Custom Wonder Weapons')
		print('- Anti Training/Camping (still possible but harder than usual)')
		print('- Game Modes Including Chaos Mode and Turned')
		print('- Kill Streaks including Predator Missle, AC130, and MOAB')
		print('- Black Ops 1 and 2 Perks except for tombstone')
		