#**2. Write a program to read a string containing numbers separated by a
#space and convert it as a list of integers. Perform the following
#operations on it.**

#1. Rotate elements in a list by 'k' position to the right

#2. Convert the list into a tuple using list comprehension

#3. Remove all duplicates from the tuple and convert them
#into a list again.

#4. Create another list by putting the results of the evaluation
#of the function 𝑓(𝑥) = 𝑥^2 – 𝑥 with each element in the
#final list

#5. After sorting them individually, merge the two lists to
#create a single sorted list.
#"""


def convertListToInt(stringList):
  int_list = [int(i) for i in stringList]
  return int_list

def rotateElements(targetList):
  #1.rotate the elements by 'k' position to right
  k = int(input("Enter the value by which you want to rotate : "))
  print("The list after rotating by",k,"position to right is ",end = " = ")
  print(targetList[-k:]+targetList[:-k])

def listToTuple(int_list):
  #2.converting the list into a tuple
  int_tuple = *(i for i in int_list),
  print("List to Tuple = ",int_tuple)
  return int_tuple

def removeDuplicates(int_tuple):
  #3.removing all duplicates
  int_tuple = tuple(set(int_tuple))
  int_list = list(int_tuple)
  return int_list

def mapToFunction(int_list):
  #4.mapping the list to the function f(x) = x^2-x
  square = [(i**2)-i for i in int_list]
  print("Results of the Function f(x) = (x^2-1) = ",square)
  return square

def singleSortedList(int_list,function_list):
  #5.merging the list in 4 and 5 into a single sorted list
  sorted_list = int_list + function_list
  sorted_list.sort()
  print("Final Sorted List = ",sorted_list)

number_string = input("Enter the list of numbers with a space : ")
#list of strings
list_numbers = list(number_string.split(" "))

#converting the list of string to list of integers.
int_list = convertListToInt(list_numbers)
print("The list of integers = ",int_list)
#rotating elements.
rotateElements(int_list)
#converting list to tuple.
int_tuple = listToTuple(int_list)
int_list = removeDuplicates(int_tuple)
print("Tuple to list after removing duplicates = ",int_list)
functionResult = mapToFunction(int_list)
singleSortedList(int_list,functionResult)
