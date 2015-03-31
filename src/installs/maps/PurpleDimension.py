import time
from .WawMaps import WawMaps
from slack.Slack import Slack
import tkinter as tk
from tkinter import *

class PurpleDimension(WawMaps):

	def install(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		## subprocess.call(["c:\\Desktop\PurpleDimension.exe"])
		print('Installing Files')
		time.sleep(2)
		print('Creating FX')
		time.sleep(3)
		print('Creating Images')
		time.sleep(2)
		print('Determing Size')
		time.sleep(3)
		print('Purple Dimension Sucsesfuly Installed')
		Slack.send_message('#coding', 'Map Installed: Purple Dimension')

	def install(self, output):
		output.delete(1.0, END)
		output.insert(INSERT, 'mapname = ' + self.mapname + '\n')
		output.update_idletasks()
		output.insert(END, 'homepage = ' + self.homepage + '\n')
		output.update_idletasks()
		output.insert(END, 'map_homepage = ' + self.map_homepage + '\n')
		output.update_idletasks()
		## subprocess.call(["c:\\Desktop\Zombie/ Cargo.exe"])
		time.sleep(2)
		output.insert(END, 'Installing Files/Scripts\n')
		output.update_idletasks()
		time.sleep(4)
		output.insert(END, 'Creating Images\n')
		output.update_idletasks()
		time.sleep(2)
		output.insert(END, 'Installing FX\n')
		output.update_idletasks()
		time.sleep(2)
		output.insert(END, 'Purple Dimension Successfuly Installed')
		output.update_idletasks()
		Slack.send_message('#coding', 'Map Installed through UI: Purple Dimension')


	def uninstall(self):
		print('Removing Files/Scripts')
		time.sleep(2)
		print('Purple Dimension Map Uninstalled with No Errors')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Nuke Town Zombies')
		print('- Origins Mid-Evil Zombies')
		print('- Five Teleporters')
		print('- Kino Teleporter')
		print('- All Black Ops 1 Perks')
		print('- Buildables')
		print('- BUYABLE ENDING')
		print('- Purple Snow')
		print('- Different Players')
		print('- Change of Viewhands')
		print('- Moving Textures')
		print('- BOB')
		print('- Imported Weapons')
		print('- Spinning Stuff')
		print('- Music Box')
		print('- Solo Revive')
		print('- FX')
		print('- All WaW Weapons Removed Except for Ray Guns')
		print('- Fire Sale Powerup')
		print('- Moving Perks')
		print('and More...')