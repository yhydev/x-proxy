#!/usr/bin/env python
import re

def findone(match, string):


    if isinstance(match, str):
        if match == "":
            return string
        res = re.search(match, string)
        if res == None:
            return string
        return res.group()


    elif callable(match):
        return match(string);

    elif isinstance(match, list):
        for amatch in match:
            string = findone(amatch, string)
        return string

