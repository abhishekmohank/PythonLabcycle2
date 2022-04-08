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
    if len(args) == 1:
      self.__length = args[0]
      self.__breadth = args[0]
      self.__height = args[0]
    
    elif len(args) == 2:
      self.__length = args[0]
      self.__breadth = args[0]
      self.__height = args[1]
    
    else:
      self.__length = args[0]
      self.__breadth = args[1]
      self.__height = args[2]

  def calc_area(self):
    self.__area = self.__length*self.__breadth
    return self.__area
  
  def calc_volume(self):
    self.__volume = self.__length*self.__breadth*self.__height
    return self.__volume
  
  def display_area(self):
    print("The area is ",self.__area)
  
  def display_volume(self):
    print("The volume is ",self.__volume,"\n")

ratio = []

cube_dimension = []
cube_dimension.append(random.randint(1,1000))
print("Cube Prism - Dimension" , end = " ")
print(cube_dimension)

cube_prism = Box(cube_dimension[0])
area1=cube_prism.calc_area()
volume1=cube_prism.calc_volume()
cube_prism.display_area()
cube_prism.display_volume()

ratio.append((volume1/area1))

square_dimension = []
for i in range(2):
  square_dimension.append(random.randint(1,1000))
print("Square Prism - Dimension" , end = " ")
print(square_dimension)

square_prism = Box(square_dimension[0],square_dimension[1])
area2=square_prism.calc_area()
volume2=square_prism.calc_volume()
square_prism.display_area()
square_prism.display_volume()

ratio.append((volume2/area2))

rectangular_dimension = []
for i in range(3):
  rectangular_dimension.append(random.randint(1,1000))

print("Rectangular Prism - Dimension" , end = " ")
print(rectangular_dimension)
rectangular_prism = Box(rectangular_dimension[0],rectangular_dimension[1],rectangular_dimension[2])
area3 = rectangular_prism.calc_area()
volume3 = rectangular_prism.calc_volume()
rectangular_prism.display_area()
rectangular_prism.display_volume()

ratio.append((volume3/area3))

index = ratio.index(max(ratio))

if index == 0:
  print("Cube Prism with Maximum Volume : Area - ", end=" ")
  print(cube_dimension)
elif index == 1:
  print("Square Prism with Maximum Volume : Area - " , end=" ")
  print(square_dimension)
else:
  print("Rectangular Prism with Maximum Volume : Area - ", end=" ")
  print(rectangular_dimension)
