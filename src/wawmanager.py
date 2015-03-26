#!/usr/bin/python

import argparse
import subprocess
import time
from Status import Status
from List import List
from installs.maps.ZombieCargo import ZombieCargo
from installs.maps.ZombieSlums import ZombieSlums
from installs.maps.TMGChristmas import TMGChristmas
from installs.maps.PurpleDimension import PurpleDimension
from installs.maps.Survivedabox import Survivedabox
from installs.maps.Cryogenic import Cryogenic
from installs.maps.OneWindow import OneWindow
from installs.maps.ProjectViking import ProjectViking
from installs.maps.Kfc import Kfc
from installs.maps.CheeseCube import CheeseCube
from installs.maps.CheeseCubeUnlimited import CheeseCubeUnlimited
from installs.mods.Ugx104 import Ugx104
from installs.mods.WawModtools import WawModtools
from installs.mods.BlackopsPerks import BlackopsPerks
from installs.mods.BlackopsWeapons import BlackopsWeapons
from installs.mods.ScaretimesScripts import ScaretimesScripts



parser = argparse.ArgumentParser(description='World at War Mod Manager 1.5')

parser.add_argument('-v','--version', help='Print Version', action='version', version='WaW Mod Manager Version 1.3')
parser.add_argument('-i','--install', help='Install new map', action='store', dest='arg_map', required=False)
parser.add_argument('-m', '--installmod', help='Installs mod', action='store', dest='arg_mod', required=False)
parser.add_argument('-rmap','--uninstallmap', help='Uninstall map', action='store', dest='remove_map_name', required=False)
parser.add_argument('-s', '--status', help='Displays the WaW Status', action='store_true', dest='status', required=False)
parser.add_argument('-l', '--list', help='Show a List of Installable Maps and Mods', action='store_true', dest='list', required=False)
parser.add_argument('-a', '--addmap', help='Adds a map or mod', action='store', dest='user_map_name', required=False)

args = parser.parse_args()

## Prints the user_map_name
if(args.user_map_name):
    print args.user_map_name + "added to our directory"

if(args.list):
    list = List()
    list.print_list()

if(args.status):
    status = Status()
    status.display_status()    

if(args.arg_mod == 'ugx_mod_1_0_4'):
    ugx = Ugx104('UGX Mod 1.0.4', 'http://www.ugx-mods.com', 'http://ugx-mods.com/forum/index.php?topic=537.0')
    ugx.install()

elif(args.arg_mod == 'waw_modtools'):
    wawmodtools = WawModtools('WaW Modtools', 'http://www.callofduty.gamefront.com/', 'http://callofduty.filefront.com/file/;95890')
    wawmodtools.install()

elif(args.arg_mod == 'black_ops_perks'):
    blackopsperks = BlackopsPerks('Black Ops Perks', 'http://www.mediafire.com', 'http://www.mediafire.com/download/nnsc6xfqewrn9qo/update_1.zip')
    blackopsperks.install()

elif(args.arg_mod == 'black_ops_weapons'):
    blackopsweapons = BlackopsWeapons('Black Ops Weapons for WaW', 'Not Found', 'Not Found')
    blackopsweapons.install()

elif(args.arg_mod == 'scaretimes_scripts'):
    scaretimes_scripts = ScaretimesScripts('Scaretimes Scripts and Prefabs', 'None', 'None')
    scaretimes_scripts.install()

## Map Installs Below


## Zombie Cargo
if(args.arg_map == 'zombie_cargo'):
    zombie_cargo = ZombieCargo('Zombie Cargo', 'http://www.ugx-mods.com', 'http://ugx-mods.com/forum/index.php?topic=5645.0')
    zombie_cargo.install()

## Zombie Slums

elif(args.arg_map == 'zombie_slums'):
    zombie_slums = ZombieSlums('Zombie Slums', 'http://www.zombiemodding.com', 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1661')
    zombie_slums.install()

## TMG Christmas 1.1

elif(args.arg_map == 'tmg_christmas1.1'):
    tmg_christmas = TMGChristmas('TMG Christmas 1.1', 'http://www.zommods.com', 'http://zommods.com/tmg-christmas/')
    tmg_christmas.install()

## Purple Dimension

elif(args.arg_map == 'purple_dimension'):
    purple_dimension = PurpleDimension('Purple Dimension', 'http://www.zombiemodding.com', 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1771')
    purple_dimension.install()

## survivedabox

elif(args.arg_map == 'survivedabox'):
    survivedabox = Survivedabox('survivedabox', 'http://www.zombiemodding.com/', 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1819')
    survivedabox.install()

## Cryogenic 

elif(args.arg_map == 'cryogenic'):
    cryogenic = Cryogenic('Cryogenic', 'http://www.ugx-mods.com', 'http://ugx-mods.com/forum/index.php?topic=5860.0')
    cryogenic.install()

## One Window Challange

elif(args.arg_map == 'one_window_challange'):
    one_window = OneWindow('One Window Challange', 'http://www.zommods.com/', 'http://www.zommods.com/zm_one-window-challenge/')
    one_window.install()

## Project Viking

elif(args.arg_map == 'project_viking'):
    project_viking = ProjectViking('Project Viking Beta 1.0.2', 'http://www.ugx-mods.com', 'http://ugx-mods.com/forum/index.php?topic=1620.0')
    project_viking.install()

## KFC

elif(args.arg_map == 'kfc'):
    kfc = Kfc('Zombie KFC', 'http://www.zombiemodding.com/', 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1837')
    kfc.install()

## Cheese Cube Unlimited 

elif(args.arg_map == 'cheese_cube_unlimited'):
    cheese_cube_unlimited = CheeseCubeUnlimited('Cheese Cube Unlimited', 'http://www.ugx-mods.com/', 'http://ugx-mods.com/forum/index.php?topic=2973.0')
    cheese_cube_unlimited.install()

## Cheese Cube Standard

elif(args.arg_map == 'cheese_cube'):
    cheese_cube = CheeseCube('Cheese Cube', 'http://www.zombiemodding.com', 'http://www.zombiemodding.com/index.php?action=downloads;sa=view;down=1390')
    cheese_cube.install()
    

## Map Removes #########################################################################################################################

elif(args.remove_map_name == 'zombie_cargo'):
   zombie_cargo.uninstall()

## Zombie Slums Uninstall

elif(args.remove_map_name == 'zombie_slums'):
    zombie_slums.uninstall()

## TMG Christmas 1.1 Uninstall

elif(args.remove_map_name == 'tmg_christmas1.1'):
   tmg_christmas.uninstall()

## Purple Dimension Uninstall

elif(args.remove_map_name == 'purple_dimension'):
    purple_dimension.uninstall()

## survivedabox uninstall

elif(args.remove_map_name == 'survivedabox'):
    survivedabox.uninstall()

## Cryogenic Unistall

elif(args.remove_map_name == 'cryogenic'):
    cryogenic.uninstall()

## One Window Challange Uninstall

elif(args.remove_map_name == 'one_window_challange'):
   one_window.uninstall()

## Project Viking 1.0.2 Beta Uninstall

elif(args.remove_map_name == 'project_viking1.0.2_beta'):
    project_viking.uninstall()

## KFC Uninstall

elif(args.remove_map_name == 'kfc'):
    kfc.uninstall()

## Cheese Cube Unlimited Uninstall

elif(args.remove_map_name == 'cheese_cube_unlimited'):
    cheese_cube_unlimited.uninstall()

## Cheese Cube Uninstall

elif(args.remove_map_name == 'cheese_cube'):
    cheese_cube.uninstall()






