#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='World at War Mod Manager 1.0')

parser.add_argument('-v','--version', help='Print Version', action='version', version='WaW Mod Manager Version 1.0')
parser.add_argument('-i','--install', help='Install new map', action='store', dest='map_name', required=False)
parser.add_argument('-m', '--installmodtools', help='Installs the WaW Mod Tools', action='store', dest='mods', required=False)
parser.add_argument('-u','--uninstall', help='Uninstall map', action='store', dest='map_name', required=False)

args = parser.parse_args()


if(args.map_name == 'zombie_cargo'):
   print 'map_name = Zombie Cargo'
   print 'Installing Files'
   print 'Creating Images'
   print 'Zombie Cargo Installed Successfuly'
elif(args.map_name == 'zombie_slums'):
    print 'mapname = Zombie Slums'
    print 'Installing Files'
    print 'Creating Images'
    print 'Zombie Slums Installed Successfuly'


