#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:34:13 2024

@author: russ


import adjust.path
"""
# ---- imports

import sys
import os
import socket

# adjust according to where I am -- in progress
hostname              = socket.gethostname()
cwd                   = os.getcwd()
me                    = __file__




if   hostname == "russ-ThinkPad-P72":
    src_root         = "/mnt/WIN_D/russ/0000/python00/python3"
elif hostname == "russ-ThinkPad-P72":
    src_root         = "/mnt/WIN_D/russ/0000/python00/python3"
else:
    src_root         = "/mnt/WIN_D/russ/0000/python00/python3"

#src_root         = r"d:\russ\0000\python00\python3"


# sys.path.append( r"D:\Russ\0000\python00\python3\_projects\rshlib"  )
# sys.path.append( "../")
#sys.path.insert( 1, "../rshlib" )
#sys.path.insert( 1, "./ex_qt" )

#comp_root        = "/mnt/WIN_D/russ/0000/python00/"
#src_root         = "/mnt/WIN_D/russ/0000/python00/python3"
py3_root         = src_root
proj_root        = f"{py3_root}/_projects"
ex_root          = f"{py3_root}/_examples"

# least important at top
sys.path.insert( 1, f"./libs" )                # libs for github repo
sys.path.insert( 1, f"./tabs" )                # tab for github repo
sys.path.insert( 1, f"{proj_root}/rshlib" )
sys.path.insert( 1, f"{src_root}/_projects/rshlib/test/"  )
sys.path.insert( 1, f"{src_root}/_projects/rshlib/rshlib_qt/" )
sys.path.insert( 1, f"{src_root}/_projects/rshlib/app_services/" )


sys.path.insert( 1, f"{src_root}/_projects/rshlib/in_spect" )
sys.path.insert( 1, f"{src_root}/_projects/rshlib/app_services" )

sys.path.insert( 1, f"{src_root}/_examples" )

sys.path.insert( 1, f"{src_root}/_projects/stuffdb" )
sys.path.insert( 1, f"{src_root}/_projects/stuffdb/qt_tabs" )
sys.path.insert( 1, f"{src_root}/_projects/qt5_by_example/tabs"  )
# /mnt/WIN_D/russ/0000/python00/python3/_projects/qt5_by_example/tabs/

sys.path.insert( 1, f"{src_root}/_projects/stuffdb/data_dict_src" )
#/mnt/WIN_D/Russ/0000/python00/python3/_projects/qt5_by_example
# /mnt/WIN_D/Russ/0000/python00/python3/_projects/qt_by_example

sys.path.insert( 1, f"{src_root}/_projects/qt5_by_example/info_about_src" )
sys.path.insert( 1, f"{src_root}/_projects/qt5_by_example" )
#sys.path.insert( 1, f"{src_root}/_projects/qt5_by_example" )


# print( "your path has been adjusted fron qt5_by_example on theProf Mint from qt5_by_example" )
# for i_path in sys.path:
#     print( f"{i_path = }")

print( "end your path has been adjusted " )

pass   # for debug



# --- eof