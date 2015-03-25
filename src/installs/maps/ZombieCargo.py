import time
from WawMaps import WawMaps

class ZombieCargo(WawMaps):
   
   def install(self):
      print 'mapname = ' + self.mapname
      print 'homepage = ' + self.homepage
      print 'map_homepage = ' + self.map_homepage
      ## subprocess.call(["c:\\Desktop\Zombie/ Cargo.exe"])
      time.sleep(2)
      print 'Installing Files'
      time.sleep(4)
      print 'Creating Images'
      time.sleep(2)
      print 'Creating Background Images'
      time.sleep(2)
      print 'Installing FX'
      time.sleep(2)
      print 'Zombie Cargo Installed Successfuly'
