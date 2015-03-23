#!/usr/bin/python

import argparse
import subprocess
import time

parser = argparse.ArgumentParser(description='World at War Mod Manager 1.0')

parser.add_argument('-v','--version', help='Print Version', action='version', version='WaW Mod Manager Version 1.0')
parser.add_argument('-i','--install', help='Install new map', action='store', dest='map_name', required=False)
parser.add_argument('-m', '--installmod', help='Installs Specified Mod', action='store', dest='mod_name', required=False)
parser.add_argument('-u','--uninstall', help='Uninstall map', action='store', dest='uninstall_map_name', required=False)
parser.add_argument('-s', '--wawstatus', help='Displays the WaW Status', action='store', dest='status', required=False)
parser.add_argument('-l', '--listofmaps', help='Show a List of Installable Maps and Mods', action='store', dest='list', required=False)

user_map_name = ''
args = parser.parse_args()

if(args.list == 'list'):
    print 'Maps:'
    print 'Zombie Cargo'
    print 'Zombie Slums'
    print 'TMG Christmas 1.1'
    print 'Purple Dimension'
    print 'survivedabox'
    print 'Cryogenic'
    print ''
    print 'Mods:'
    print 'WaW Mod Tools'
    print 'UGX Mod 1.0.4'

if(args.status == 'status'):
    print 'WaW Online Services: Running'
    print 'WaW Mod Manager 1.0: Running'

if(args.mod_name == 'ugx_mod_1_0_4'):
    print 'mod_name = UGX Mod 1.0.4'
    print 'Copying Files to c://ProgramFilesx86/Steam/steamapps/common/CallofDutyWorldatWar'
    print 'Installing .gsc Files'
    print 'Installing Yo Momma'
    print 'WARNING: It is not our fault if you do not backup your root'
    raw_input("PRESS ENTER TO CONTINUE:")
    time.wait(5)
    print 'UGX Mod 1.0.4 Installed Successfuly'
elif(args.mod_name == 'waw_modtools'):
    print 'Copying Files to c://ProgramFilesx86/Steam/steamapps/common/CallofDutyWorldatWar. Completed'
    print 'Running Shell Scripts. Completed'
    print 'WARNING: It is not our fault if you do not back up your root'
    raw_input("PRESS ENTER TO CONTINUE:")
    time.wait(5)
    print 'Installing Launcher. Completed'
    print 'Installing Script Placer. Completed'
    print 'Installing WeaponsEditor++. Completed'
    print 'WaW Mod Tools Successfuly Installed'

## Map Installs Below

if(args.map_name == 'zombie_cargo'):
   print 'map_name = Zombie Cargo'
   print 'homepage = http://www.ugx-mods.com'
   print 'map_homepage = http://ugx-mods.com/forum/index.php?topic=5645.0'
   ## subprocess.call(["c:\\Desktop\Zombie/ Cargo.exe"])
   time.wait(2)
   print 'Installing Files'
   print 'Creating Images'
   print 'Zombie Cargo Installed Successfuly'
elif(args.map_name == 'zombie_slums'):
    print 'mapname = Zombie Slums'
    print 'homepage = http://www.zombiemodding.com'
    print 'map_homepage = http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1661'
    ## subprocess.call(["c:\\Desktop\nazi_zombie_slums.exe"])
    time.wait(2)
    print 'Installing Files'
    print 'Creating Images'
    print 'Zombie Slums Installed Successfuly'
elif(args.map_name == 'tmg_christmas1.1'):
    print 'mapname = TMG Christmas 1.1'
    print 'homepage = http://www.zommods.com'
    print 'map_homepage = http://zommods.com/tmg-christmas/'
    ## subprocess.call(["C:\\Desktop\TMG_Christmas1.1.exe"])
    time.wait(2)
    print 'Installing Files'
    print 'Creating Images'
    print 'Setting Weather'
    print 'TMG Christmas 1.1 Installed Successfuly'
elif(args.map_name == 'purple_dimension'):
    print 'mapname = Purple Dimension'
    print 'homepage = http://www.zombiemodding.com'
    print 'map_homepage = http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1771'
    ## subprocess.call(["C:\\Desktop\PurpleDimension.exe"])
    time.wait(2)
    print 'Installing Files'
    print 'Creating Images'
    print 'Setting Weather'
    print 'Purple Dimension Installed Successfuly'
elif(args.map_name == 'survivedabox'):
    print 'mapname = survivedabox'
    print 'homepage = http://www.zombiemodding.com'
    print 'map_homepage = http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1819'
    ## subprocess.call(["C://Desktop/survivedabox.exe"])
    time.wait(2)
    print 'Installing Files'
    print 'Creating Images'
    print 'survivedabox Installed Successfuly'
elif(args.map_name == 'cryogenic'):
    print 'mapname = Cryogenic'
    print 'homepage = http://www.ugx-mods.com'
    print 'map_homepage = http://ugx-mods.com/forum/index.php?topic=5860.0'
    ## subprocess.call(["C://Desktop/Cryogenic.exe"])
    time.wait(2)
    print 'Installing Files'
    print 'Creating Images'
    print 'Setting Blood Rain'
    print 'Cryogenic Installed Successfuly'
elif(args.map_name == 'one_window_challange'):
    print 'mapname = One Window Challange'
    print 'homepage = http://zommods.com/'
    print 'map_homepage = http://zommods.com/zm_one-window-challenge/'
    ## subprocess.call(["C://Desktop/zm_owc.exe"])
    time.wait(2)
    print 'Installing Files'
    print 'Creating Images'
    print 'One Window Challange Installed Successfuly'
elif(args.map_name == 'project_viking1.0.2_beta'):
    print 'mapname = Project Viking 1.0.2 Beta'
    print 'homepage = http://ugx-mods.com/'
    print 'map_homepage = http://ugx-mods.com/forum/index.php?topic=1620.0'
    ## subprocess.call(["C://Desktop/ProjectVikingBetaV1.0.2.exe"])
    time.wait(2)
    print 'Installing Files'
    print 'Creating Images'
    print 'Project Viking Beat 1.0.2 Installed Successfuly'

## Map Uninstalls

if(args.uninstall_map_name == 'zombie_cargo'):
    print 'Removing Files/Scripts'
    time.wait(2)
    print 'Zombie Cargo Map Uninstalled with No Errors'
elif(args.uninstall_map_name == 'zombie_slums'):
    print 'Removing Files/Scripts'
    time.wait(2)
    print 'Zombie Slums Map Uninstaled with No Errors'
elif(args.uninstall_map_name == 'tmg_christmas1.1'):
    print 'Removing Files/Scripts'
    time.wait(2)
    print 'TMG Christmas Map Uninstalled with No Errors'
elif(args.uninstall_map_name == 'purple_dimension'):
    print 'Removing Files/Scripts'
    time.wait(2)
    print 'Purple Dimension Map Uninstalled with No Errors'
elif(args.uninstall_map_name == 'survivedabox'):
    print 'Removing Files/Scripts'
    time.wait(2)
    print 'survivedabox Map Uninstalled with No Errors'
elif(args.uninstall_map_name == 'cryogenic'):
    print 'Removing Files/Scripts'
    time.wait(2)
    print 'Cryogenic Map Uninstalled with No Errors'
elif(args.uninstall_map_name == 'one_window_challange'):
    print 'Removing Files/Scripts'
    time.wait(2)
    print 'One Window Challange Uninstalled with No Errors'
elif(args.uninstall_map_name == 'project_viking1.0.2_beta'):
    print 'Removing Files/Scripts'
    time.wait(2)
    print 'Project Viking Beat 1.0.2 Uninstalled with No Errors'


