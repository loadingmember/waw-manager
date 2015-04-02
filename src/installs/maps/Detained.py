import time
from .WawMaps import WawMaps
from slack.Slack import Slack

class Detained(WawMaps):

    def install(self, output=None):
        if output == None:
            print('mapname = ' + self.mapname)
            print('homepage = ' + self.homepage)
            print('map_homepage = ' + self.map_homepage)
            ## subprocess.call([C:\\Desktop\detained.exe])
            time.sleep(2)
            print('Installing Files')
            time.sleep(2)
            print('Creating Images')
            time.sleep(2)
            print('Detained R2 Successfuly Installed')
            Slack.send_message('#coding', 'Map Installed: Detained R2')
        else:
            output.delete(1.0, END)
            output.insert(INSERT, 'mapname = ' + self.mapname + '\n')
            output.update_idletasks()
            output.insert(END, 'homepage = ' + self.homepage + '\n')
            output.update_idletasks()
            output.insert(END, 'map_homepage = ' + self.map_homepage + '\n')
            output.update_idletasks()
            ## subprocess.call(["c:\\Desktop\Detained\ R2.exe"])
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
            output.insert(END, 'Creating Black and White Pictures')
            output.update_idletasks()
            time.sleep(2)
            output.insert(END, 'Detained R2 Successfuly Installed')
            output.update_idletasks()
            Slack.send_message('#coding', 'Map Installed through UI: Detained R2')

    def uninstall(self):
        print('mapname = ' + self.mapname)
        time.sleep(2)
        print('Removing Files/Scripts')
        time.sleep(2)
        print('Removing Images')
        time.sleep(2)
        print('Removing from Root')
        time.sleep(2)
        print(self.mapname + 'Removed with No Errors')

    def descritpion(self):
        print('mapname = ') + self.mapname
        print('homepage = ') + self.homepage
        print('map_homepage = ') + self.map_homepage
        print('- Heavily Modded')
        print('- Black and White View')
        print('- Custom Weapons')
        print('- Custom Zombies')
        print('- Prison Themed Map')