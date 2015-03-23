#!/usr/bin/python

import argparse
import subprocess
import time

parser = argparse.ArgumentParser(description='World at War Mod Manager 1.1')

parser.add_argument('-version','--version', help='Print Version', action='version', version='WaW Mod Manager Version 1.1')
parser.add_argument('-installmap','--install', help='Install new map', action='store', dest='map_name', required=False)
parser.add_argument('-installmod', '--installmod', help='Installs Specified Mod', action='store', dest='mod_name', required=False)
parser.add_argument('-rmmap','--uninstall', help='Uninstall map', action='store', dest='remove_map_name', required=False)
parser.add_argument('-rmmod', '--uninstallmod', help='Uninstall mod', action='store', dest='remove_mod_name', required=False)
parser.add_argument('-status', '--wawstatus', help='Displays the WaW Status', action='store', dest='status', required=False)
parser.add_argument('-list', '--listofmaps', help='Show a List of Installable Maps and Mods', action='store', dest='list', required=False)

args = parser.parse_args()


if(args.list == 'list'):
    print 'Maps:'
    print 'zombie_cargo'
    print 'zombie_slums'
    print 'tmg_christmas1.1'
    print 'purple_dimension'
    print 'survivedabox'
    print 'cryogenic'
    print 'project_viking1.0.2_beta'
    print 'kfc'
    print 'cheese_cube_unlimited'
    print 'cheese_cube'
    print ''
    print 'Mods:'
    print 'waw_modtools'
    print 'ugx_mod_1_0_4'
    print 'black_ops_perks'
    print 'black_ops_weapons'
    print 'scaretimes_scripts'

if(args.status == 'status'):
    print 'WaW Online Services: Running'
    print 'WaW Mod Manager 1.2: Running'
    print "www.zombiemodding.com: Running"
    print "www.ugx-mods.com: Running"
    print "www.zommods.com: Running"

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
    print 'Installing Map Manager. Completed'
    time.sleep(2)
    print 'WaW Mod Tools Successfuly Installed'
elif(args.mod_name == 'black_ops_perks'):
    print 'mod_name = Black Ops Perks'
    print 'Copying files to root directory'
    print 'Copying Prefabs'
    print 'WARNING: It is not our fault if you do not back up your root'
    raw_input("PRESS ENTER TO CONTINUE:")
    time.sleep(2)
    print 'Black Ops Perks Successfuly Installed'
elif(args.mod_name == 'black_ops_weapons'):
    print 'mod_name = Black Ops Weapons'
    print 'Copying Files to root directory'
    print 'Copying Files'
    raw_input("PRESS ENTER TO CONTINUE:")
    time.sleep(2)
    print 'Black Ops Weapons Successfuly Installed'
elif(args.mod_name == 'scaretimes_scripts'):
    print 'mod_name = Scaretimes Scripts and Prefabs'
    print 'Copying Files to root directory'
    print 'Copying Scripts'
    print 'Copying Prefabs'
    print 'WARNING: It is not our fault if you do not backup your root directory'
    raw_input("PRESS ENTER TO CONTINUE:")
    time.sleep(4)
    print 'Scaretimes Scripts and Prefabs Successfuly Installed'

## Map Installs Below


## Zombie Cargo

if(args.map_name == 'zombie_cargo'):
   mapname = 'Zombie Cargo'
   homepage = 'http://www.ugx-mods.com'
   map_homepage = 'http://ugx-mods.com/forum/index.php?topic=5645.0'
   print 'mapname = ' + mapname
   print 'homepage = ' + homepage
   print 'map_homepage = ' + map_homepage
   ## subprocess.call(["c:\\Desktop\Zombie/ Cargo.exe"])
   time.sleep(2)
   print 'Installing Files'
   print 'Creating Images'
   print 'Zombie Cargo Installed Successfuly'

## Zombie Slums

elif(args.map_name == 'zombie_slums'):
    mapname = 'Zombie Slums'
    homepage = 'http://www.zombiemodding.com'
    map_homepage = 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1661'
    print 'mapname = ' + mapname
    print 'homepage = ' + homepage
    print 'map_homepage = ' + map_homepage
    ## subprocess.call(["C:\\Desktop\nazie_zombie_slums.exe"])
    time.sleep(3)
    print 'Installing Files'
    print 'Creating Images'
    print 'Zombie Slums Installed Successfuly'

## TMG Christmas 1.1

