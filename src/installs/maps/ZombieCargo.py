import time
from .WawMaps import WawMaps
from slack.Slack import Slack

class ZombieCargo(WawMaps):

      def install(self, output=None):
            if output == None:
                  print('mapname = ' + self.mapname)
                  print('homepage = ' + self.homepage)
                  print('map_homepage = ' + self.map_homepage)
                  ## subprocess.call(["c:\\Desktop\Zombie/ Cargo.exe"])
                  time.sleep(2)
                  print('Installing Files')
                  time.sleep(4)
                  print('Creating Images')
                  time.sleep(2)
                  print('Creating Background Images')
                  time.sleep(2)
                  print('Installing FX')
                  time.sleep(2)
                  print('Zombie Cargo Installed Successfuly')
                  Slack.send_message('#coding', 'Map Installed: Zombie Cargo')
            else:
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
                  output.insert(END, 'Zombie Cargo Successfuly Installed')
                  output.update_idletasks()
                  Slack.send_message('#coding', 'Map Installed through UI: Zombie Cargo')

      def uninstall(self):
            print('Removing Files/Scripts')
            time.sleep(2)
            print('Zombie Cargo Map Uninstalled with No Errors')
            Slack.send_message('#coding', 'Map Uninstalled: Zombie Cargo')

      def reset(self):
            print('mapname = ' + self.mapname)
            time.sleep(2)
            print('Reversing Files and Water')
            time.sleep(2)
            print('Zombie Cargo Reset Complete')

      def description(self):
            print('mapname = ' + self.mapname)
            print('homepage = ' + self.homepage)
            print('map_homepage = ' + self.map_homepage)
            print('- 9 Perks')
            print('- Black Ops 2 Weapons with a few Modern Warfare 2 guns')
            print('- Kino Style Teleporter')
            print('- Expanded Map and Hidden Rooms')
            print('- Buildables')
            print('- 80 FOV')
            print('- Rain FX and Rain SFX')
            print('- Custom Pack a Punch Camo')
            print('- Double Tap 2.0')
            print('- A Unique way to Obtain Perk Slots')
            print('- Zombie Counter')
            print('- Buyable Ending')
            print('- Nuketown Zombie Models')
