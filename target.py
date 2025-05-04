'''Given an array of integers arr and an integer target, return indices of the two numbers such that they add up to target.
'''

arr=list(map(int,input().split()))
target=int(input())
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print("output",i,j)
