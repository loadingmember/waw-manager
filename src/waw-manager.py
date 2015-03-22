#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='World at War Mod Manager 1.0')

parser.add_argument('-v','--version', help='Print Version', action='version', version='WaW Mod Manager Version 1.0')
parser.add_argument('-i','--install', help='Install new map', action='store', dest='map_name', required=False)
parser.add_argument('-m', '--installmodtools', help='Installs the WaW Mod Tools', action='store', dest='modtools_name', required=False)
parser.add_argument('-s', '--wawstatus', help='Displays the WaW Status', action='store', dest='status', required=False)
parser.add_argument('-u','--uninstall', help='Uninstall map', action='store', dest='map_name', required=False)

args = parser.parse_args()

if(args.status == 'status'):
    print 'WaW Online Services: Running'
    print 'WaW Mod Manager 1.0: Running'

if(args.modtools_name == 'waw_modtools'):
    print 'Copying Files to c://ProgramFilesx86/Steam/steamapps/common/CallofDutyWorldatWar. Completed'
    print 'Running Shell Scripts. Completed'
    print 'Installing Launcher. Completed'
    print 'Installing Script Placer. Completed'
    print 'Installing WeaponsEditor++. Completed'
    print 'WaW Mod Tools Successfuly Installed'

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
elif(args.map_name == 'tmg_christmas1.1'):
    print 'mapname = TMG Christmas 1.1'
    print 'Installing Files'
    print 'Creating Images'
    print 'Setting Weather'
    print 'TMG Christmas 1.1 Installed Successfuly'

