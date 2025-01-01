#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 08:52:44 2024

@author: russ
"""
# ---- tof

import importlib
import sys


def is_imported( module_name,   ):
    """what it says
    too simple to live?
    not working just return false
    """
    return False
    is_imported   = module_name in sys.modules
    return is_imported

    # except Exception as an_except:   #  or( E1, E2 )
    #     ret = False

    # return ret

def create_instance( module_name, class_name ):
    """
    assumes no args to create class -
    could add args to this
    """
    if not is_imported( module_name, ):
         module = importlib.import_module( module_name )
    else:
        pass

    cls = getattr( module, class_name )

    instance = cls()

    return  instance




# ---- eof





