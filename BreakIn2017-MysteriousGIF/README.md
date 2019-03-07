# Mysterious GIF

## 題目
從一張[神奇的gif](https://drive.google.com/file/d/0Bw-aSVx60ZiOU1h6QWRqMkNfOVU/view)中找出flag

## Write-Up
```=shell
binwalk Question.gif
```
得到：
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             GIF image data, version "89a", 440 x 608
2670386       0x28BF32        Zip archive data, at least v1.0 to extract, compressed size: 112890, uncompressed size: 112890, name: temp.zip
2783320       0x2A7858        End of Zip archive
2783420       0x2A78BC        End of Zip archive
```

