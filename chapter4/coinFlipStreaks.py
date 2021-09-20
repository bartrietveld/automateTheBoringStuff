import random

def hundredCoinFlips():
    # Returns a list of a hundred coinflips
    flips=[]
    for i in range(100):
        if random.randint(0,1) == 0:
            flips.append('H')
        else:
            flips.append('T')     
    # print(flips)
    return flips

def checkStreakofSix(list):
    # Takes a list
    # Returns True if at any point in the list, 6 the same values are present
    for i in range(len(list)-5):
        if all(list[i] == list[j] for j in range(i+1,i+6)):

            # print("There is a streak! Starting at index: "+str(i))
            return True
    return False
    
count = 0
for i in range(10000):
    if checkStreakofSix(hundredCoinFlips()) == True:
        count += 1

print(count)