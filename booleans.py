a=int(input("Assing an integer value: "))
b=int(input("Assing an integer value: "))

print(a<b) #Booleans return "true" or "false" value
print(a>b)
print(a!=b)

if (a<b):
    print(b,"is greater than",a)

elif (a>b):
    print(a,"is greater than",b)

elif (a!=b):
    print(a,"is not equal with",b)

else:
    print(a,"is equal",b)