elif(args.map_name == 'tmg_christmas1.1'):
    mapname = 'TMG Christmas 1.1'
    homepage = 'http://www.zommods.com'
    map_homepage = 'http://zommods.com/tmg-christmas/'
    print 'mapname = ' + mapname
    print 'homepage = ' + homepage
    print 'map_homepage = ' + map_homepage
    ## subprocess.call(["C:\\Desktop\TMG_Christmas1.1.exe"])
    time.sleep(3)
    print 'Installing Files'
    print 'Creating Images'
    print 'Setting Weather'
    print 'TMG Christmas 1.1 Installed Successfuly'

## Purple Dimension

elif(args.map_name == 'purple_dimension'):
    mapname = 'Purple Dimension'
    homepage = 'http://www.zombiemodding.com'
    map_homepage = 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1771'
    print 'mapname = ' + mapname
    print 'homepage = ' + homepage
    print 'map_homepage = ' + map_homepage
    ## subprocess.call(["C:\\Desktop\PurpleDimension.exe"])
    time.sleep(5)
    print 'Installing Files'
    print 'Creating Images'
    print 'Setting Weather'
    print 'Purple Dimension Installed Successfuly'

## survivedabox

elif(args.map_name == 'survivedabox'):
    mapname = 'survivedabox'
    homepage = 'http://www.zombiemodding.com/'
    map_homepage = 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1819'
    print 'mapname = ' + mapname
    print 'homepage = ' + homepage
    print 'map_homepage = ' + map_homepage
    ## subprocess.call(["C://Desktop/survivedabox.exe"])
    time.sleep(2)
    print 'Installing Files'
    print 'Creating Images'
    print 'survivedabox Installed Successfuly'

## Cryogenic 

elif(args.map_name == 'cryogenic'):
    mapname = 'Cryogenic'
    homepage = 'http://www.ugx-mods.com'
    map_homepage = 'http://ugx-mods.com/forum/index.php?topic=5860.0'
    print 'mapname = ' + mapname
    print 'homepage = ' + homepage
    print 'map_homepage = ' + map_homepage
    ## subprocess.call(["C://Desktop/Cryogenic.exe"])
    time.sleep(5)
    print 'Installing Files'
    print 'Creating Images'
    print 'Setting Blood Rain'
    print 'Cryogenic Installed Successfuly'

## One Window Challange

elif(args.map_name == 'one_window_challange'):
    mapname = 'One Window Challange'
    homepage = 'http://www.zommods.com'
    map_homepage = 'http://www.zommods.com/zm_one-window-challenge/'
    print 'mapname = ' + mapname
    print 'homepage = ' + homepage
    print 'map_homepage = ' + map_homepage
    ## subprocess.call(["C://Desktop/zm_owc.exe"])
    time.sleep(2)
    print 'Installing Files'
    time.sleep(2)
    print 'Creating Images'
    print 'One Window Challange Installed Successfuly'

## Project Viking

elif(args.map_name == 'project_viking1.0.2_beta'):
    mapname = 'Project Viking 1.0.2 Beta'
    homepage = 'http://www.ugx-mods.com'
    map_homepage = 'http://ugx-mods.com/forum/index.php?topic=1620.0'
    print 'mapname = ' + mapname
    print 'homepage = ' + homepage
    print 'map_homepage = ' + map_homepage
    ## subprocess.call(["C://Desktop/ProjectVikingBetaV1.0.2.exe"])
    time.sleep(4)
    print 'Installing Files'
    time.sleep(2)
    print 'Creating Images'
    print 'Project Viking Beta 1.0.2 Installed Successfuly'

## KFC

elif(args.map_name == 'kfc'):
    mapname = 'KFC Zombie'
    homepage = 'http://www.zombiemodding.com/'
    map_homepage = 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1837'
    print 'mapname = ' + mapname
    print 'homepage = ' + homepage
    print 'map_homepage = ' + map_homepage
    ## subprocess.call([C:\\Desktop\KFC.exe])
    time.sleep(3)
    print 'Installing Files'
    time.sleep(2)
    print 'Creating Images'
    print 'Zombie KFC Map Installed Successfuly'

## Cheese Cube Unlimited 

elif(args.map_name == 'cheese_cube_unlimited'):
    homepage = 'http://www.ugx-mods.com/'
    map_homepage = 'http://ugx-mods.com/forum/index.php?topic=2973.0'
    mapname = 'Cheese Cube Unlimited'
    print 'mapname = ' + mapname
    print 'homepage = ' + homepage
    print 'map_homepage = ' + map_homepage
    # subprocess.call([C:\\Desktop\Cheese/ Cube/ Unlimited/ v1.0.exe])
    time.sleep(2)
    print 'Installing Scripts'
    time.sleep(2)
    print 'Creating Images'
    time.sleep (3)
    print 'Cheese Cube Unlimited Installed Successfuly'

