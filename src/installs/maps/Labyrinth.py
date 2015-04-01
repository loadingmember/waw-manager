import time
import os
import sys
from .WawMaps import WawMaps
from slack.Slack import Slack
from tkinter as tk
from tkinter import *

class Labyrinth(WawMaps):

	def install(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		## subprocess.call([C:\\Desktop\labyrinth.exe])
		time.sleep(2)
		print('Installing Files')
		time.sleep(2)
		print('Creating Images')
		time.sleep(2)
		print('Creating Box')
		time.sleep(2)
		print('Labyrinth 1.2 Now Installed Successfuly')

	def install(self, output):
		output.delete(1.0, END)
		output.insert(INSERT, 'mapname = ' + self.mapname + '\n')
		output.update_idletasks()
		output.insert(END, 'homepage = ' + self.homepage + '\n')
		output.update_idletasks()
		output.insert(END, 'map_homepage = ' + self.map_homepage + '\n')
		output.update_idletasks()
		## subprocess.call(["c:\\Desktop\nazi_zombie_labyrinth.exe"])
		time.sleep(3)
		output.insert(END, 'Installing Files/Scripts\n')
		output.update_idletasks()
		time.sleep(2)
		output.insert(END, 'Creating Images\n')
		output.update_idletasks()
		time.sleep(2)
		output.instert(END, 'Creating Huge Box\n')
		output.update_idletasks()
		time.sleep(3)
		output.insert(END, 'Labyrinth Successfuly Installed')
		output.update_idletasks()
		Slack.send_message('#coding', 'Map Installed through UI: Labyrinth')

	def uninstall(self):
		print('mapname = ' + self.mapname)
		print('Removing Files/Scripts')
		# os.rmtree(Labyrinth)
		time.sleep(2)
		print('Removing from Root Directory')
		time.sleep(2)
		print('Removing Images')
		time.sleep(2)
		print('Labyrinth 1.2 Uninstalled with No Errors')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Black Ops Perks')
		print('- Black Ops Quick Revive')
		print('- Zombie or Freakbag Counter')
		print('- Custom Perks')
		print('- Custom Guns')
		print('- Nuketown Zombie Models')
		print('- Multiplayer Weapons')
		print('- Buildable Gun and Power')
		print('- Buyable Ending')