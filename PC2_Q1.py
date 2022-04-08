"""
**1. Suppose a newly born pair of rabbits, one male and one female, are
put in a field. Rabbits can mate at the age of one month so that at the
end of its second month, a female has produced another pair of
rabbits. Suppose that our rabbits never die and that the female always
produces one new pair every month from the second month.

Develop a program to show a table containing the number of pairs of
rabbits in the first N months.**
"""

n = int(input("Enter the month upto which you want the table : "))
#adding the first no of pairs of rabbit to the list
rabbit_pair = [1,1]
print("\nMonths\t\tNo of Pairs of Rabbit")
#loop used to iterate upto n-months
for i in range(0,n):
  #printing the month
  print(i+1,end="\t\t")
  #printing the pair of rabbits
  print(rabbit_pair[i])
  rabbit_pair.append(rabbit_pair[i]+rabbit_pair[i+1])
