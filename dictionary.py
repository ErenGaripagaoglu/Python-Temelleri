licensePlates={"İzmir" : 35 , "İstanbul" : 34 , "Ankara" : 6 }

print(licensePlates.items()) #returns the items(keys,values) in the dictionary
print(licensePlates.keys()) #returns the keys in the dict
print(licensePlates.values()) #returns the values in the dict

print(licensePlates.get("İzmir")) #returns the value of the given key

licensePlates.update({"Sivas":58})
print(licensePlates)

licensePlates.pop("İstanbul") #removes the given key with its value from the dictionary
print(licensePlates)