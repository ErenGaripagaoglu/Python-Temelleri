#-----Variable Classes-----#
"""
Immutable = (int, str, float, bool, tuple)
Mutable = (list, set, dictionary)

"""
#----Immutable----#

tuple1 = (1, 2)

var1 = tuple1 #This copys the value of the tuple1 and pastes it to var1

tuple1 = (1, 2, 3)

print(tuple1, var1)

#-----Mutable-----#

list1 = [1, 2]

var2 = list1 #This instances the value and attaches it to var2

list1[0] = [500] #This change will also effect on var2

print(list1, var2)

#-----------------#