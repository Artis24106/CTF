#!/usr/bin/python
# coding=utf-8
import itertools
import os

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in itertools.product(alphabet, repeat=2):
    iname = 'part' + ''.join(i) + '.enc'
    oname = 'part2' + ''.join(i) + '.enc'
    if os.path.isfile(iname):
        os.system("openssl rsautl -decrypt -inkey key.pem -in " +
                  iname + " -out " + oname)
