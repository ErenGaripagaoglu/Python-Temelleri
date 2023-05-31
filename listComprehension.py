#-----List Comprehension-----#

list1 = [i for i in range(20)] 
#We can assign the variable thats going to be added to list, then we can run a for loop with this variable

print(list1)

#----------------------------#

list2 = [[j for j in range(3)] for i in range(1, 20)] 
#We can have multiple for loops linked to each other like this(one using other as variable)

print(list2)

#----------------------------#

list1 = [i for i in range(20) if i % 5 == 0] 
#We can add an if statement to filter the elements we want to be added into the list

print(list1)

#----------------------------#