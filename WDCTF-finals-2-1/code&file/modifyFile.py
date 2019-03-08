#!/usr/bin/python
# coding=utf-8
import struct
import binascii

filename = "misc4.png"
outputFile = "final.png"
f = open(filename, "rb+").read()
o = open(outputFile, "wb")

# 用正確的PNG文件頭取代原本的，更改圖片寬度，最後輸出output.png
o.write(binascii.unhexlify('89504e470d0a1a0a') +
        f[8:16] + struct.pack(">L", 709) + f[20:])
