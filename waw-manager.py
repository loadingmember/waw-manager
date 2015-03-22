#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='World at War Manager')

parser.add_argument('-v','--version', help='Print Version', action='version', version='1.0-SNAPSHOT')
parser.add_argument('-i','--install', help='Install new mod', action='store', dest='mod_location', required=False)
parser.add_argument('-u','--uninstall', help='Uninstall mod', action='store', dest='mod_name', required=False)

args = parser.parse_args()

if(args.mod_location):
   print 'mod_location=' + args.mod_location

if(args.mod_name):   
   print 'mod_name=' + args.mod_name
