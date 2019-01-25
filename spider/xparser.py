#!/usr/bin/env python
import re
from .commtype import *

def findone(match, string):
    match_t = type(match)

    if match_t == srematchtype:
        res = match.search(string)
        if res : 
            return res.group()


    elif match_t == strtype:
        if match == "":
            return string
        return findone(re.compile(match), string)

    elif match_t == functiontype:
        return match(string);

    elif match_t == listtype:
        for amatch in match:
            string = findone(amatch, string)
        return string

