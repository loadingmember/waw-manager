import time
from .WawMaps import WawMaps
from tkinter as tk
from tkinter import *
from slack.Slack import Slack

class OneWindow(WawMaps):

	def install(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		## subprocess.call(["c:\\Desktop\zm_owc.exe"])
		print('Installing File/Scripts')
		time.sleep(2)
		print('Creating Box')
		time.sleep(2)
		print('One Window Challange Installed Succesfully')
		Slack.send_message('#coding', 'Map installed: One Window Challange')

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
		output.insert(END, 'Installing Files\n')
		output.update_idletasks()
		time.sleep(2)
		output.insert(END, 'Creating Box\n')
		output.update_idletasks()
		time.sleep(2)
		output.insert(END, 'One Window Challange Successfuly Installed')
		output.update_idletasks()
		Slack.send_message('#coding', 'Map Installed through UI: One Window Challange')


	def uninstall(self):
		print('Removing Files/Scripts')
		time.sleep(2)
		print('One Window Challange Uninstalled with No Errors')

	def description(self):
		print('mapname = ' + self.mapname)
		print('homepage = ' + self.homepage)
		print('map_homepage = ' + self.map_homepage)
		print('- Black Ops Weapons')
		print('- Black Ops Perks')
		print('- Buyable Powerups')
		print('- Box Map')
		print('- Custom Window Defense Script')
		print('- One Window')
		print('- Pack a Punch')