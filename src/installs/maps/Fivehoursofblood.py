import time
from .WawMaps import WawMaps
from slack.Slack import Slack

class Fivehoursofblood(WawMaps):

      def install(self):
            print('mapname = ' + self.mapname)
            print('homepage = ' + self.homepage)
            print('map_homepage = ' + self.map_homepage)
            print('Installing Files')
            time.sleep(2)
            print('Creating Blood')
            time.sleep(2)
            print('Creating Custom Weapons')
            time.sleep(2)
            print('Five Hours of Blood Successfuly Installed')
            Slack.send_message('#coding', 'Five Hours of Blood Installed')
            
      def uninstall(self):
            print('mapname = ' + self.mapname)
            print('homepage = ' + self.homepage)
            print('map_homepage = ' + self.map_homepage)
            print('Removing Scripts')
            time.sleep(2)
            print('Removing Blood')
            time.sleep(2)
            print('Removing Custom Weapons')
            time.sleep(2)
            print('Five Hours of Blood Removed with No Errors')

      def description(self):
            print('mapname = ' + self.mapname)
            print('homepage = ' + self.homepage)
            print('map_homepage = ' + self.map_homepage)
            print('- Lots and Lots of Blood')
            print('- Custom Weapons')
            print('- Made in Five Hours')
            print('- Custom Zombie Models')