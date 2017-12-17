#!/usr/bin/env python  
""" 
@author:Administrator 
@file: read_write_file1.py
@time: 2017/12/16 
"""
import pickle


def read_file():
    # fp=open("read.txt","rb")
    # #print(fp.readlines())
    # content=fp.readlines()
    # print(content)
    # for i in content:
    #     print(i.decode("utf-8").strip())
    # fp.close()
    with open("read.txt","rb") as fp:
        print(fp.readlines())
        fp.seek(0)#读取两次文件，指针需要设置到文件开头
        content = fp.readlines()
        print(content)
        for i in content:
            print(i.decode("utf-8").strip())


def write_file():
    fp=open("write.txt","wb")#会自动创建文件
    add=["中国","非洲","朝鲜"]
    for i in add:
        fp.write(i.encode("utf-8")+b'\n') #换行要byte转换
        #fp.write('{}\n'.format(i).encode("utf-8"))
    fp.close()


def write_pickle():
    """将对象写进文件中去"""
    dict1={"name":"sam","age":16}
    # fp = open("write_pickle.txt","wb")
    # pickle.dump(dict1,fp)
    # fp.close()
    with open("write_pickle.txt","wb") as fp:
        pickle.dump(dict1,fp)


def read_pickle():
    """读取文件中的对象信息"""
    fp=open("write_pickle.txt","rb")
    dict1=pickle.load(fp)
    print(dict1)
    fp.close()


if __name__ == "__main__":
    #read_file()
    #write_file()
    #write_pickle()
    read_pickle()