a=[7,4,3,5,6]
for i in range(len(a)):
    for j in range(0,len(a)-1):
        if(a[i]<a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)

#optimal code 
class Solution:
    arr=[3,4,5,1,2]
    def getSecondLargest(self, arr):
        larg=arr[0]
        seclarg=-1
        for i in range(0,len(arr)):
            if(arr[i]>larg):
                seclarg=larg
                larg=arr[i]
            elif(arr[i]<larg and arr[i]>seclarg):
                seclarg=arr[i]
        return seclarg
                
    
            


    
        