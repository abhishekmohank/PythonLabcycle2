"""**3. Read the file 'iris.json' as a text file :**
1. Create a list having each line of the file as an element 
2. Convert it into a list of dictionary objects. 
3. Show the details of all flowers whose species is "setosa". 
4. Print the minimum petal area and max sepal area in each species 
5. Sort the list of dictionaries according to the total area are sepal and petal.
"""

import json

myJson =  open('iris.json', 'r')
jsonData = myJson.read()
jsonList = json.loads(jsonData)

print("List having each line of json as elements")
print(jsonList)
print("\n")

print("List of Dictionary Objects")
for i in jsonList:
  
  print(i)
print("\n")

print("Details of Flowers whose species is Setosa")
for i in jsonList:
  if(i['species']=='setosa'):
    print(i)

listOfSpeciesName = list()
for i in jsonList:
  
  listOfSpeciesName.append(i['species'])  


listOfSpeciesName = set(listOfSpeciesName)

print('\n')

sepal_area = list()
petal_area = list()
for i in listOfSpeciesName:
  
  print(i.capitalize())
  for j in jsonList:
    
    if(j['species']==i):
      sepal_area.append(j['sepalLength']*j['sepalWidth'])
      petal_area.append(j['petalLength']*j['petalWidth'])
  
  print("Maximum Sepal Area in ",i.capitalize()," is ",round(max(sepal_area),2))
  print("Minimum Petal Area in ",i.capitalize()," is ",round(min(petal_area),2))  
  print('\n')
  
  sepal_area.clear()
  petal_area.clear()
print('\n')


jsonListCopy = list()
jsonListCopy = jsonList
for i in jsonListCopy:
  
  petalArea = (i["petalLength"]*i["petalWidth"])
  sepalArea = (i["sepalLength"]*i["sepalWidth"])
  totalArea = (petalArea+sepalArea)
  
  
  i.update({'totalArea':totalArea})

sortedList = (sorted(jsonListCopy, key = lambda i:i['totalArea'] ))

print("The Sorted List")

for i in sortedList:
  
  print(i)

myJson.close()