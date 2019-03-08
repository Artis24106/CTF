#!/usr/bin/python
# coding=utf-8
import binascii
import struct
import sys

filename = "misc4.png"
f = open(filename, "rb+").read()

# 從0~1023檢查哪一個長度能符合CRC
for i in range(1024):
    temp = f[12:16] + struct.pack(">i", i) + f[20:29]
    crc32 = binascii.crc32(temp) & 0xffffffff
    if crc32 == 0x932f8a6b:
        print(i)
        sys.exit()
