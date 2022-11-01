arr=[1,1]
n=int(input())
i=1
while i<n:
    arr=[arr[1],arr[0]+arr[1]]
    i+=1
print(arr[-1])