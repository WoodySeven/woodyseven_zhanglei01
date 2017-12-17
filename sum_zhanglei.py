#!/usr/bin/env python
""" 
@author:Administrator 
@file: hello.py 
@time: 2017/12/16 
"""  
from lib.utils import print_sum


# def print_sum(a,n,sum=0):
#     while a<=n:
#         sum=sum+a
#         a=a+1
#     return sum
#

if __name__=="__main__":
    print("求x至y的两个数之间所有自然数的和？")
    x=int(input("请输入一个数x："))
    y=int(input("请输入一个比x大的数y："))
    print(print_sum(x,y))