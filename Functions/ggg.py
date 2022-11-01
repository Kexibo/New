n=[2,7,11,15]
target=9
'''def foo(a,target):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]+a[j]==target:
                print(i,j,a[i],a[j])
            else:
                break
foo(a,target)'''
def foo(n,target):
    hashmap={}
    for i in range(len(n)):
        num=n[i]
        if num not in hashmap:
            hashmap[num]=[i]
        else:
            hashmap[num].append(i)
    for i in range(len(n)):
        num=n[i]
        x=target-num
        if x in hashmap:
            if num==x and len(hashmap[x])>=2:
                return hashmap[x][:2]
            if num!=x:
                return[i,hashmap[x][0]]
print(foo(n,target))

