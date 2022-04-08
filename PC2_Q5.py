"""    **5. Write a program to create a parent class, 3DShapes, with methods
printVolume() and printArea(), which prints the Volume and Area,
respectively. Create classes Cylinder and Sphere by inheriting
3DShapes class. Using these child classes, calculate and print the
volume and area of a cylinder and sphere.**

"""

class threeD_Shapes:
  def printVolume(self):
    print("The Volume is ",self._volume)
  def printArea(self):
    print("The Area is ",self._area)
  
class cylinder(threeD_Shapes):
  def __init__(self,r,h):
    self.__radius = r
    self.__height = h
  def calc_area(self):
    self._area = 2*3.14*self.__radius*(self.__radius+self.__height)
  def calc_volume(self):
    self._volume = round((3.14*self.__radius*self.__radius*self.__height),2)

class sphere(threeD_Shapes):
    def __init__(self,r):
      self.__radius = r
    def calc_area(self):
      self._area = 4*3.14*self.__radius*self.__radius
    def calc_volume(self):
      self._volume = round(((4/3)*3.14*(self.__radius**3)),2)

cylinder_radius = int(input("Enter the radius of the cylinder "))
cylinder_height = int(input("Enter the height of the cylinder "))
cyl_obj = cylinder(cylinder_radius,cylinder_height)
cyl_obj.calc_area()
cyl_obj.printArea()
cyl_obj.calc_volume()
cyl_obj.printVolume()

sphere_radius = int(input("\nEnter the radius of the sphere "))
sph_obj = sphere(sphere_radius)
sph_obj.calc_area()
sph_obj.calc_volume()
sph_obj.printArea()
sph_obj.printVolume()
