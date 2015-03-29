import tkinter as tk
from tkinter import *
from installs.maps.ZombieCargo import ZombieCargo
from installs.maps.ZombieSlums import ZombieSlums
from installs.maps.TMGChristmas import TMGChristmas

class WawManagerApplication(tk.Frame):
    
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.parent = master
		self.parent.title("WawManager Application")
		self.center_window()
		## Cargo Button
		self.button = tk.Button(self.master, text="Install Zombie Cargo")
		self.button.bind('<ButtonPress>', self.press_cargo)
		## Slums Button
		slums = tk.Button(self.master, text="Install Zombie Slums")
		slums.bind('<ButtonPress>', self.press_slums)
		## TMG Button
		tmg = tk.Button(self.master, text="Install TMG Christmas 1.1")
		tmg.bind('<ButtonPress>', self.press_tmg)
		self.output = Text(self.master)
		self.output.height = 10
		self.button.pack(side=LEFT)
		slums.pack(side=LEFT)
		tmg.pack(side=LEFT)
		self.output.pack(side=RIGHT)

	def press_cargo(self, *args):
		zombie_cargo = ZombieCargo('Zombie Cargo', 'http://www.ugx-mods.com', 'http://ugx-mods.com/forum/index.php?topic=5645.0')
		zombie_cargo.install(self.output)

	def press_slums(self, *args):
		zombie_slums = ZombieSlums('Zombie Slums', 'http://www.zombiemodding.com', 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1661')
		zombie_slums.install(self.output)

	def press_tmg(self, *args):
		tmg = TMGChristmas('TMG Christmas 1.1', 'http://www.zommods.com', 'http://zommods.com/tmg-christmas/')
		tmg.install(self.output)

	def center_window(self):
		w = 1000
		h = 1000

		sw = self.master.winfo_screenwidth()
		sh = self.master.winfo_screenheight()

		x = (sw - w)/2
		y = (sh - h)/2
		self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))