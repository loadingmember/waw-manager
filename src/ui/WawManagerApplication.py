import tkinter as tk
from tkinter import *
from installs.maps.ZombieCargo import ZombieCargo

class WawManagerApplication(tk.Frame):
    
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.parent = master
		self.parent.title("WawManager Application")
		self.center_window()
		self.button = tk.Button(self.master, text="Press Me!")
		self.button.bind('<ButtonPress>', self.press)
		self.output = Text(self.master)
		self.output.height = 5
		self.button.pack()
		self.output.pack()

	def press(self, *args):
		zombie_cargo = ZombieCargo('Zombie Cargo', 'http://www.ugx-mods.com', 'http://ugx-mods.com/forum/index.php?topic=5645.0')
		zombie_cargo.install(self.output)

	def center_window(self):
		w = 500
		h = 200

		sw = self.master.winfo_screenwidth()
		sh = self.master.winfo_screenheight()

		x = (sw - w)/2
		y = (sh - h)/2
		self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))