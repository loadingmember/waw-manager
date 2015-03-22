#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='World at War Mod Manager 1.0')

parser.add_argument('-v','--version', help='Print Version', action='version', version='WaW Mod Manager Version 1.0')
parser.add_argument('-i','--install', help='Install new map', action='store', dest='map_name', required=False)
parser.add_argument('-m', '--installmod', help='Installs Specified Mod', action='store', dest='mod_name', required=False)
parser.add_argument('-s', '--wawstatus', help='Displays the WaW Status', action='store', dest='status', required=False)
parser.add_argument('-u','--uninstall', help='Uninstall map', action='store', dest='map_name', required=False)

args = parser.parse_args()

if(args.status == 'status'):
    print 'WaW Online Services: Running'
    print 'WaW Mod Manager 1.0: Running'

if(args.mod_name == 'ugx_mod_1_0_4'):
    print 'mod_name = UGX Mod 1.0.4'
    print 'Copying Files to c://ProgramFilesx86/Steam/steamapps/common/CallofDutyWorldatWar'
    print 'Installing .gsc Files'
    print 'Installing Yo Momma'
    print 'UGX Mod 1.0.4 Installed Successfuly'
elif(args.mod_name == 'waw_modtools'):
    print 'Copying Files to c://ProgramFilesx86/Steam/steamapps/common/CallofDutyWorldatWar. Completed'
    print 'Running Shell Scripts. Completed'
    print 'Installing Launcher. Completed'
    print 'Installing Script Placer. Completed'
    print 'Installing WeaponsEditor++. Completed'
    print 'WaW Mod Tools Successfuly Installed'


if(args.map_name == 'zombie_cargo'):
   print 'map_name = Zombie Cargo'
   print 'homepage = http://www.ugx-mods.com'
   print 'map_homepage = http://ugx-mods.com/forum/index.php?topic=5645.0'
   print 'Installing Files'
   print 'Creating Images'
   print 'Zombie Cargo Installed Successfuly'
elif(args.map_name == 'zombie_slums'):
    print 'mapname = Zombie Slums'
    print 'homepage = http://www.zombiemodding.com'
    print 'map_homepage = http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1661'
    print 'Installing Files'
    print 'Creating Images'
    print 'Zombie Slums Installed Successfuly'
elif(args.map_name == 'tmg_christmas1.1'):
    print 'mapname = TMG Christmas 1.1'
    print 'homepage = http://www.zommods.com'
    print 'map_homepage = http://zommods.com/tmg-christmas/'
    print 'Installing Files'
    print 'Creating Images'
    print 'Setting Weather'
    print 'TMG Christmas 1.1 Installed Successfuly'
elif(args.map_name == 'purple_dimension'):
    print 'mapname = Purple Dimension'
    print 'homepage = http://www.zombiemodding.com'
    print 'map_homepage = http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1771'
    print 'Installing Files'
    print 'Creating Images'
    print 'Setting Weather'
    print 'Purple Dimension Installed Successfuly'
elif(args.map_name == 'survivedabox'):
    print 'mapname = survivedabox'
    print 'homepage = http://www.zombiemodding.com'
    print 'map_homepage = http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1819'
    print 'Installing Files'
    print 'Creating Images'
    print 'survivedabox Installed Successfuly'



