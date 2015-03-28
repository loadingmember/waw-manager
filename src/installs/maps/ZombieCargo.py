import time
from WawMaps import WawMaps

class ZombieCargo(WawMaps):

   def install(self):
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

   def uninstall(self):
      print('Removing Files/Scripts')
      time.sleep(2)
      print('Zombie Cargo Map Uninstalled with No Errors')

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