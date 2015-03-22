#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='World at War Mod Manager 1.0')

parser.add_argument('-v','--version', help='Print Version', action='version', version='WaW Mod Manager Version 1.0')
parser.add_argument('-i','--install', help='Install new map', action='store', dest='mods', required=False)
parser.add_argument('-m', '--installmodtools', help='Installs the WaW Mod Tools', action='store', dest='modtools_location', required=False)
parser.add_argument('-u','--uninstall', help='Uninstall map', action='store', dest='mod_name', required=False)

args = parser.parse_args()

if(args.map_location):
   print 'map_location=ProgramFilesx86'

if(args.map_name):
   print 'map_name=' + args.map_name


