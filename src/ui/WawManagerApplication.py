import tkinter as tk
from tkinter import *
from installs.maps.ZombieCargo import ZombieCargo
from installs.maps.ZombieSlums import ZombieSlums
from installs.maps.TMGChristmas import TMGChristmas
from installs.maps.Survivedabox import Survivedabox
from installs.maps.PurpleDimension import PurpleDimension
from installs.maps.ProjectViking import ProjectViking
from installs.maps.OneWindow import OneWindow
from installs.maps.Labyrinth import Labyrinth
from installs.maps.Kfc import Kfc
from installs.maps.Detained import Detained
# from installs.maps.Annihilation import Annihilation

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
		self.onewindow = tk.Button(self.master, text="Install One Window Challange")
		self.onewindow.bind('<ButtonPress>', self.press_onewindow)
		## Labyrinth
		self.labyrinth = tk.Button(self.master, text="Install Laybrinth")
		self.labyrinth.bind('<ButtonPress>', self.press_labyrinth)
		## KFC
		self.kfc = tk.Button(self.master, text="Install KFC Zombies")
		self.kfc.bind('<ButtonPress>', self.press_kfc)
		## Detained Button
		self.detained = tk.Button(self.master, text="Install Detained R2")
		# self.detained.bind('<ButtonPress>', self.press_detained)
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
		self.labyrinth.grid(row=7, column=0)
		self.kfc.grid(row=8, column=0)
		self.detained.grid(row=9, column=0)
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

	def press_onewindow(self, *args):
		onewindow = OneWindow('One Window Challange', 'http://www.zommods.com/', 'http://www.zommods.com/zm_one-window-challenge/')
		onewindow.install(self.output)

	def press_labyrinth(self, *args):
		labyrinth = Labyrinth('Labyrith 1.2', 'http://www.zombiemodding.com', 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1747')
		labyrinth.install(self.output)

	def press_kfc(self, *args):
		kfc = Kfc('Zombie KFC', 'http://www.zombiemodding.com/', 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1837')
		kfc.install(self.output)

	# def press_detained(self, *args):


	def center_window(self):
		w = 1000
		h = 1000

		sw = self.master.winfo_screenwidth()
		sh = self.master.winfo_screenheight()

		x = (sw - w)/2
		y = (sh - h)/2
		self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))