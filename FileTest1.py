#!/usr/bin/env python
# encoding:utf-8
'''
@author:Kevin
@contact:kevin-li@yeah.net
@file:FileTest1.py
@time:2018/11/16/016 09:43
@desc:
'''

import os

'''
myFiles=['accounts.txt','details.csv','invite.docx']

for filename in myFiles:
    print(os.path.join('C:\\User\kkmm',filename))
'''
'''
print('\n说明：os.getcwd()\n 获取当前工作目录')
print(os.getcwd())     #os.getcwd() 获取当前工作目录


print('\n说明：os.chdir(\'D:\\VMware\') \n改变当前工作目录至D:\VMware')
os.chdir('D:\\VMware')   #os.chdir('D:\\VMware') 改变当前工作目录
print(os.getcwd())

print('\n说明：os.makedirs(\'D:\\Pyprojects\\FilesWR\\test2\')\n创建新文件夹,若已经存在则报错')
os.makedirs('D:\\Pyprojects\\FilesWR\\test2')
'''

print('\n说明：os.path.abspath(\'.\') \n返回参数的绝对路径的字符串')
print(os.path.abspath('.'))
print(os.path.abspath('.\\venv'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('C:\\Windows', 'C:\\'))
print(os.path.relpath('D:\\VMware\\share', 'D:\\VMware'))
print(os.path.relpath('D:\\VMware\\share'))
