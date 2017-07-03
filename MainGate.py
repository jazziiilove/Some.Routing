"""
 " " " " " " " " " " " " " " " " " " " " " " "
 " Assignment: Routing Search                "
 " Programmer: Baran Topal                   "
 " File name: Routing.py                     "
 "                                           "      
 " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " "
 "	                                                                                         "
 "  LICENSE: This source file is subject to have the protection of GNU General                   "
 "	Public License. You can distribute the code freely but storing this license information. "
 "	Contact Baran Topal if you have any questions. barantopal@barantopal.com                 "
 "	                                                                                         "
 " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " 
 """
 
#!/usr/bin/env python

# imports
import fileinput
from Routing import Routing

# main gate of the program
routing = Routing()

# uncomment for user input
#var = raw_input("Enter the alphanumeric input: ")
#print "You entered ", var

var = "+46-73-212"

# clean the input
routing.clean(var)

# reverse reading the file
for line in reversed(open("List.txt").readlines()):
    # process each line
    routing.process(line.rstrip())