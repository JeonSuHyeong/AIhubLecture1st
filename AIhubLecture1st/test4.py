listN = [1,3,2,5,4,7,6,10,8,9]
for i in range(0,len(listN)):
    for j in range(0,i):
        if(listN[i]<listN[j]):
            temp = listN[i]
            listN[i] = listN[j]
            listN[j] = temp
        
print(listN)

"""
listN = [1,3,2,5,4]
for i in range(0,5):
    for j in range(0,5):
        if(listN[i]<listN[j]):
            temp = listN[i]
            listN[i] = listN[j]
            listN[j] = temp
        
print(listN)
"""