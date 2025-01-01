#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:52:48 2024

@author: russ
"""


import adjust_path


import info_about


#my_info_about     = info_about.InfoAbout()


print( f"{info_about.INFO_ABOUT =}")

#info_about.INFO_ABOUT
import info_about
FIF       = info_about.INFO_ABOUT.find_info_for(

    )
print( info_about.INFO_ABOUT.info_provider_list )

print( FIF( [1,2,3,4], msg = "a list with FIF") )

print( "try to get info ---------------------------------")

print( info_about.INFO_ABOUT.find_info_for( [1,2,3,4], msg = "a list") )


print( FIF( " 1,2,3,4 " , msg = "a string with FIF") )