## Cheese Cube Standard

elif(args.map_name == 'cheese_cube'):
    homepage = 'http://www.zombiemodding.com/'
    map_homepage = 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1390'
    mapname = 'Cheese Cube'
    print 'mapname = ' + mapname
    print 'homepage = ' + homepage
    print 'map_homepage = ' + map_homepage
    # subprocess.call([C:\\Desktop\Cheese/ Cube/ V1/ by/ ZK.exe])
    time.sleep(2)
    print 'Installing Files/Scripts'
    time.sleep(2)
    print 'Creating Images'
    print time.sleep(1)
    print 'Cheese Cube Installed Successfuly'

## Map Removes ################################################################################################

if(args.remove_map_name == 'zombie_cargo'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'Zombie Cargo Map Uninstalled with No Errors'

## Zombie Slums Uninstall

elif(args.remove_map_name == 'zombie_slums'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'Zombie Slums Map Uninstaled with No Errors'

## TMG Christmas 1.1 Uninstall

elif(args.remove_map_name == 'tmg_christmas1.1'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'TMG Christmas Map Uninstalled with No Errors'

## Purple Dimension Uninstall

elif(args.remove_map_name == 'purple_dimension'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'Purple Dimension Map Uninstalled with No Errors'

## survivedabox uninstall

elif(args.remove_map_name == 'survivedabox'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'survivedabox Map Uninstalled with No Errors'

## Cryogenic Unistall

elif(args.remove_map_name == 'cryogenic'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'Cryogenic Map Uninstalled with No Errors'

## One Window Challange Uninstall

elif(args.remove_map_name == 'one_window_challange'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'One Window Challange Uninstalled with No Errors'

## Project Viking 1.0.2 Beta Uninstall

elif(args.remove_map_name == 'project_viking1.0.2_beta'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'Removing from Mods Folder'
    time.sleep(2)
    print 'Removing from Root'
    time.sleep(4)
    print 'Project Viking Beta 1.0.2 Uninstalled with No Errors'

## KFC Uninstall

elif(args.remove_map_name == 'kfc'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'Removing from Mods Folder'
    time.sleep(2)
    print 'Removing from Root'
    time.sleep(4)
    print 'KFC Uninstalled with No Errors'

## Cheese Cube Unlimited Uninstall

elif(args.remove_map_name == 'cheese_cube_unlimited'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'Removing from Mods Folder'
    time.sleep(2)
    print 'Removing from Root'
    time.sleep(4)
    print 'Cheese Cube Unlimited Uninstalled with No Errors'

## Cheese Cube Uninstall

elif(args.remove_map_name == 'cheese_cube'):
    print 'Removing Files/Scripts'
    time.sleep(2)
    print 'Removing from Mods Folder'
    time.sleep(2)
    print 'Removing from Root'
    time.sleep(4)
    print 'Cheese Cube Uninstalled with No Errors'

if(args.remove_mod_name == 'ugx_mod_1_0_4'):
    print 'Removing Files/Scripts'
    time.sleep(3)
    print 'Removing all .gsc files'
    time.sleep(2)
    raw_input('ARE YOU SURE YOU WANT TO CONTINUE THE UNINSTALATION? PRESS ENTER TO CONTINUE:')
    print 'Removing Prefabs'
    time.sleep(2)
    print 'UGX Mod 1.0.4 Removed'
elif(args.remove_mod_name == 'waw_modtools'):
    print 'Sorry. These mod development tools are unreversable. You will have to find another way to uninstall'
elif(args.remove_mod_name == 'black_ops_perks'):
    print 'Removing Files/Scripts'
    time.sleep(3)
    print 'Removing all .gsc files'
    time.sleep(2)
    raw_input('ARE YOU SURE YOU WANT TO CONTINUE WITH THE UNINSTALATION? PRESS ENTER TO CONTINUE:')
    print 'Removing Prefabs'
    time.sleep(2)
    print 'Black Ops Perk Mod Removed'
elif(args.remove_mod_name == 'black_ops_weapons'):
    print 'Removing Files/Scripts'
    time.sleep(3)
    print 'Removing all .gsc files'
    time.sleep(2)
    raw_input('ARE YOU SURE YOU WANT TO CONTINUE WITH THE UNINSTALATION? PRESS ENTER TO CONTINUE:')
    print 'Removing Prefabs'
    time.sleep(2)
    print 'Black Ops Weapons Mod Removed'





