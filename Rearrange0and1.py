#Rearrange 0 and 1
#https://www.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1
#User function Template for python3

class Solution:
    def segregate0and1(self, arr):
        i = 0
        j=len(arr)-1
        while i<j:
            if arr[i]<1 and arr[j]>0:
                i=i+1
                j=j-1
            elif arr[i]>0 and arr[j]<1:
                temp = arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                i=i+1
                j=j-1
            elif arr[i]>0 and arr[j]>0:
                j=j-1
            elif arr[i]<1 and arr[j]<1:
                i=i+1
        else:
            return arr