"""
 " " " " " " " " " " " " " " " " " " " " " " "
 " Assignment: Routing Search                "
 " Programmer: Baran Topal                   "
 " File name: TestGate.py                    "
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

import unittest
from Routing import Routing
        
# Here's our "unit tests".
class IsOddTests(unittest.TestCase):


    # comparing cleaned user input with expected input
    def testClean(self):    
        r = Routing()    
        input = "+46-73-212"
        r.clean(input)
        expected = 4673212
        actual = r.cleaned
        self.failUnlessEqual(int (expected), int (actual))
    
    #...I may continue

def main():
    unittest.main()

if __name__ == '__main__':
    main()
