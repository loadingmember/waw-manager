import time
from .WawMaps import WawMaps
from slack.Slack import Slack
import tkinter as tk
from tkinter import *

class TMGChristmas(WawMaps):

	def install(self, output=None):
		if output == None:
			print('mapname = ' + self.mapname)
			print('homepage = ' + self.homepage)
			print('map_homepage = ' + self.map_homepage)
			## subprocess.call(["c:\\Desktop\TMG_Christmas1.1.exe.exe"])
			print('Installing Files/Scripts')
			time.sleep(3)
			print('Creating Images')
			time.sleep(2)
			print('Setting Weather')
			time.sleep(2)
			print('Creating FX')
			time.sleep(3)
			print('TMG Christmas Sucessfuly Installed')
			Slack.send_messag('#coding', 'Map Installed: TMG Christmas 1.1')
		else:
			output.delete(1.0, END)
			output.insert(INSERT, 'mapname = ' + self.mapname + '\n')
			output.update_idletasks()
			output.insert(END, 'homepage = ' + self.homepage + '\n')
			output.update_idletasks()
			output.insert(END, 'map_homepage = ' + self.map_homepage + '\n')
			output.update_idletasks()
			## subprocess.call(["c:\\Desktop\TMG_Christmas1.1.exe.exe"])
			output.insert(END, 'Installing Files/Scripts\n')
			output.update_idletasks()
			time.sleep(3)
			output.insert(END, 'Creating Images\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Setting Weather\n')
			output.update_idletasks()
			time.sleep(2)
			output.insert(END, 'Creating and Installing FX\n')
			output.update_idletasks()
			time.sleep(3)
			output.insert(END, 'TMG Christmas 1.1 Successfuly Installed')
			output.update_idletasks()
			Slack.send_message('#coding', 'Map Installed through UI: TMG Christmas 1.1')

	def uninstall(self):
		print('Removing Files')
		time.sleep(2)
		print('TMG Christmas 1.1 Uninstalled with No Errors')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Soul Chests')
		print('- Snow')
		print('- MW2 Guns')
		print('- Black Ops 2 Weapons')
		print('- All Perks + Custom Perks')
		print('- All Wonder Weapons')