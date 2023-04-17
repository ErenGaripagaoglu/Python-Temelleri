import random #here we import random module in order to use random functions.

integerValue = random.randint(0,100) #this line generates a number in range of 0 to 100
print(integerValue)

floatValue = random.random() #this line generates a float value between 0 to 1
print(floatValue)

rangeValue = random.randrange(0,10) #this line returns a value in range between given arguments
print(rangeValue)