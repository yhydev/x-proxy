#!/usr/bin/env python
import logging


def getlogger(name, filename = None, level = logging.INFO, filemode = "a"):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if filename != None:
        handler = logging.FileHandler(filename, mode = filemode)
        logger.addHandler(handler)
    return logger


debug = getlogger("debug", "debug.log", level = logging.DEBUG, filemode = "a").debug 
info = getlogger("info", "info.log", level = logging.INFO, filemode = "a") .info
warning = getlogger("warning", "warning.log", level = logging.WARNING, filemode = "a").warning
error = getlogger("error", "error.log", level = logging.ERROR, filemode = "a").error
