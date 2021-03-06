import time
from .WawMaps import WawMaps

class CheeseCubeUnlimited(WawMaps):

    def install(self, output=None):
        if output == None:
            print('mapname = ' + self.mapname)
            print('homepage = ' + self.homepage)
            print('map_homepage = ' + self.map_homepage)
            # subprocess.call([C:\\Desktop\Cheese/ Cube/ Unlimited/ v1.0.exe])
            time.sleep(2)
            print('Installing Scripts')
            time.sleep(2)
            print('Creating Images')
            time.sleep (3)
            print('Cheese Cube Unlimited Installed Successfuly')
            Slack.send_message('#coding', 'Map Installed: Cheese Cube Unlimited')
        else:
            output.delete(1.0, END)
            output.insert(INSERT, 'mapname = ' + self.mapname + '\n')
            output.update_idletasks()
            output.insert(END, 'homepage = ' + self.homepage + '\n')
            output.update_idletasks()
            output.insert(END, 'map_homepage = ' + self.map_homepage + '\n')
            output.update_idletasks()
            ## subprocess.call(["c:\\Desktop\Cheese\ Cube\ Unlimited\ v1.0.exe"])
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
            output.insert(END, 'Creating Iron Man Suit\n')
            output.update_idletasks
            time.sleep(3)
            output.insert(END, 'Cheese Cube Unlimited Successfuly Installed')
            output.update_idletasks()
            Slack.send_message('#coding', 'Map Installed through UI: Cheese Cube Unlimited')

    def uninstall(self):
        print('Removing Files/Scripts')
        time.sleep(2)
        print('Removing from Mods Folder')
        time.sleep(2)
        print('Removing from Root')
        time.sleep(4)
        print('Cheese Cube Unlimited Uninstalled with No Errors')

    def reset(self):
        print('mapname = ' + self.mapname)
        time.sleep(2)
        print('Reversing Cheeseienes Unlimited')
        time.sleep(2)
        print('Reset on Cheese Cube Unlimited Completed')

    def description(self):
        print('mapname = ' + self.mapname)
        print('homepage = ' + self.homepage)
        print('map_homepage = ' + self.map_homepage)
        print('- Unique Gameplay')
        print('- Moving Evviorment')
        print('- Black Ops 2 Weapons')
        print('- Buildables')
        print('- Puzzles')
        print('- Trivia')
        print('- Animated Pack a Punch Camo')
        print('- Extreme Zombies')
        print('- Custom Perks: PHD Flopper and Double Dew')
        print('- Custom Cheese Perk Shaders')
        print('- Custom Power Ups')
        print('- Random Easter Eggs')
        print('- Unique Ending')
        print('- IRON MAN SUIT!!!')