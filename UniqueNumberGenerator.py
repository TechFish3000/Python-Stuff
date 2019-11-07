# BY TECHFISH 3000


import random
strig = ""
nums = open("nums.txt", "w")
numlist: set = {"", }
many = int(input("How many?"))
r = int(input("Range start?"))
s = int(input("range stop?"))
numlist.clear()
while len(numlist) != many:
    numlist.add(random.randrange(r, s))

for i in numlist:
    strig = strig + "\n" + str(i)




nums.write(strig)
nums.close()


