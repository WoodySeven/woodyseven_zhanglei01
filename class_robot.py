#!/usr/bin/env python  
""" 
@author:Administrator 
@file: class_robot.py 
@time: 2017/12/17 
"""



class Robot(object):
    population=0


    def __init__(self,name,age):
        self.name=name
        self.age=age
        Robot.population=Robot.population+1

    def speak(self):
        print("{}can speak! It's {} year old".format(self.name,self.age))

    def walk(self):
        print("%s can walk" % self.name)

    @classmethod
    def how_many_robot(cls):
        if Robot.population>=0:
            print("We have %s robot." % Robot.population)
        else:
            print("Sorry,we have no robot.")

    def die(self):
        print("%s is %s ,It's dead." % (self.name,self.age))
        Robot.population=Robot.population-1
        if Robot.population==0:
            print("This is the last Robot!")
        elif Robot.population>0:
            print("We also have {} robot.".format(Robot.population))
        else:
            print("Our robot is die up!")



if __name__=="__main__":
    robot1=Robot("Xiaoming",18)
    #robot2=Robot("Xiaohua",19)
    robot1.speak()
    robot1.walk()
    Robot.how_many_robot()
    robot1.die()
    #robot1.die()
    Robot.how_many_robot()