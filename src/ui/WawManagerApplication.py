import tkinter as tk
from tkinter import *
from installs.maps.ZombieCargo import ZombieCargo
from installs.maps.ZombieSlums import ZombieSlums
from installs.maps.TMGChristmas import TMGChristmas
from installs.maps.Survivedabox import Survivedabox
from installs.maps.PurpleDimension import PurpleDimension
from installs.maps.ProjectViking import ProjectViking

class WawManagerApplication(tk.Frame):
    
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.parent = master
		self.parent.title("WawManager Application")
		self.center_window()
		## Cargo Button
		self.cargo = tk.Button(self.master, text="Install Zombie Cargo")
		self.cargo.bind('<ButtonPress>', self.press_cargo)
		## Slums Button
		self.slums = tk.Button(self.master, text="Install Zombie Slums")
		self.slums.bind('<ButtonPress>', self.press_slums)
		## TMG Button
		self.tmg = tk.Button(self.master, text="Install TMG Christmas 1.1")
		self.tmg.bind('<ButtonPress>', self.press_tmg)
		## Survivedabox Button
		self.survive = tk.Button(self.master, text="Install SurvivedaBox")
		self.survive.bind('<ButtonPress>', self.press_survive)
		## Puple Dimension Button
		self.purpled = tk.Button(self.master, text="Install Purple Dimension")
		self.purpled.bind('<ButtonPress>', self.press_purpled)
		## Project Viking
		self.viking = tk.Button(self.master, text="Install Project Viking")
		self.viking.bind('<ButtonPress>', self.press_viking)
		## One Window Button
		self.onewindow = tk.Button(self.master)
		self.onewindow.bind('<ButtonPress>', self.press_onewindow)
		## Output
		self.output = Text(self.master)
		self.output.height = 10
		self.output.width = 10
		# self.button.pack(side=LEFT)
		# self.slums.pack(side=LEFT)
		self.cargo.grid(row=0, column=0)
		self.slums.grid(row=1, column=0)
		self.tmg.grid(row=2, column=0)
		self.survive.grid(row=3, column=0, rowspan=1)
		self.purpled.grid(row=4, column=0, rowspan=1)
		self.viking.grid(row=5, column=0, rowspan=1)
		self.onewindow.grid(row=6, column=0)
		self.output.grid(row=0, column=1, rowspan=1)
		# self.tmg.pack(side=LEFT, padx=20, pady=20)
		# self.output.pack(side=RIGHT)

	def press_cargo(self, *args):
		zombie_cargo = ZombieCargo('Zombie Cargo', 'http://www.ugx-mods.com', 'http://ugx-mods.com/forum/index.php?topic=5645.0')
		zombie_cargo.install(self.output)

	def press_slums(self, *args):
		zombie_slums = ZombieSlums('Zombie Slums', 'http://www.zombiemodding.com', 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1661')
		zombie_slums.install(self.output)

	def press_tmg(self, *args):
		tmg = TMGChristmas('TMG Christmas 1.1', 'http://www.zommods.com', 'http://zommods.com/tmg-christmas/')
		tmg.install(self.output)

	def press_survive(self, *args):
		survive = Survivedabox('survivedabox', 'http://www.zombiemodding.com/', 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1819')
		survive.install(self.output)

	def press_purpled(self, *args):
		purpled = PurpleDimension('Purple Dimension', 'http://www.zombiemodding.com', 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1771')
		purpled.install(self.output)

	def press_viking(self, *args):
		viking = ProjectViking('Project Viking Beta 1.0.2', 'http://www.ugx-mods.com', 'http://ugx-mods.com/forum/index.php?topic=1620.0')
		viking.install(self.output)

	def center_window(self):
		w = 1000
		h = 1000

		sw = self.master.winfo_screenwidth()
		sh = self.master.winfo_screenheight()

		x = (sw - w)/2
		y = (sh - h)/2
		self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))