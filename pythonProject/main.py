'''x=[1,1]
for i in range(100):
    x.append(i+x[i+1])
    print(x)



def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(20))'''
n=int(input())
arr=[1]*(n+1)
#print(arr)
for i in range(2,n+1):
    arr[i]=arr[i-1]+arr[i-2]
    #print(arr)
print(arr[-1])