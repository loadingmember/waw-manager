import time
from WawMaps import WawMaps

class CheeseCube(WawMaps):

    def install(self):
        print 'mapname = ' + self.mapname
        print 'homepage = ' + self.homepage
        print 'map_homepage = ' + self.homepage
        # subprocess.call([C:\\Desktop\Cheese/ Cube/ V1/ by/ ZK.exe])
        time.sleep(2)
        print 'Installing Files/Scripts'
        time.sleep(2)
        print 'Creating Images'
        print time.sleep(1)
        print 'Cheese Cube Installed Successfuly'

    def uninstall(self):
        print 'Removing Files/Scripts'
        time.sleep(2)
        print 'Removing from Mods Folder'
        time.sleep(2)
        print 'Removing from Root'
        time.sleep(4)
        print 'Cheese Cube Uninstalled with No Errors'