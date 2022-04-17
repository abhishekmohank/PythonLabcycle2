""" **4. Write a program to create a class Box with data members length,
breadth, height, area, and volume. Provider constructor that enables
initialization with one parameter (for cube), two parameters (for
square prism) three parameters (rectangular prism). Also, provide
functions to calculate area and volume.
Create a list of N boxes with random measurements and print the
details of the box with maximum volume: area ratio**
"""

import random

class Box:
  def __init__(self,*args):
    #if all arguements are same,cube prism is initialised.
    if (args[0]==args[1]==args[2]):
      self.__length = args[0]
      self.__breadth = args[0]
      self.__height = args[0]
    #if any two arguements are same, the square prism is initialised
    elif (args[0]==args[1] or args[1]==args[2] or args[0]==args[2]):
      if (args[0]==args[1]):
        self.__length = args[0]
        self.__breadth = args[0]
        self.__height = args[1]
      elif (args[1]==args[2]):
        self.__length = args[1]
        self.__breadth = args[1]
        self.__height = args[0]
      elif (args[0]==args[2]):
        self.__length = args[0]
        self.__breadth = args[0]
        self.__height = args[1]       
    #if three arguements are different , rectangular prism is initialised.
    else:
      self.__length = args[0]
      self.__breadth = args[1]
      self.__height = args[2]

  #funtion to calculate area
  def calc_area(self):
    self.__area = self.__length*self.__breadth
    return self.__area
  #funtion to calculate volume
  def calc_volume(self):
    self.__volume = self.__length*self.__breadth*self.__height
    return self.__volume
  #funtion to print area
  def display_area(self):
    print("The area is ",self.__area)
  #funtion to print volume
  def display_volume(self):
    print("The volume is ",self.__volume,"\n")


N = 10
box = [Box(random.randint(1,1000),random.randint(1,1000),random.randint(1,1000)) for i in range(N)]
area = [i.calc_area() for i in box]
volume = [i.calc_volume() for i in box]
ratio = [x//y for x,y in zip(volume,area)]
index = ratio.index(max(ratio))
print("Box with Maximum Volume:Area ratio")
print("Area = ",area[index])
print("Volume = ",volume[index])
print("Ratio = ",max(ratio))
