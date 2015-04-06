import time
from .WawMaps import WawMaps
from slack.Slack import Slack

class CheeseCube(WawMaps):

    def install(self, output=None):
        if output == None:
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
            Slack.send_message('#coding', 'Map Installed: Cheese Cube')
        else:
            output.delete(1.0, END)
            output.insert(INSERT, 'mapname = ' + self.mapname + '\n')
            output.update_idletasks()
            output.insert(END, 'homepage = ' + self.homepage + '\n')
            output.update_idletasks()
            output.insert(END, 'map_homepage = ' + self.map_homepage + '\n')
            output.update_idletasks()
            # subprocess.call([C:\\Desktop\Cheese/ Cube/ V1/ by/ ZK.exe])
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
            output.insert(END, 'Creating Bubble Zombies\n')
            output.update_idletasks()
            time.sleep(3)
            output.insert(END, 'Cheese Cube Successfuly Installed')
            output.update_idletasks()
            Slack.send_message('#coding', 'Map Installed through UI: Cheese Cube')

    def uninstall(self):
        print('Removing Files/Scripts')
        time.sleep(2)
        print('Removing from Mods Folder')
        time.sleep(2)
        print('Removing from Root')
        time.sleep(4)
        print('Cheese Cube Uninstalled with No Errors')

    def reset(self):
        print('mapname = ' + self.mapname)
        time.sleep(2)
        print('Reversing Cheeseienes')
        time.sleep(2)
        print('Cheese Cube Reset Complete')

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
