import time
from WawMaps import WawMaps

class CheeseCube(WawMaps):

    def install(self):
        print('mapname = ' + self.mapname)
        print('homepage = ' + self.homepage)
        print('map_homepage = ' + self.map_homepage)
        # subprocess.call([C:\\Desktop\Cheese/ Cube/ V1/ by/ ZK.exe])
        time.sleep(2)
        print('Installing Files/Scripts')
        time.sleep(2)
        print('Creating Images')
        time.sleep(1)
        print('Cheese Cube Installed Successfuly')

    def uninstall(self):
        print('Removing Files/Scripts')
        time.sleep(2)
        print('Removing from Mods Folder')
        time.sleep(2)
        print('Removing from Root')
        time.sleep(4)
        print('Cheese Cube Uninstalled with No Errors')

    def description(self):
        print('mapname = ' + self.mapname)
        print('homepage = ' + self.homepage)
        print('map_homepage = ' + self.map_homepage)
        print('by ZK (or Zombie Killr)')
        print('- Standard Der Riese No Dogs')
        print('- Box Map with 6 Buyable Doors')
        print('- 2 Custom Perks: Dr. Dagger and Double Dew')
        print('- Returning Fan Favorite Cheese Gun w/ Sight')
        print('- Black Ops Perks')
        print('- Double Tap 2.0')
        print('- All Perks are 2x the Price (Added Difficulty)')
        print('- Modified Mystery Box')
        print('- Re-Skinned Pack a Punch, weapons, and Zombies')
