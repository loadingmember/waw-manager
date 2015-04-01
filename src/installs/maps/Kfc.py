import time
from .WawMaps import WawMaps
from tkinter as tk
from tkinter import *
from slack.Slack import Slack

class Kfc(WawMaps):

    def install(self):
        print('mapname = ' + self.mapname)
        print('homepage = ' + self.homepage)
        print('map_homepage = ' + self.map_homepage)
        ## subprocess.call([C:\\Desktop\KFC.exe])
        time.sleep(3)
        print('Installing Files')
        time.sleep(2)
        print('Creating Images')
        print('Zombie KFC Map Installed Successfuly')
        Slack.send_message('#coding', 'Map InstalledL KFC')

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
        output.insert(END, 'Creating Player\n')
        output.update_idletasks()
        time.sleep(2)
        output.insert(END, 'KFC Successfuly Installed')
        output.update_idletasks()
        Slack.send_message('#coding', 'Map Installed through UI: KFC')

    def uninstall(self):
        print('Removing Files/Scripts')
        time.sleep(2)
        print('Removing from Mods Folder')
        time.sleep(2)
        print('Removing from Root')
        time.sleep(4)
        print('KFC Uninstalled with No Errors')

    def description(self):
        print('mapname = ' + self.mapname)
        print('homepage = ' + self.homepage)
        print('map_homepage = ' + self.map_homepage)
        print('Custom Textures')
        print('Custom Transit Zombies')
        print('Custom Buyable Guns')
        print('Friendly AI')