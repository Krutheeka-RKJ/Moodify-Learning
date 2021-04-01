import numpy as np 
import matplotlib.pyplot as plt
import random  

def SwapEntries(arr):       #Swap 8 entries
    for i in range(8):
        x1=random.randint(0,99)
        y1=random.randint(0,149)
        x2=random.randint(0,99)
        y2=random.randint(0,149)
        temp=arr[x1,y1]
        arr[x1,y1]=arr[x2,y2]
        arr[x2,y2]=temp

def Mod1(arr,i,j):         #Modify the first neighbours
    a1 = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j+1),(i+1,j+1),(i+1,j),(i+1,j-1),(i,j-1)]
    OutofRange = []
    for ele in a1:
        if (ele[0]<0 or ele[1]<0 or ele[0]>99 or ele[1]>149):   #Removing elements
            OutofRange.append(ele)
    InRange = [i for i in a1 if i not in OutofRange]
    for index in InRange:
        if(arr[index[0],index[1]]==0):
            arr[index[0],index[1]] = np.random.choice([0,1],p = [0.75,0.25], size=(1))
    
def Mod2(arr,i,j):      #Modify second neighbours
    a1 = [(i-2,j-2),(i-2,j-1),(i-2,j),(i-2,j+1),(i-2,j+2),(i-1,j+2),(i,j+2),(i+1,j+2),(i+2,j+2),(i+2,j+1),(i+2,j),(i+2,j-1),(i+2,j-2),(i+1,j-2),(i,j-2),(i-1,j-2)]
    OutofRange = []
    for ele in a1:
        if (ele[0]<0 or ele[1]<0 or ele[0]>99 or ele[1]>149):
            OutofRange.append(ele)
    InRange = [i for i in a1 if i not in OutofRange]
    for index in InRange:
        if(arr[index[0],index[1]]==0):
            arr[index[0],index[1]] = np.random.choice([0,1],p = [0.92,0.08], size=(1))

arr = np.zeros((100,150), dtype= int)
arr[50,75] = 1
Numofiter = [0]
iterations=0
Numof1s=[1]
Changein1s=[0]
while True:
    pos1=[]
    ones=0
    SwapEntries(arr)
    for i in range(100):
        for j in range(150):
            if (arr[i,j]==1):
                pos1.append((i,j))
                ones+=1
            else:
                continue
    for pos in pos1:
        Mod1(arr,pos[0],pos[1])
        Mod2(arr,pos[0],pos[1])
    iterations+=1
    Numofiter.append(iterations)
    Numof1s.append(ones)
    Changein1s.append(Numof1s[-1]-Numof1s[-2])
    if ones==15000: break
print("The peak value in plot 2 is",max(Changein1s))

plt.subplot(2,1,1)
plt.plot(Numofiter,Numof1s)
plt.xlabel("Number of Iterations")
plt.ylabel("Number of ones in the matrix")

plt.subplot(2,1,2)
plt.plot(Numofiter,Changein1s)
plt.xlabel("Number of Iterations")
plt.ylabel("Change in number of ones in the matrix")
plt.show()





