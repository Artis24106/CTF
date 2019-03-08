# 2-1

## 題目
從`misc4.png`中找出flag

## Write-Up
用`xxd misc4.png | less`發現PNG文件頭跟width有錯誤（width不可為0）

```
00000000: 8059 4e47 0d0a 1a0a 0000 000d 4948 4452  .YNG........IHDR
00000010: 0000 0000 0000 02f8 0806 0000 0093 2f8a  ............../.
00000020: 6b00 0000 0467 414d 4100 009c 4020 0de4  k....gAMA...@ ..
00000030: cb00 0000 2063 4852 4d00 0087 0f00 008c  .... cHRM.......
...
```

---

首先處理width問題：

png的數據塊(Chunk)由Length(4 bytes), Chunk Type Code(4 bytes), Chunk Data(Length bytes), CRC(4 bytes)四個部分組成，而width存在IHDR裡面。

> CRC = Cyclic Redundancy Check 循環冗餘校驗

CRC 用來檢查資料有沒有被更動過。png數據塊中的CRC是由Chunk Type Code跟Chunk Data採CRC-32計算得到的。

因此不斷猜測width長度並計算CRC，直到與IHDR的CRC相同（即0x932f8a6b）。使用`python3 findWidth.py`。
```
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
```
得知width為709

---

再來將PNG文件頭跟width復原。

> PNG文件頭固定為： 89 50 4E 47 0D 0A 1A 0A

使用`python3 modifyFile.py`

```
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
```
打開`final.png`即可看到flag

> wdflag{Png_C2c_u_kn0W}