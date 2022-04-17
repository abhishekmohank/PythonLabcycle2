"""    **5. Write a program to create a parent class, 3DShapes, with methods
printVolume() and printArea(), which prints the Volume and Area,
respectively. Create classes Cylinder and Sphere by inheriting
3DShapes class. Using these child classes, calculate and print the
volume and area of a cylinder and sphere.**

"""

#base - class 
class threeD_Shapes:
  def printVolume(self):
    print("The Volume is ",round(self._volume,3))
  def printArea(self):
    print("The Area is ",round(self._area,3))
  
#derived class - for calculation of area and volume of cylinder
class cylinder(threeD_Shapes):
  #initialisation using constructor
  def __init__(self,r,h):
    self.__radius = r
    self.__height = h
  def calc_area(self):
    self._area = 2*3.14*self.__radius*(self.__radius+self.__height)
  def calc_volume(self):
    self._volume = round((3.14*self.__radius*self.__radius*self.__height),2)

#derived class - for calculation of area and volume of sphere
class sphere(threeD_Shapes):
    #initialisation using constructor
    def __init__(self,r):
      self.__radius = r
    def calc_area(self):
      self._area = 4*3.14*self.__radius*self.__radius
    def calc_volume(self):
      self._volume = round(((4/3)*3.14*(self.__radius**3)),2)

#object of class cylinder for calculating the area and volume of cylinder
cyl_obj = cylinder(int(input("Enter the radius of the cylinder ")),int(input("Enter the height of the cylinder ")))
cyl_obj.calc_area()
cyl_obj.printArea()
cyl_obj.calc_volume()
cyl_obj.printVolume()

#object of class sphere for calculating the area and volume of sphere
sph_obj = sphere(int(input("\nEnter the radius of the sphere ")))
sph_obj.calc_area()
sph_obj.calc_volume()
sph_obj.printArea()
sph_obj.printVolume()
