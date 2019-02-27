#!/usr/bin/env python
# encoding:utf-8
'''
@author:Kevin
@contact:kevin-li@yeah.net
@file:GetFilesSize.py
@time:2018/11/19/019 16:08
@desc:
get the files Size
'''

import os
print('Please input the Directory:\nLike: C:\\\\ABC\\\\DEF')
fileDict = input()

totalSize = 0

for filename in os.listdir(fileDict):
    totalSize = totalSize + os.path.getsize(os.path.join(fileDict, filename))

print('TotalSize =',totalSize)
