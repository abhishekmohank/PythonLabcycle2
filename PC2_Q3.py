"""**3. Read the file 'iris.json' as a text file :**
1. Create a list having each line of the file as an element 
2. Convert it into a list of dictionary objects. 
3. Show the details of all flowers whose species is "setosa". 
4. Print the minimum petal area and max sepal area in each species 
5. Sort the list of dictionaries according to the total area are sepal and petal.
"""

import json

def readAsList(filepath):
  fp = open(filepath,'r')
  #list having each line of json as elements
  jsonList = fp.readlines()
  fp.close()
  return jsonList

def readAsListOfDict(filepath):
  fp = open(filepath,'r')
  #list having dictionary of objects.
  jsonData = json.load(fp)
  fp.close()
  return jsonData

def printSetosa(jsonList):
  #printing the details of only setosa.
  print("\nDetails of flowers of species setosa")
  for i in jsonList:
    if(i['species']=='setosa'):
      print(i)

def sepalAreaAndPetalArea(jsonList):
  #list to store species names.
  listOfSpeciesName = list()
  for i in jsonList:
    #appeding the different species name to the list.
    listOfSpeciesName.append(i['species'])
  #removing duplicates to get unique speices.
  listOfSpeciesName = list(set(listOfSpeciesName))
  #list to store sepal and petal area.
  sepalArea = list()
  petalArea = list()
  for i in listOfSpeciesName:
    for j in jsonList:
      if(j['species']==i):
        sepalArea.append(j['sepalLength']*j['sepalWidth'])
        petalArea.append(j['petalLength']*j['petalWidth'])
    print()
    print(i.capitalize())
    #printing minimum and maximum areas.
    print("Maximum Sepal Area in ",i.capitalize()," is ",round(max(sepalArea),2))
    print("Minimum Petal Area in ",i.capitalize()," is ",round(min(petalArea),2))
    sepalArea.clear()
    petalArea.clear()
    
def sortTotalArea(jsonList):
  for i in jsonList:
    #adding total area to the each dictionary
    totalArea = (i['petalLength']*i['petalWidth'])+(i['sepalLength']*i['sepalWidth'])
    i.update({'totalArea':round(totalArea,2)})
  #list sorted according to total area
  sortedList = sorted(jsonList,key=lambda i:i['totalArea'])
  print("\nList sorted on the basis of total area")
  for i in sortedList:
    print(i)

#path where target file is stored.
filePath = 'iris.json'
jsonList = readAsList(filePath)
print("List with each line as element\n")
for line in jsonList:
  print(line)

jsonData = readAsListOfDict(filePath)
print("\nList of Dictionaries")
for i in jsonData:
  for key, values in i.items():
    print(key.capitalize()+" : ",values,end=" , ")
  print()

printSetosa(jsonData)
sepalAreaAndPetalArea(jsonData)
sortTotalArea(jsonData)
