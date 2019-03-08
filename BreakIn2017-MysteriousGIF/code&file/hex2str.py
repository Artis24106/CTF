#!/usr/bin/python
# coding = UTF-8
import codecs

files = open("data.txt", "r")
output = open("key.txt", "w+")

for f in files:
    output.write(codecs.decode(f.strip(), 'hex').decode('utf-8') + '\n')

files.close()
output.close()
