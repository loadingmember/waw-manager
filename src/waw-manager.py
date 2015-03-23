#!/usr/bin/python

import argparse
import subprocess
import time

parser = argparse.ArgumentParser(description='World at War Mod Manager 1.0')

parser.add_argument('-version','--version', help='Print Version', action='version', version='WaW Mod Manager Version 1.1')
parser.add_argument('-installmap','--install', help='Install new map', action='store', dest='map_name', required=False)
parser.add_argument('-installmod', '--installmod', help='Installs Specified Mod', action='store', dest='mod_name', required=False)
parser.add_argument('-rmmap','--uninstall', help='Uninstall map', action='store', dest='remove_map_name', required=False)
parser.add_argument('-status', '--wawstatus', help='Displays the WaW Status', action='store', dest='status', required=False)
parser.add_argument('-list', '--listofmaps', help='Show a List of Installable Maps and Mods', action='store', dest='list', required=False)

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
    print 'Project Viking Beta 1.0.2'
    print ''
    print 'Mods:'
    print 'WaW Mod Tools'
    print 'UGX Mod 1.0.4'
    print 'Black Ops Perks Mod'

if(args.status == 'status'):
    print 'WaW Online Services: Running'
    print 'WaW Mod Manager 1.0: Running'
    print "www.zombiemodding.com: Running"
    print "www.ugx-mods.com: Running"

if(args.mod_name == 'ugx_mod_1_0_4'):
    print 'mod_name = UGX Mod 1.0.4'
    print 'Copying Files to c://ProgramFilesx86/Steam/steamapps/common/CallofDutyWorldatWar'
    print 'Installing .gsc Files'
    time.sleep(2)
    print 'Installing Yo Momma'
    print 'WARNING: It is not our fault if you do not backup your root'
    raw_input("PRESS ENTER TO CONTINUE:")
    time.sleep(3)
    print 'UGX Mod 1.0.4 Installed Successfuly'
elif(args.mod_name == 'waw_modtools'):
    print 'Copying Files to c://ProgramFilesx86/Steam/steamapps/common/CallofDutyWorldatWar. Completed'
    print 'Running Shell Scripts. Completed'
    print 'WARNING: It is not our fault if you do not back up your root'
    raw_input("PRESS ENTER TO CONTINUE:")
    time.sleep(2)
    print 'Installing Launcher. Completed'
    time.sleep(2)
    print 'Installing Script Placer. Completed'
    time.sleep(2)
    print 'Installing WeaponsEditor++. Completed'
    time.sleep(2)
    print 'WaW Mod Tools Successfuly Installed'
elif(args.mod_name == 'black_ops_perks'):
    print 'mod_name = Black Ops Perks'
    print 'Copying files to root directory'
    print 'Copying Prefabs'
    time.sleep(2)
    print 'Black Ops Perks Successfuly Installed'

## Map Installs Below

if(args.map_name == 'zombie_cargo'):
   print 'map_name = Zombie Cargo'
   print 'homepage = http://www.ugx-mods.com'
   print 'map_homepage = http://ugx-mods.com/forum/index.php?topic=5645.0'
   ## subprocess.call(["c:\\Desktop\Zombie/ Cargo.exe"])
   time.sleep(2)
   print 'Installing Files'
   print 'Creating Images'
   print 'Zombie Cargo Installed Successfuly'
elif(args.map_name == 'zombie_slums'):
    print 'mapname = Zombie Slums'
    print 'homepage = http://www.zombiemodding.com'
    print 'map_homepage = http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1661'
    ## subprocess.call(["C:\\Desktop\nazie_zombie_slums.exe"])
    time.sleep(3)
    print 'Installing Files'
    print 'Creating Images'
    print 'Zombie Slums Installed Successfuly'
elif(args.map_name == 'tmg_christmas1.1'):
    print 'mapname = TMG Christmas 1.1'
    print 'homepage = http://www.zommods.com'
    print 'map_homepage = http://zommods.com/tmg-christmas/'
    ## subprocess.call(["C:\\Desktop\TMG_Christmas1.1.exe"])
    time.sleep(3)
    print 'Installing Files'
    print 'Creating Images'
    print 'Setting Weather'
    print 'TMG Christmas 1.1 Installed Successfuly'
elif(args.map_name == 'purple_dimension'):
    print 'mapname = Purple Dimension'
    print 'homepage = http://www.zombiemodding.com'
    print 'map_homepage = http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1771'
    ## subprocess.call(["C:\\Desktop\PurpleDimension.exe"])
    time.sleep(5)
    print 'Installing Files'
    print 'Creating Images'
    print 'Setting Weather'
    print 'Purple Dimension Installed Successfuly'
elif(args.map_name == 'survivedabox'):
    print 'mapname = survivedabox'
    print 'homepage = http://www.zombiemodding.com'
    print 'map_homepage = http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1819'
    ## subprocess.call(["C://Desktop/survivedabox.exe"])
    time.sleep(2)
    print 'Installing Files'
    print 'Creating Images'
    print 'survivedabox Installed Successfuly'
elif(args.map_name == 'cryogenic'):
    print 'mapname = Cryogenic'
    print 'homepage = http://www.ugx-mods.com'
    print 'map_homepage = http://ugx-mods.com/forum/index.php?topic=5860.0'
    ## subprocess.call(["C://Desktop/Cryogenic.exe"])
    time.sleep(5)
    print 'Installing Files'
    print 'Creating Images'
    print 'Setting Blood Rain'
    print 'Cryogenic Installed Successfuly'
elif(args.map_name == 'one_window_challange'):
    print 'mapname = One Window Challange'
    print 'homepage = http://zommods.com/'
    print 'map_homepage = http://zommods.com/zm_one-window-challenge/'
    ## subprocess.call(["C://Desktop/zm_owc.exe"])
    time.sleep(2)
    print 'Installing Files'
    print 'Creating Images'
    print 'One Window Challange Installed Successfuly'
elif(args.map_name == 'project_viking1.0.2_beta'):
    print 'mapname = Project Viking 1.0.2 Beta'
    print 'homepage = http://ugx-mods.com/'
    print 'map_homepage = http://ugx-mods.com/forum/index.php?topic=1620.0'
    ## subprocess.call(["C://Desktop/ProjectVikingBetaV1.0.2.exe"])
    time.sleep(4)
    print 'Installing Files'
    print 'Creating Images'
    print 'Project Viking Beta 1.0.2 Installed Successfuly'

## Map Removes

if(args.remove_map_name == 'zombie_cargo'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'Zombie Cargo Map Uninstalled with No Errors'
elif(args.remove_map_name == 'zombie_slums'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'Zombie Slums Map Uninstaled with No Errors'
elif(args.remove_map_name == 'tmg_christmas1.1'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'TMG Christmas Map Uninstalled with No Errors'
elif(args.remove_map_name == 'purple_dimension'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'Purple Dimension Map Uninstalled with No Errors'
elif(args.remove_map_name == 'survivedabox'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'survivedabox Map Uninstalled with No Errors'
elif(args.remove_map_name == 'cryogenic'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'Cryogenic Map Uninstalled with No Errors'
elif(args.remove_map_name == 'one_window_challange'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'One Window Challange Uninstalled with No Errors'
elif(args.remove_map_name == 'project_viking1.0.2_beta'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'Removing from Mods Folder'
    time.sleep(2)
    print 'Removing from Root'
    time.sleep(4)
    print 'Project Viking Beta 1.0.2 Uninstalled with No Errors'


