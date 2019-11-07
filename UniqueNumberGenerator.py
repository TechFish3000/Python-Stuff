# BY TECHFISH 3000


import random
EndString = ""
NumberFile = open("nums.txt", "w")
NumList: set = {"", }
Count = int(input("Amount of unique numbers?"))
RangeStart = int(input("Range starting point?"))
RangeStop = int(input("Range stopping point?"))
NumList.clear()
while len(NumList) != Count:
    NumList.add(random.randrange(RangeStart, RangeStop))

for i in NumList:
    EndString = EndString + "\n" + str(i)




NumberFile.write(EndString)
NumberFile.close()


