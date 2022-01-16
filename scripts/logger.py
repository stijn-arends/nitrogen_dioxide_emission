#!/usr/bin/env python3

# IMPORTS
import sys
import logging
import datetime
from functools import wraps
from pathlib import Path


def make_dir(folder):
    """
    Create a directory (if it does not exisit yet) to store log files.

    :Excepts
    --------
    FileExistsError
        The directory already exists
    """
    try:
        folder.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print(f"[{create_logger.__name__}] Folder is already there.")


def create_logger(file_name):
    """
    Create a logger object.

    :parameters
    -----------
    file_name - String
        Name of the log file 

    :returns
    --------
    logger - Logger
        Logger object

    :see also
    ---------
    make_dir(folder)
    log(logger)
    """ 
    #create a logger object
    logger = logging.getLogger('logger')
    logger.setLevel(logging.INFO)
      
    #create a file to store all the 
    # logged exceptions
    folder = Path.cwd() / 'logs/'

    make_dir(folder) # Create a folder for the log file

    logfile = logging.FileHandler(folder / file_name) # Create the log file
      
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s' # Set format
    formatter = logging.Formatter(fmt)
      
    logfile.setFormatter(formatter)
    logger.addHandler(logfile)
      
    return logger

def log(logger):
    """
    Base function for the decorator.
    Log basic information about a function plus the catched exceptions
    into a log file.

    :parameters
    -----------
    logger - Logger
        Logging object
    """
    def decorator(func):
          
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Store information about the function that is being run and 
            log it into a log file. Also catch the exceptions that might 
            occure and write them to the log file aswell. 
            """
            start = datetime.datetime.now()
            fun_name = func.__name__
            end = datetime.datetime.now()
              
            try:
                text = "no exceptions raised."
                text += """
                Function: {}
                Execution time: {}
                Adress: {}
                Memory: {} bytes
                Date: {}
                """.format(fun_name, end-start, func.__name__,
                sys.getsizeof(func), start)
                logger.info(text)
                return func(*args, **kwargs)
                
            except:
                issue = "exception in "+func.__name__+"\n"
                issue = issue+"-------------------------\
                ------------------------------------------------\n"
                logger.exception(issue)
            raise Exception
               
        return wrapper
    return decorator