#!/usr/bin/env python
import ReParser
import re


mstr = "([1|2]?[1-9]?\d\.){3}[1|2]?[1-9]?\d"
string = '192.168.11.1sd0394334,asdf'

res = re.search(mstr, string)
print(res)

res = ReParser.findone(mstr, string)
print(res)

res = ReParser.findone([re.compile(mstr), '\d'], string)
print(res)
