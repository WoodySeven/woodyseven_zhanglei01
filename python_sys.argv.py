#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:Administrator 
@file: python_sys.argv.py 
@time: 2017/12/18 
""" 
import os
import sys


def usage():
    print("文件获取两个参数，请重新输入：")
    print("eg:python python_sys.argv.py zhanglei 18")

def sys_argv(fname,uname,age):
    print("传入的文件名是：{0},用户名是：{1},年龄是：{2}".format(fname,uname,age))


if __name__ == "__main__":
    if (len(sys.argv)!=3):
        usage()
        parm = sys.argv
        fname, uname, age = parm[1],parm[2],parm[3]
        sys_argv(fname, uname, age)