#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
needs import and
call to init

import app_logging
app_logging.init( )

my_logging   = app_logging.APP_LOGGING
my_logging.what(0)

sets up glogal lobbing

depends on parmetes being set up first
        and appGlobal



"""


# ---- tof

# ---- imports
import logging
import traceback
import sys

from app_global import AppGlobal
import parameters
# ---- end imports
#global APP_LOGGING
APP_LOGGING   = None

#-------------------------------

PARAMETERS   = parameters.PARAMETERS

if not PARAMETERS:
    1/0    # set up parameters first

class AppLogging( ):

    def __init__(self ):
        """ """
        self.config_logger( )


    def config_logger(self):
        """
        Configure the Python logger to allow logging from other modules.
        """
        log_file_name   = PARAMETERS.pylogging_fn  # File to log messages
        log_mode        = PARAMETERS.log_mode
        log_level       = PARAMETERS.logging_level

        try:
            # Configure the ROOT LOGGER (so other modules can use it)
            root_logger = logging.getLogger()  # Get root logger
            root_logger.setLevel( log_level )

            # Remove existing handlers to prevent duplicates
            if root_logger.hasHandlers():
                root_logger.handlers.clear()

            # Create file handler (overwrites or appends based on mode)
            file_handler = logging.FileHandler(log_file_name, mode = log_mode )
            file_handler.setLevel( log_level )
            file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

            # Create console handler
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel( log_level )
            console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

            # Add handlers to root logger
            root_logger.addHandler(file_handler)
            root_logger.addHandler(console_handler)

        except Exception as e:
            print("Exception occurred setting up logger:")
            traceback.print_exc()

        logger          = logging.getLogger( )
        AppGlobal.set_logger( logger )
        self.logger      = logger

        # Example log from the root logger
        logging.critical("Root logger is set up. Modules can now log using logging.getLogger().")
        logging.info("config_logger call was: logging.info")

        # Example logs and test
        self.logger.critical("config_logger call was logger.critical()")
        self.logger.critical(f"config_logger {log_file_name = } ========================================= ")
        self.logger.log(22, "config_logger This is a 22 message from my_logger.")
        self.logger.debug("config_logger call was: logging.debug")
        self.logger.info("config_logger call was: logging.info")


    def test_logingr(self):
        """ """
        pass

    # ----------------------------------------------
    def os_open_log_file( self,  ):
        """
        have function since want flush

        """
        self.log_file_handler.flush()  # Manually flushing

        AppGlobal.os_open_txt_file( self.parameters.pylogging_fn )


    # ------------------------------------------
    def close_logger( self, ):
        """
        not tested after other changes
        """
        logger  = AppGlobal.logger
        for a_handler in logger.handlers:
            a_handler.close()

def  init( ):
    global APP_LOGGING
    if not APP_LOGGING:
        APP_LOGGING = AppLogging( )


# ---- eof
