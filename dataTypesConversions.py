thisIsString1="This is string with (\") "
print(thisIsString1)

thisIsString2='This is string with (\') '
print(thisIsString2)

thisIsMultipleLineString="""This is a multiple line string. 
That can be used with \"\"\" (three quotes)"""
print(thisIsMultipleLineString)

thisIsInteger=35
print("This is integer:",thisIsInteger)

thisIsFloat=2.5
print("This is float:",thisIsFloat)

print("-"*50) #

print(thisIsInteger,type(thisIsInteger))

intToString=str(thisIsInteger)              #str() converts the variable into string if possible
print(intToString,type(intToString))

intToFloat=float(thisIsInteger)             #float() for converting into float
print(intToFloat,type(intToFloat))

floatToInt=int(thisIsFloat)          #int() for converting into integer; floors into integer 
print(floatToInt,type(floatToInt)) 