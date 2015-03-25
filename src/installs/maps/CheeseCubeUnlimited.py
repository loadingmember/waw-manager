import time
from WawMaps import WawMaps

class CheeseCubeUnlimited(WawMaps):

    def install(self):
        print 'mapname = ' + self.mapname
        print 'homepage = ' + self.homepage
        print 'map_homepage = ' + self.map_homepage
        # subprocess.call([C:\\Desktop\Cheese/ Cube/ Unlimited/ v1.0.exe])
        time.sleep(2)
        print 'Installing Scripts'
        time.sleep(2)
        print 'Creating Images'
        time.sleep (3)
        print 'Cheese Cube Unlimited Installed Successfuly'

    def uninstall(self):
        print 'Removing Files/Scripts'
        time.sleep(2)
        print 'Removing from Mods Folder'
        time.sleep(2)
        print 'Removing from Root'
        time.sleep(4)
        print 'Cheese Cube Unlimited Uninstalled with No Errors'