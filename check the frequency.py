testDict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'coding' : 1}

print("the original dictionar:" + str(testDict))

k = 2 

res = 0 
for key in testDict:
    if testDict[key] == k:
        res += 1

print("The frequency of k is:" + str(res))
