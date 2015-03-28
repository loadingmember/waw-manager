import tkinter as tk

class WawManagerApplication(tk.Frame):
    
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.parent = master
		self.parent.title("WawManager Application")
		self.center_window()

	def center_window(self):
		w = 500
		h = 200

		sw = self.master.winfo_screenwidth()
		sh = self.master.winfo_screenheight()

		x = (sw - w)/2
		y = (sh - h)/2
		self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))