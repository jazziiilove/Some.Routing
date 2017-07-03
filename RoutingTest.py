"""
 " " " " " " " " " " " " " " " " " " " " " " "
 " Assignment: Routing Search                "
 " Programmer: Baran Topal                   "
 " File name: RoutingTest.py                 "
 "                                           "      
 " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " "
 "	                                                                                         "
 "  LICENSE: This source file is subject to have the protection of GNU General               "
 "	Public License. You can distribute the code freely but storing this license information. "
 "	Contact Baran Topal if you have any questions. barantopal@barantopal.com                 "
 "	                                                                                         "
 " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " 
 """

#!/usr/bin/env python

# imports
import re
import fileinput

# class for handling the ops
class Routing:
    
    # global dictionary to keep the matching prefix and its corresponding price
    dRes = {}
    
    # global string to keep alpha free string
    cleaned = ""
    
    # constructor
    # not necessarily needed in this case
    def __init__(self):
        # member variables
        self.letter = None # to keep letter
        self.prefix = None # to keep prefix
        self.price = None # to keep price
    
    # display function to show the minimum price for matching prefix
    def display(self):
        print "Operator %c:" % self.letter
        print "Prefix: %d " % int (self.prefix)
        print "Price: %.2f " % float (self.price)
        print "**************************"
    
    # processing the per line values which are represented as a list
    def listProcess(self, list):
        # index to keep iteration
        y = 0            
        # matching letters are stored
        flist =[]        
        # length of cleaned user input
        cleanLen = len(self.cleaned)        
        # length of prefix
        listelementLen = len(list[0])    
        
        # loop for matching check
        for x in xrange(0, cleanLen):
            # if cleaned character is equal to prefix array value
            if (list[0][x] == self.cleaned[y]):
                # iterate for next character
                y += 1
                # append matching character to list
                flist.append(list[0][x])            
                # if prefix reached an end
                if(x == listelementLen - 1):
                    # list of character values are transformed to string
                    p = ''.join(flist)
                    # populate dictionary with prefix and price, list[1] denotes matching price
                    self.dRes[p] = list[1]                               
                    # hack to avoid index out of range for prefix since loop is for input
                    break
            else:
                # no match break
                break
            # none return for testing purpose
        return None
    
    # split incoming line
    def split(self, line):    
        list = line.split()
        # pass to listProcess
        self.listProcess(list)
    
    # clean user input
    def clean(self, userinput):
        # regular expression for digit check
        self.cleaned = re.sub(r'\D', "", userinput)        
    
    # longest matching element in dictionary
    def longestElement(self):    
        # checking longest key
        keyTempLength = 0
        keyTemp = ""    
        for key in self.dRes.keys():        
            if (len(key) > keyTempLength):
                keyTempLength = len(key)
                keyTemp = key
        #print "Longest key: ", keyTemp
        #print "Value: ", self.dRes[keyTemp]
        
        # assigning longest key and value
        self.prefix = keyTemp
        self.price = self.dRes[keyTemp]
    
    # file process
    def process(self, line):
        # if not starts with alpha
        if(not line.startswith('Operator')):
            # split the line for numerics
            self.split(line)
        # line is alpha
        else:        
            # retrieve letter
            self.letter = line[-2]
            
            # check longest element in matching keys
            self.longestElement()
            
            # display longest element with its value
            self.display()
            
            # prepare for incoming operator values
            self.dRes = {}