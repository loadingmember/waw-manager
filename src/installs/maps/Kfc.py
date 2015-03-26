import time
from WawMaps import WawMaps

class Kfc(WawMaps):

    def install(self):
        print 'mapname = ' + self.mapname
        print 'homepage = ' + self.homepage
        print 'map_homepage = ' + self.map_homepage
        ## subprocess.call([C:\\Desktop\KFC.exe])
        time.sleep(3)
        print 'Installing Files'
        time.sleep(2)
        print 'Creating Images'
        print 'Zombie KFC Map Installed Successfuly'

    def uninstall(self):
        print 'Removing Files/Scripts'
        time.sleep(2)
        print 'Removing from Mods Folder'
        time.sleep(2)
        print 'Removing from Root'
        time.sleep(4)
        print 'KFC Uninstalled with No Errors'

    def description(self):
        print 'mapname = ' + self.mapname
        print 'homepage = ' + self.homepage
        print 'map_homepage = ' + self.map_homepage
        print 'Custom Textures'
        print 'Custom Transit Zombies'
        print 'Custom Buyable Guns'
        print 'Friendly AI'