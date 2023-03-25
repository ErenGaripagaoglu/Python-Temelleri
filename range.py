a=int(input("Assign an integer value: "))
b=int(input("Assign an integer value: "))

l=[]
for i in range(a,b): #range is used when a <= i < b so it doesnt get to value b
    l.append(i)
print(l)


l=[]
for i in range(a,b+1):
    l.append(i)
print(l)