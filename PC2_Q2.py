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


number_string = input("Enter the list of numbers with a space : ")

list_numbers = list(number_string.split(" "))

int_list = []
for i in list_numbers:
  int_list.append(int(i))
print("The list of integers = ",int_list)


k = int(input("Enter the value by which you want to rotate : "))
print("The list after rotating by",k,"position to right is ",end = " = ")
print(int_list[-k:]+int_list[:-k])


int_tuple = tuple(int_list)
print("List to Tuple = ",int_tuple)

int_tuple = tuple(set(int_tuple))
int_list = list(int_tuple)
print("Tuple to list after removing duplicates ",end = " = ")
print(int_list)

square = []
for i in int_list:
  square.append((i**2)-i)
print("Results of the Function ",end = " = ")
print(square)

sorted_list = int_list + square
sorted_list.sort()
print("Final Sorted List ",end = " = ")
print(sorted_list)
