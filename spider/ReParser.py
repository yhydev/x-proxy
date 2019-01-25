#!/usr/bin/env python
import re, commtype

def findone(match, string):
    match_t = type(match)
    if match_t == commtype.srematchtype:
        res = match.search(string)
        if res : 
            return res.group()
    elif match_t == commtype.strtype:
        if match == "":
            return string
        return findone(re.compile(match), string)

    elif match_t == commtype.listtype:
        for amatch in match:
            string = findone(amatch, string)
        return string

