list=[]

print(list)

list.append(3) #append takes only 1 argument
print(list)

list.clear() #clears list items
print(list)

list.extend("banana") #splits iterables into single letters
print(list)

aCount=list.count("a") #checks the occurancy of the give argument in the list
print(aCount)

indexVal=list.index("a") #searches for the given argument in the list and returns its first occurancy index
print(indexVal)

list.sort() #sorts the list elements with alphabetical order or value
print(list)

list.remove("a") #removes the first occurancy of given argument
print(list)