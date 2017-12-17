#!/usr/bin/env python
""" 
@author:Administrator 
@file: utils.py 
@time: 2017/12/16 
"""


def print_sum(a,n,):
    sum = 0
    if a>n:
        return None
    while a<=n:
        sum=sum+a
        a=a+1
    return sum


if __name__=="__main__":
    print(print_sum(10, 1))
    print(print_sum(1, 10))